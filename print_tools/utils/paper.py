from typing import Literal, TypeAlias
from reportlab.lib.pagesizes import A3, A4, A5, LETTER

PaperRef: TypeAlias = Literal["A3", "A4", "A5", "LETTER"] | tuple[float, float]


def get_paper_size(paper: PaperRef) -> tuple[float, float]:
    """
    Get the dimensions of the specified paper size.

    Args:
        paper: Paper size as a string or a tuple of (width, height).

    Returns:
        A tuple containing the width and height in points.
    """
    if isinstance(paper, tuple):
        return paper
    elif paper == "A3":
        return A3
    elif paper == "A4":
        return A4
    elif paper == "A5":
        return A5
    elif paper == "LETTER":
        return LETTER
    else:
        raise ValueError(f"Unknown paper size: {paper}")


__all__ = [
    "get_paper_size",
    "PaperRef",
    "A3",
    "A4",
    "A5",
    "LETTER",
]
