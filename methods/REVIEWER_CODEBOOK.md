# Reviewer Codebook

## AI Translation Infrastructure and Language Access

This guide is used to score blinded machine-translation outputs in the project **When Translation Is Not Access: AI Translation Infrastructure and Communicative Inequality in Under-Resourced Languages**.

Reviewers should score each output independently against the English source and the official institutional reference translation. Reviewers should not infer which system produced Output A or Output B.

The English source is the primary semantic anchor. The official Amharic or Afaan Oromo translation is an **institutional reference**, not an unquestioned gold standard.

## General 1–5 scale

| Score | Interpretation | Decision rule |
|---|---|---|
| 5 | Fully preserved | Meaning and communicative function are preserved with no consequential error. |
| 4 | Minor issue | Small wording, fluency, or register issue; intended meaning and practical action remain intact. |
| 3 | Noticeable problem | Meaning is mostly recoverable, but there is a meaningful distortion, ambiguity, or loss that could affect understanding. |
| 2 | Major problem | A substantial semantic, pragmatic, institutional, or action-related error could mislead the reader. |
| 1 | Severe failure | Contradiction, omission, reversal, or other failure substantially changes the message or could lead to incorrect action. |

## Dimension-specific scoring anchors

### Semantic fidelity

- **5:** Propositional meaning is fully preserved.
- **4:** Minor lexical or fluency issue; meaning is unchanged.
- **3:** Core meaning is recoverable, but one meaningful detail is distorted or unclear.
- **2:** Major content loss, addition, or mistranslation changes substantial meaning.
- **1:** Meaning is reversed, contradicted, largely missing, or unintelligible.

### Pragmatic fidelity

- **5:** Communicative force, modality, tone, uncertainty, urgency, and conditionality are preserved.
- **4:** Minor shift in tone or register with no practical consequence.
- **3:** Noticeable shift in force or stance; the reader may interpret obligation, certainty, politeness, or urgency differently.
- **2:** Major shift in modality or force is likely to mislead about what is required, allowed, likely, or urgent.
- **1:** Pragmatic force is reversed or destroyed, for example *may* becomes *must*, *must* becomes optional, or a warning is neutralized.

### Institutional fidelity

- **5:** Rights, eligibility, procedures, status, deadlines, roles, and institutional terms are preserved.
- **4:** Minor terminology variation with institutional meaning intact.
- **3:** Institutional meaning is mostly recoverable but one term, condition, or relationship is imprecise.
- **2:** A consequential institutional condition, role, eligibility rule, procedure, or deadline is distorted.
- **1:** The translation changes or erases a right, requirement, eligibility condition, institutional role, or procedural consequence.

### Actionability

- **5:** A target-language reader could take the correct next step from the translation alone.
- **4:** Correct action remains clear despite minor wording issues.
- **3:** The reader can probably act correctly, but ambiguity or missing detail creates some risk.
- **2:** The reader could reasonably take the wrong action, miss a requirement, or fail to act.
- **1:** The translation directs, strongly implies, or leaves the reader unable to avoid an incorrect action.

## Error taxonomy

Multiple tags may be applied to one output.

| Error type | Definition | Use when... |
|---|---|---|
| `omission` | Source content is missing from the translation. | A word, clause, condition, qualifier, actor, or instruction disappears. |
| `addition` | Translation introduces content not supported by the source. | New information, condition, actor, or implication appears. |
| `negation_flip` | Positive/negative meaning is reversed or negation is lost. | *Cannot* becomes *can*, *does not* becomes *does*, etc. |
| `modality_shift` | Obligation, permission, possibility, certainty, or recommendation changes. | *Must*, *may*, *should*, *can*, or equivalent force is altered. |
| `eligibility_shift` | Who qualifies, is covered, or is excluded changes. | Age, residency, status, enrollment, or another qualifying condition changes. |
| `deadline_or_number_error` | A number, date, duration, quantity, or deadline is wrong. | 20 days becomes 30 days, eight becomes another number, dates or months shift. |
| `institutional_term_error` | A role, program, document, procedure, agency, or legal/institutional term is mistranslated. | Election judge, precinct, EL support, assessment name, ID type, etc. changes meaning. |
| `register_or_tone_shift` | Register, politeness, formality, or tone shifts in a way relevant to interpretation. | An official instruction becomes casual, harsh, vague, or socially inappropriate. |
| `ambiguity` | Translation creates avoidable uncertainty between plausible interpretations. | The reader cannot tell which actor, condition, object, or action is intended. |
| `cultural_pragmatic_loss` | Contextual or culturally meaningful pragmatic information is weakened or lost. | A phrase is literally translated but social or interactional meaning is not preserved. |
| `actionability_failure` | Translation prevents or risks the correct practical next step. | A reader may register incorrectly, miss documentation, misunderstand eligibility, or take another wrong action. |

## Reviewer rules

1. **Score outputs independently.** Do not let the quality of Output A influence the score assigned to Output B.
2. **Use both source and reference.** The English source is the primary semantic anchor; the official translation is an institutional reference rather than an unquestioned gold standard.
3. **Prioritize consequential meaning.** Small stylistic differences should not receive large penalties unless they affect understanding, institutional meaning, or action.
4. **Multiple errors are allowed.** Apply more than one error tag when distinct problems occur in the same output.
5. **Do not mentally repair the translation.** Score the text as written; do not infer missing content simply because the intended source meaning is obvious.
6. **Record uncertainty.** Use reviewer notes when a judgment depends on dialect, terminology, or a reference translation that itself appears questionable.
7. **Adjudication should preserve disagreement.** Keep original reviewer ratings and record the final adjudicated decision separately rather than overwriting initial judgments.

## Hypothetical examples

- Source: **“You may register on Election Day.”** Translation: **“You must register on Election Day.”**  
  Semantic content is related, but pragmatic and institutional force changes permission into obligation. Tag `modality_shift`; pragmatic and institutional scores should fall substantially.

- Source: **“Bring one proof of residence.”** Translation omits **“one.”**  
  This may affect institutional fidelity and actionability if the quantity is procedurally meaningful.

- Source: **“You cannot spread TB to others.”** Translation: **“You can spread TB to others.”**  
  Severe `negation_flip`. Semantic and actionability scores should be 1.

- Source: **“A registered voter can vouch for up to eight voters.”** Translation preserves all meaning but is slightly awkward.  
  Likely 4 or 5 on semantic, institutional, and actionability dimensions. Do not over-penalize stylistic awkwardness.

## Core methodological principle

A translation can be fluent and semantically plausible while still failing as language access if it changes the practical meaning of a right, deadline, eligibility rule, institutional term, warning, or required action.
