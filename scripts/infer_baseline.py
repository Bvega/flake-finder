from __future__ import annotations

import argparse
import csv

import cv2
import numpy as np

from flake_finder.utils.io import read_image, mkdir_p
from flake_finder.utils.viz import draw_boxes


def detect_candidates(image_bgr: np.ndarray, min_area: float, max_area: float):
    h, w = image_bgr.shape[:2]

    lab = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2LAB)
    L, A, B = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    L2 = clahe.apply(L)

    edges = cv2.Canny(L2, 40, 120)

    thr = cv2.adaptiveThreshold(
        L2,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        35,
        2,
    )

    mask = cv2.bitwise_or(edges, thr)

    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, k, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, k, iterations=1)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    boxes, areas = [], []
    for c in contours:
        area = float(cv2.contourArea(c))
        if area < min_area or area > max_area:
            continue

        x, y, bw, bh = cv2.boundingRect(c)

        if bw > 0.95 * w and bh > 0.95 * h:
            continue
        if bw < 5 or bh < 5:
            continue

        boxes.append((int(x), int(y), int(bw), int(bh)))
        areas.append(area)

    return boxes, areas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--image", required=True, help="Path to chip image (png/jpg/tif)")
    ap.add_argument("--outdir", default="outputs", help="Output directory")
    ap.add_argument("--min-area", type=float, default=500, help="Min contour area")
    ap.add_argument("--max-area", type=float, default=2e7, help="Max contour area")
    args = ap.parse_args()

    outdir = mkdir_p(args.outdir)

    img = read_image(args.image)
    boxes, areas = detect_candidates(img, args.min_area, args.max_area)

    labels = [str(i) for i in range(len(boxes))]
    overlay = draw_boxes(img, boxes, labels=labels)

    overlay_path = outdir / "overlay.png"
    csv_path = outdir / "flakes.csv"

    cv2.imwrite(str(overlay_path), overlay)

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "x", "y", "w", "h", "area"])
        for i, ((x, y, ww, hh), area) in enumerate(zip(boxes, areas)):
            writer.writerow([i, x, y, ww, hh, f"{area:.1f}"])

    print(f"Found {len(boxes)} candidate flakes")
    print(f"Wrote: {overlay_path}")
    print(f"Wrote: {csv_path}")


if __name__ == "__main__":
    main()
