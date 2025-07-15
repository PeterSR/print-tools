"""Test configuration and fixtures."""
import io
import tempfile
from collections.abc import Generator
from pathlib import Path

import pytest
from reportlab.pdfgen import canvas


@pytest.fixture
def temp_dir() -> Generator[Path]:
    """Create a temporary directory for tests."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        yield Path(tmp_dir)


@pytest.fixture
def sample_pdf_content() -> bytes:
    """Create a simple PDF content for testing."""
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=(200, 300))
    c.drawString(50, 250, "Test PDF Content")
    c.showPage()
    c.save()
    return buffer.getvalue()


@pytest.fixture
def sample_pdf_file(temp_dir: Path, sample_pdf_content: bytes) -> Path:
    """Create a sample PDF file for testing."""
    pdf_file = temp_dir / "sample.pdf"
    pdf_file.write_bytes(sample_pdf_content)
    return pdf_file


@pytest.fixture
def multiple_pdf_files(temp_dir: Path) -> list[Path]:
    """Create multiple sample PDF files for testing."""
    pdf_files = []
    for i in range(3):
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=(200, 300))
        c.drawString(50, 250, f"Test PDF Content {i + 1}")
        c.showPage()
        c.save()

        pdf_file = temp_dir / f"sample_{i + 1}.pdf"
        pdf_file.write_bytes(buffer.getvalue())
        pdf_files.append(pdf_file)

    return pdf_files


@pytest.fixture
def sample_text_blocks_file(temp_dir: Path) -> Path:
    """Create a sample text blocks file for templating tests."""
    blocks_file = temp_dir / "blocks.txt"
    content = """First Block
Line 1
Line 2
---
Second Block
Another line
---
Third Block
Final content"""
    blocks_file.write_text(content)
    return blocks_file
