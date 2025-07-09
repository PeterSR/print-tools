from pathlib import Path
from typing import Iterator


def parse_blocks(path: Path) -> Iterator[list[str]]:
    """Yield list[str] blocks separated by --- lines (ignoring blank lines)."""
    with path.open(encoding="utf-8") as fh:
        buf = []
        for line in fh:
            line = line.rstrip("\n")
            if line.strip() == "---":
                if buf:
                    yield buf
                    buf = []
            elif line.strip():
                buf.append(line)
        if buf:
            yield buf
