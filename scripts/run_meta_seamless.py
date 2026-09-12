"""
Generate Meta SeamlessM4T v2 Large text-to-text outputs.

NOTE:
The checkpoint is large (about 2.3B parameters). A GPU/Colab environment is strongly
recommended. Do not run this blindly on a low-memory laptop.

Input CSV must contain columns: item_id, english
"""

import argparse
import pandas as pd
import torch
from transformers import AutoProcessor, SeamlessM4Tv2Model

MODEL_ID = "facebook/seamless-m4t-v2-large"


def translate_text(model, processor, text, tgt_lang, device):
    inputs = processor(text=text, src_lang="eng", return_tensors="pt")
    inputs = {k: v.to(device) for k, v in inputs.items()}
    with torch.inference_mode():
        output_tokens = model.generate(
            **inputs,
            tgt_lang=tgt_lang,
            generate_speech=False
        )
    if isinstance(output_tokens, tuple):
        output_tokens = output_tokens[0]
    return processor.decode(output_tokens[0].tolist(), skip_special_tokens=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", default="meta_outputs.csv")
    args = ap.parse_args()

    df = pd.read_csv(args.input)
    if not {"item_id", "english"}.issubset(df.columns):
        raise ValueError("Input needs item_id and english columns.")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print("Device:", device)
    if device == "cpu":
        print("WARNING: This 2.3B model can be slow/heavy on CPU.")

    processor = AutoProcessor.from_pretrained(MODEL_ID)
    dtype = torch.float16 if device == "cuda" else torch.float32
    model = SeamlessM4Tv2Model.from_pretrained(MODEL_ID, torch_dtype=dtype).to(device)
    model.eval()

    am, om = [], []
    for i, row in df.iterrows():
        text = str(row["english"])
        print(f"{i+1}/{len(df)} {row['item_id']}")
        am.append(translate_text(model, processor, text, "amh", device))
        om.append(translate_text(model, processor, text, "gaz", device))

    out = df.copy()
    out["meta_model_name"] = MODEL_ID
    out["meta_amharic"] = am
    out["meta_oromo"] = om
    out.to_csv(args.output, index=False, encoding="utf-8-sig")
    print("Saved:", args.output)


if __name__ == "__main__":
    main()
