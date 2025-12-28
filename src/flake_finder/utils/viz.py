from __future__ import annotations

from typing import Iterable, Sequence, Tuple
import cv2
import numpy as np


def draw_boxes(
    image_bgr: np.ndarray,
    boxes_xywh: Sequence[Tuple[int, int, int, int]],
    labels: Iterable[str] | None = None,
    color=(0, 255, 0),
    thickness: int = 2,
) -> np.ndarray:
    overlay = image_bgr.copy()
    if labels is None:
        labels = ["" for _ in boxes_xywh]

    for (x, y, w, h), label in zip(boxes_xywh, labels):
        cv2.rectangle(overlay, (x, y), (x + w, y + h), color, thickness)
        if label:
            cv2.putText(
                overlay,
                str(label),
                (x, max(0, y - 6)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2,
                cv2.LINE_AA,
            )
    return overlay
