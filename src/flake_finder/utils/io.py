from __future__ import annotations

from pathlib import Path
import cv2


def mkdir_p(path: str | Path) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def read_image(path: str | Path):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Image not found: {p}")
    img = cv2.imread(str(p), cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError(
            f"OpenCV could not read the image at: {p}. "
            "Check the path and confirm it’s a valid image file."
        )
    return img
