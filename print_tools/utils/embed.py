from pypdf import Transformation
from pypdf._page import PageObject


def create_transformation(
    dx: float = 0.0,
    dy: float = 0.0,
    scale: float = 1.0,
    rotation: float = 0.0,
    mirror_horizontal: bool = False,
    mirror_vertical: bool = False,
    compensate_mirror_horizontal: float = 0.0,
    compensate_mirror_vertical: float = 0.0,
):
    # Build transformation: mirror (via scale), rotate, then translate.
    sx = -1.0 if mirror_horizontal else 1.0
    sy = -1.0 if mirror_vertical else 1.0

    if mirror_horizontal:
        # compensate for negative x‑scale
        dx += compensate_mirror_horizontal

    if mirror_vertical:
        # compensate for negative y‑scale
        dy += compensate_mirror_vertical

    op = (
        Transformation()  # identity
        .scale(sx=sx * scale, sy=sy * scale)  # apply scale and mirror
        .rotate(rotation)  # clockwise degrees
        .translate(tx=dx, ty=dy)  # final placement
    )

    return op


def embed_page(
    base: PageObject,
    overlay: PageObject,
    *,
    position: tuple[float, float] = (0.0, 0.0),
    scale: float = 1.0,
    rotation: float = 0.0,
    mirror_horizontal: bool = False,
    mirror_vertical: bool = False,
    transformation: Transformation | None = None,
) -> None:
    """Draw `overlay` on top of `base` in-place."""
    w = overlay.mediabox.width
    h = overlay.mediabox.height

    if transformation:
        # Use the provided transformation directly
        op = transformation
    else:
        op = create_transformation(
            dx=position[0],
            dy=position[1],
            scale=scale,
            rotation=rotation,
            mirror_horizontal=mirror_horizontal,
            mirror_vertical=mirror_vertical,
            compensate_mirror_horizontal=w if mirror_horizontal else 0.0,
            compensate_mirror_vertical=h if mirror_vertical else 0.0,
        )

    # Overlay with one call; overlay page itself is left untouched.
    base.merge_transformed_page(overlay, op)
