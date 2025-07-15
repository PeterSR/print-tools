"""Unit tests for print_tools.utils module."""
import pytest
from pypdf._page import PageObject

from print_tools.utils.utils import (
    gather_files,
    gather_pdf_pages,
    hex_to_colour,
    register_font,
)


class TestHexToColour:
    """Test hex_to_colour function."""

    def test_valid_hex_codes(self):
        """Test valid hex color codes."""
        # Test with hash
        color = hex_to_colour("#FF0000")
        assert color.red == 1.0
        assert color.green == 0.0
        assert color.blue == 0.0

        # Test without hash
        color = hex_to_colour("00FF00")
        assert color.red == 0.0
        assert color.green == 1.0
        assert color.blue == 0.0

        # Test blue
        color = hex_to_colour("#0000FF")
        assert color.red == 0.0
        assert color.green == 0.0
        assert color.blue == 1.0

    def test_mixed_case(self):
        """Test hex codes with mixed case."""
        color = hex_to_colour("#FfAaBb")
        assert abs(color.red - 1.0) < 0.001
        assert abs(color.green - 0.667) < 0.001
        assert abs(color.blue - 0.733) < 0.001


class TestRegisterFont:
    """Test register_font function."""

    def test_builtin_font(self):
        """Test with built-in font names."""
        result = register_font("Helvetica")
        assert result == "Helvetica"

        result = register_font("Times-Roman")
        assert result == "Times-Roman"

    def test_ttf_file_path(self, temp_dir):
        """Test with TTF file path."""
        # Create a dummy TTF file
        font_file = temp_dir / "test_font.ttf"
        font_file.write_bytes(b"dummy ttf content")

        result = register_font(str(font_file))
        assert result == "test_font"

    def test_otf_file_path(self, temp_dir):
        """Test with OTF file path."""
        # Create a dummy OTF file
        font_file = temp_dir / "test_font.otf"
        font_file.write_bytes(b"dummy otf content")

        result = register_font(str(font_file))
        assert result == "test_font"


class TestGatherFiles:
    """Test gather_files function."""

    def test_single_pdf_file(self, sample_pdf_file):
        """Test with a single PDF file."""
        result = gather_files([sample_pdf_file])
        assert result == [sample_pdf_file]

    def test_multiple_pdf_files(self, multiple_pdf_files):
        """Test with multiple PDF files."""
        result = gather_files(multiple_pdf_files)
        assert result == multiple_pdf_files

    def test_directory_with_pdfs(self, temp_dir, multiple_pdf_files):
        """Test with directory containing PDF files."""
        result = gather_files([temp_dir])
        # Should find all PDF files in the directory
        assert len(result) == 3
        assert all(f.suffix == ".pdf" for f in result)

    def test_non_pdf_file_raises_error(self, temp_dir):
        """Test that non-PDF files raise ValueError."""
        txt_file = temp_dir / "test.txt"
        txt_file.write_text("not a pdf")

        with pytest.raises(ValueError, match="is not a .pdf file"):
            gather_files([txt_file])

    def test_custom_extension(self, temp_dir):
        """Test with custom file extension."""
        txt_file = temp_dir / "test.txt"
        txt_file.write_text("text content")

        result = gather_files([txt_file], ext=".txt")
        assert result == [txt_file]


class TestGatherPdfPages:
    """Test gather_pdf_pages function."""

    def test_single_pdf_file(self, sample_pdf_file):
        """Test gathering pages from a single PDF file."""
        result = gather_pdf_pages([sample_pdf_file])
        assert len(result) == 1
        assert isinstance(result[0], PageObject)

    def test_multiple_pdf_files(self, multiple_pdf_files):
        """Test gathering pages from multiple PDF files."""
        result = gather_pdf_pages(multiple_pdf_files)
        assert len(result) == 3
        assert all(isinstance(page, PageObject) for page in result)

    def test_nonexistent_file_raises_error(self, temp_dir):
        """Test that nonexistent files raise FileNotFoundError."""
        nonexistent = temp_dir / "nonexistent.pdf"

        with pytest.raises(FileNotFoundError):
            gather_pdf_pages([nonexistent])

    def test_non_pdf_file_raises_error(self, temp_dir):
        """Test that non-PDF files raise ValueError."""
        txt_file = temp_dir / "test.txt"
        txt_file.write_text("not a pdf")

        with pytest.raises(ValueError, match="is not a PDF file"):
            gather_pdf_pages([txt_file])
