# Methods Log

## 2026-09-11

- Established the project as a comparative audit of AI translation infrastructure and language access.
- Selected Amharic and Afaan Oromo as the initial empirical case.
- Built development corpus v0.2 with 40 candidate-aligned English–Amharic–Afaan Oromo units.
- Preserved official agency translations as institutional references rather than unquestioned gold standards.
- Selected Meta `facebook/seamless-m4t-v2-large` as the reproducible Meta system.
- Ran Meta inference in Google Colab with GPU support.
- Recorded environment: pandas 2.2.3, PyTorch 2.11.0+cu128, Transformers 5.17.0.
- Generated 40 Amharic and 40 Afaan Oromo Meta outputs with no missing values.
- Cleaned only serialization/list wrappers; no linguistic post-editing.
- Began Google Translate public-web collection, one source unit at a time.
- Planned blinded human evaluation of semantic fidelity, pragmatic fidelity, institutional fidelity, and actionability.

## Rules for future entries

Append rather than overwrite major methodological changes. Record:
- corpus version
- collection dates
- model/checkpoint revisions
- software versions
- interface changes
- alignment/adjudication decisions
- deviations from protocol
