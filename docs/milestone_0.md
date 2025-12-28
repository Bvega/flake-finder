# Milestone 0 — Baseline Flake Detection Pipeline

## Overview
Milestone 0 establishes a complete, reproducible baseline pipeline for automated
flake localization in optical microscope images of exfoliated 2D materials
(graphene, hBN, TMDCs) on Si/SiO₂ substrates.

The purpose of this milestone is to automate **where flakes are located** in a
full-chip image and export these locations in a structured form suitable for
dataset construction and future machine learning.

This milestone intentionally does **not** attempt to classify material type or
layer thickness.

---

## Key Concepts

### Detector
A **detector** answers the question:

> “Where are candidate flakes in this image?”

It outputs spatial regions of interest (bounding boxes or masks).

### Classifier (future milestone)
A **classifier** answers the question:

> “What is this flake?”

It outputs material identity and/or layer count (mono / bi / tri) with confidence.

---

## Pipeline Overview

[ Full chip optical image ]
|
v
+-------------------+
| DETECTOR | ← Milestone 0 (current)
| (classical CV) |
+-------------------+
|
v
[ Bounding boxes of candidate flakes ]
|
v
+-------------------+
| CROPPER | ← Milestone 1–2
| (ROI extraction) |
+-------------------+
|
v
[ Individual flake images ]
|
v
+-------------------+
| CLASSIFIER | ← Milestone 3+
| (ML / PyTorch) |
+-------------------+
|
v
[ Material + layer count + confidence ]


---

## Inputs and Outputs

### Input
- Full optical microscope image of a chip (PNG / JPG / TIF)

### Outputs
- `outputs/overlay.png`  
  Image showing detected flake bounding boxes
- `outputs/flakes.csv`  
  Table with one row per detected flake:
id, x, y, w, h, area

---

## Detection Method (Milestone 0)
The baseline detector uses classical computer vision for transparency and
scientific interpretability:

- LAB color space conversion
- CLAHE normalization on the L channel (illumination robustness)
- Edge detection (Canny)
- Adaptive thresholding
- Morphological cleanup
- Contour extraction
- Geometric and area-based filtering

This approach is robust, explainable, and suitable as a foundation for future
extensions.

---

## Code-to-Pipeline Mapping

| Pipeline Component | File | Purpose |
|------------------|------|---------|
| Detector | `scripts/infer_baseline.py` | Runs CV pipeline and exports results |
| Image I/O | `src/flake_finder/utils/io.py` | Image loading and directory creation |
| Visualization | `src/flake_finder/utils/viz.py` | Draw bounding boxes and labels |
| Sanity check | `scripts/hello.py` | Environment verification |

---

## Why Detector Quality Matters
Detector performance sets the upper bound for future layer classification accuracy:

1. **Missed flakes produce no data**  
 Undetected flakes cannot be cropped, labeled, or learned from.

2. **Poor bounding boxes degrade optical features**  
 Layer classification relies on subtle optical contrast relative to the
 substrate. Incorrect crops distort these features.

3. **False positives waste labeling effort**  
 Dust and artifacts increase noise and slow down dataset curation.

4. **Error propagation**
Bad detection → bad crop → noisy features → wrong labels → weaker ML model


For scientific reliability and institutional deployment, detector robustness must
be addressed before introducing machine learning.

---

## Status
**Milestone 0: COMPLETE**

The repository contains a reproducible, end-to-end baseline detector with
structured outputs and a clean version-control workflow. This milestone provides
the foundation for dataset generation and ML-based layer classification in future
work.
