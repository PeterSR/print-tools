def saddle_order(pages: int, mirror_back=False) -> list[int]:
    """Two-up saddle-stitch imposition (left-to-right for each sheet side)."""
    if pages % 4:
        raise ValueError("Pages must be a multiple of 4.")
    out: list[int] = []
    left, right = 0, pages - 1
    while left < right:
        # front
        out += [right + 1, left + 1]
        # back (optionally mirrored)
        back_pair = [left + 2, right]
        if mirror_back:
            back_pair.reverse()
        out += [*back_pair]
        left += 2
        right -= 2
    return out


def quarter_fold_order(pages: int) -> list[int]:
    """Four-up quarter-fold imposition (TL,TR,BL,BR for each side)."""
    if pages % 8:
        raise ValueError("Quarter-fold needs pages multiple of 8.")
    out: list[int] = []
    sheets = pages // 8
    for k in range(sheets):
        # front
        out += [
            pages - 4 * k,          # TL
            2 * k + 1,              # TR
            2 * k + 2,              # BL
            pages - (4 * k + 1)     # BR
        ]
        # back
        out += [
            pages - (4 * k + 2),    # TL
            2 * k + 3,              # TR
            2 * k + 4,              # BL
            pages - (4 * k + 3)     # BR
        ]
    return out


def imposition_order(total_pages: int) -> list[int]:
    if total_pages % 4:
        raise ValueError("Page count must be a multiple of 4")
    order = []
    left, right = 0, total_pages - 1
    flip = True  # alternate front/back
    while left < right:
        if flip:  # front side
            order += [right + 1, left + 1]  # 1‑based numbers
        else:  # back side
            order += [left + 1, right + 1]
        flip = not flip
        left += 1
        right -= 1
    return order