# When Translation Is Not Access

## AI Translation Infrastructure and Communicative Inequality in Under-Resourced Languages

This repository contains research materials for an ongoing communication study of how global platform companies build, distribute, and operationalize AI translation infrastructure for under-resourced languages.

The empirical study focuses on **Amharic and Afaan Oromo** and compares translation outputs from **Google Translate** and **Meta SeamlessM4T v2** using public-facing institutional communication from education, elections/civic services, and health contexts.

The project asks a broader question than whether machine translation is "accurate":

> When does AI translation provide meaningful communicative access, and when does it merely create the appearance of access?

## Research focus

The study examines AI translation at two connected levels:

1. **Translation performance** — whether systems preserve semantic meaning, pragmatic force, institutional terminology, eligibility conditions, deadlines, rights, obligations, and actionable instructions.
2. **Translation infrastructure** — how global platforms organize language support, model availability, product interfaces, technical resources, and uneven linguistic capacity across languages.

The project therefore treats translation systems as **communicative infrastructure**, not merely as language models.

## Current development corpus

The current `v0.2` corpus contains **40 candidate-aligned English–Amharic–Afaan Oromo units** drawn from official Minnesota public-facing materials:

- 20 education units
- 19 civic/election units
- 1 health/TB pilot unit

Official Amharic and Afaan Oromo translations are retained as **institutional reference translations**, not assumed to be perfect linguistic gold standards.

All current alignments remain subject to native-speaker review and adjudication.

## AI systems

### Meta
The reproducible Meta condition uses:

`facebook/seamless-m4t-v2-large`

The current development run generated:
- 40 Amharic outputs
- 40 Afaan Oromo outputs
- 0 missing outputs

This is a reproducible Meta research-model condition and should not be treated as equivalent to the live translation stack used in Facebook or Instagram products.

### Google
Google Translate outputs were collected from the public web interface one source unit at a time to preserve item independence and audit the product ordinary users encounter.

The current collection contains:
- 40 Amharic outputs
- 40 Afaan Oromo outputs
- 0 missing outputs

## Evaluation framework

Human evaluation separates four dimensions:

- **Semantic fidelity** — preservation of propositional meaning
- **Pragmatic fidelity** — preservation of communicative force, modality, uncertainty, urgency, and conditionality
- **Institutional fidelity** — preservation of rights, eligibility, procedures, status, deadlines, and institution-specific meanings
- **Actionability** — whether a target-language reader could reasonably take the correct next step

A qualitative error taxonomy tracks omissions, additions, negation changes, modality shifts, eligibility shifts, deadline/number errors, institutional-term errors, ambiguity, pragmatic loss, and actionability failures.

Two researchers will score the same blinded outputs independently. Inter-rater agreement will be calculated before disagreements are adjudicated. Original reviewer scores will be preserved separately from adjudicated final scores.

## Methods and reviewer tools

The repository includes the current methodological tools used for the human-evaluation stage:

- [`methods/PROTOCOL.md`](methods/PROTOCOL.md) — corpus and evaluation protocol
- [`methods/METHODS_LOG.md`](methods/METHODS_LOG.md) — running methods log
- [`methods/CODEBOOK.md`](methods/CODEBOOK.md) — project coding framework
- [`methods/REVIEWER_CODEBOOK.md`](methods/REVIEWER_CODEBOOK.md) — 1–5 scoring anchors, error taxonomy, reviewer rules, and examples
- [`methods/TWO_REVIEWER_WORKFLOW.md`](methods/TWO_REVIEWER_WORKFLOW.md) — independent two-reviewer and adjudication procedure
- [`methods/INTER_RATER_RELIABILITY_PLAN.md`](methods/INTER_RATER_RELIABILITY_PLAN.md) — reliability analysis plan to be implemented after independent coding is complete

## Repository structure

```text
data/
  development/     development corpus and system outputs
  sources/         source inventory and provenance
scripts/           reproducible model-inference code
methods/           protocol, methods log, codebooks, reviewer workflow, and reliability plan
docs/              research design and theoretical framework
```

## Development status

This is an active research repository. The current data are a **development corpus**, not yet a validated gold benchmark. The repository is public for transparency and reproducibility, but corpus versions should not be treated as final until native-speaker review and adjudication are complete.

## Target scholarly contribution

The project is being developed as a communication study, with *Human Communication Research* as the current target journal. Its intended contribution is theoretical as well as empirical: to conceptualize AI translation as an uneven communicative infrastructure through which platform companies shape access to institutional information across languages.

## Researcher

**Endalkachew H. Chala**  
Center for an Informed Public, University of Washington  
ORCID: https://orcid.org/0000-0001-6210-6706  
Website: https://endalk-chala.github.io/

## Citation

Citation metadata will be finalized when the development corpus reaches a stable public release.
