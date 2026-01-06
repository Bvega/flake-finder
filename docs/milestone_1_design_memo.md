TASK: Add the approved Milestone 1 design memo to the repo as a tracked file.

BRANCH:
- Create and switch to a new branch: milestone-1-design-memo

FILES:
- Create: docs/milestone_1_design_memo.md

CONTENT:
- Use EXACTLY the following markdown content (no edits, no reformatting):

# 📄 Milestone 1 Design Memo
## Detector Robustness & Diagnostics

**Status:** Design-only, pre-decision  
**Decisions:** None made  
**Purpose:** Shared understanding and structured discussion

---

## 1. Background & Motivation

The current detector pipeline produces scientifically meaningful outputs, but when results are incorrect or surprising, it is often difficult to determine **why**.

Typical challenges include:
- Lack of visibility into intermediate processing stages
- Implicit assumptions about image quality, substrate, or microscope setup
- Difficulty reproducing results across environments or collaborators
- Parameter tuning that risks becoming ad hoc or non-reproducible

**Milestone 1** is intended to address these challenges by improving **robustness** and **diagnostic transparency**, while preserving the integrity of the existing baseline detector.

---

## 2. Scope of Milestone 1

### What this milestone *is about*
- Making detector behavior **explainable and diagnosable**
- Enforcing explicit assumptions and invariants
- Capturing sufficient context to enable reproducibility
- Supporting careful, configuration-based tuning (not code edits)
- Preserving scientific correctness over convenience or speed

### What this milestone is *not*
- No changes to the baseline detector algorithm
- No changes to baseline detector outputs
- No changes to the pipeline structure (detector → cropper → classifier)
- No classifier improvements
- No performance optimization unless required for correctness

All work in this milestone is **additive** and respects frozen components defined in `PROJECT_STATE.md`.

---

## 3. Scientific and Engineering Principles

This milestone is guided by the following principles:

1. **Scientific correctness over performance**  
   Prefer interpretable, conservative behavior to fast but opaque results.

2. **Reproducibility by construction**  
   Runs should be reproducible from saved artifacts and configuration alone.

3. **Explicit, inspectable stages**  
   Intermediate processing steps should be observable, not hidden.

4. **Separation of concerns**  
   Detection robustness and diagnostics should not bleed into classification logic.

---

## 4. Failure Modes We Want to Diagnose

Rather than solving all failure modes perfectly, Milestone 1 aims to make them **visible and explainable**.

### Input / Acquisition
- Blur or defocus
- Over/under-exposure or saturation
- Uneven illumination
- Dust or contamination
- Incorrect magnification or scale assumptions

### Substrate / Sample Variability
- Oxide thickness differences
- Material-dependent contrast changes
- Residue patterns mistaken for flakes

### Algorithmic / Parameter Sensitivity
- Normalization mismatch
- Threshold brittleness
- Morphological over- or under-merging
- Noise amplification

### Runtime / Environment
- Non-determinism
- Dependency or version drift
- File I/O failures

For each category, the goal is to provide:
- a detectable signal,
- recorded evidence,
- and enough context to support reasoning and tuning.

---

## 5. Robustness: Design Options (No Decisions Yet)

### Option A — Input Invariants & Early Validation
Define explicit checks on inputs and intermediate states to detect invalid or suspicious conditions early.

**Pros**
- Simple and foundational
- Improves scientific rigor
- Scales well as the system grows

**Cons**
- Requires careful definition of thresholds and heuristics

---

### Option B — Profile-Based Parameterization
Use named configuration profiles for different microscope or substrate setups, allowing tuning without code changes.

**Pros**
- Essential for scaling across setups
- Encourages reproducible tuning

**Cons**
- Risk of configuration sprawl if introduced too early

---

### Option C — Safe Fallback Semantics
When conditions are suspicious, prefer “no detection with explanation” over potentially misleading detections.

**Pros**
- Scientifically honest
- Prevents confident but incorrect outputs

**Cons**
- May reduce recall in edge cases

---

## 6. Diagnostics: Conceptual Direction

A central idea under discussion is treating diagnostics as **first-class artifacts**, potentially including:
- A run manifest (inputs, configuration, environment)
- Saved intermediate images and masks
- Structured diagnostic events
- Simple summary metrics

These artifacts would support:
- offline debugging,
- collaboration,
- and reproducible investigation of failures.

Whether diagnostics are always-on or opt-in remains an open question.

---

## 7. Operator Perspective

From a user or researcher standpoint, the desired workflow is:

1. Observe an unexpected detection result
2. Inspect saved run context and intermediate artifacts
3. Identify where and why behavior diverged
4. Adjust configuration (not code)
5. Re-run and compare results

The intent is to make debugging **methodical rather than ad hoc**.

---

## 8. Open Questions for Discussion

- Which robustness options should be considered core vs future?
- How much diagnostic data should be retained per run?
- How many microscope/substrate profiles do we realistically expect?
- Are there any data retention or privacy constraints?
- What level of tooling is appropriate (CLI-only vs human-browsable)?

---

## 9. Purpose of This Memo

This document exists to:
- align understanding,
- surface trade-offs,
- and enable informed discussion.

It is **not** a decision record and **not** an implementation plan.

---

*End of memo.*

VALIDATION:
- Ensure the file path is exactly docs/milestone_1_design_memo.md
- Do not modify any other files.

GIT:
- git status should show only the new markdown file.
- Commit message: "docs: add Milestone 1 design memo"
- Open a PR to main titled: "Docs: Milestone 1 design memo"

OUTPUT:
- Provide the exact git commands you ran
- Provide the PR link or PR title and branch name
