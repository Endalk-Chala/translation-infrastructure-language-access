# Protocol draft v0.3

## Inclusion
Select public-facing institutional messages with consequences for:
- rights
- eligibility
- service access
- deadlines or time windows
- required documentation
- medical understanding
- institutional decision-making

## Alignment
A row may enter the development set when:
1. all three texts come from official source materials;
2. the units are plausibly semantically parallel;
3. source URLs are retained;
4. no missing or invented translation is silently supplied.

A row becomes validated only after language-competent review and adjudication.

Official institutional translations are treated as **institutional references**, not automatically as perfect linguistic gold standards.

## System-output collection
For each English source:
- collect Google Amharic from the Google Translate web interface;
- collect Google Afaan Oromo from the Google Translate web interface;
- generate Meta Amharic using the reproducible research model condition;
- generate Meta Afaan Oromo using the reproducible research model condition;
- record collection date, interface/product, model, and relevant settings.

The Meta research condition uses `facebook/seamless-m4t-v2-large`. It is not assumed to be identical to the live translation systems used in Facebook or Instagram products.

## Human evaluation
Two researchers independently score the same blinded outputs. System identity is hidden during independent evaluation.

Each output is scored separately on:
- semantic fidelity
- pragmatic fidelity
- institutional fidelity
- actionability

Each dimension uses a 1–5 ordinal scale defined in `REVIEWER_CODEBOOK.md`.

Reviewers may assign multiple qualitative error codes and write explanatory notes.

## Error taxonomy
- omission
- addition
- negation_flip
- modality_shift
- eligibility_shift
- deadline_or_number_error
- institutional_term_error
- register_or_tone_shift
- ambiguity
- cultural_pragmatic_loss
- actionability_failure

## Independence and reliability
1. Reviewer 1 completes the blinded evaluation independently.
2. Reviewer 2 completes the same evaluation without seeing Reviewer 1 ratings.
3. Inter-rater agreement is calculated on the original independent ratings.
4. Reviewers then discuss disagreements.
5. Adjudicated scores and error codes are recorded separately.
6. Original reviewer ratings are preserved and are never overwritten.

The current reliability plan is documented in `INTER_RATER_RELIABILITY_PLAN.md`.

## Adjudication
Adjudication occurs only after independent scoring and the reliability calculation. The adjudicated dataset is used for final comparative interpretation, while the original independent scores remain the evidence for inter-rater reliability.

## Core analytic principle
A translation can be fluent and semantically plausible while still failing as language access if it changes the practical meaning of a right, deadline, eligibility rule, institutional term, warning, or required action.
