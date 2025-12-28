# Project State — flake-finder

## Purpose
The flake-finder project aims to automate the detection and future layer
classification of exfoliated 2D material flakes (graphene, hBN, TMDCs) from
optical microscope images of Si/SiO₂ chips.

This project is developed as a **scientific and educational tool** intended for
long-term institutional use and collaboration.

---

## Current Status
- **Milestone 0 — Baseline Flake Detection:** COMPLETE
- **Milestone 1 — Detector Robustness & Diagnostics:** PLANNED

---

## Frozen Components
The following components are considered stable and should not be modified
without explicit intent:

- Baseline detector implementation (`scripts/infer_baseline.py`)
- Detector outputs:
  - `outputs/overlay.png`
  - `outputs/flakes.csv`
- Milestone 0 documentation (`docs/milestone_0.md`)
- Overall pipeline structure (detector → cropper → classifier)

---

## Active Development Principles
- All development occurs on feature branches
- The `main` branch remains stable and reproducible
- Each milestone represents a coherent, reviewable unit of work
- Machine learning models are introduced **only after** dataset quality is validated

---

## Near-Term Goal (Milestone 1)
Improve detector reliability and scientific transparency by:
- Making detection failures diagnosable
- Saving intermediate processing outputs
- Supporting tuning across substrates and microscopes

---

## Constraints
- Scientific correctness over performance
- Reproducibility over cleverness
- Explicit, inspectable pipeline stages
- Clear separation between detection and classification
