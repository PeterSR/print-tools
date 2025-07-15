"""Unit tests for print_tools.core.concat module."""
import pytest
from pypdf import PdfReader

from print_tools.core.concat import concat_pdfs


class TestConcatPdfs:
    """Test concat_pdfs function."""

    def test_concat_multiple_files(self, multiple_pdf_files, temp_dir):
        """Test concatenating multiple PDF files."""
        output_file = temp_dir / "concatenated.pdf"

        result = concat_pdfs(multiple_pdf_files, output_file)

        assert result == output_file
        assert output_file.exists()

        # Verify the concatenated file has the correct number of pages
        reader = PdfReader(str(output_file))
        assert len(reader.pages) == 3

    def test_concat_single_file(self, sample_pdf_file, temp_dir):
        """Test concatenating a single PDF file."""
        output_file = temp_dir / "single.pdf"

        result = concat_pdfs([sample_pdf_file], output_file)

        assert result == output_file
        assert output_file.exists()

        reader = PdfReader(str(output_file))
        assert len(reader.pages) == 1

    def test_empty_input_raises_error(self, temp_dir):
        """Test that empty input raises ValueError."""
        output_file = temp_dir / "output.pdf"

        with pytest.raises(ValueError, match="input_files must contain at least one path"):
            concat_pdfs([], output_file)

    def test_nonexistent_file_raises_error(self, temp_dir):
        """Test that nonexistent files raise FileNotFoundError."""
        nonexistent = temp_dir / "nonexistent.pdf"
        output_file = temp_dir / "output.pdf"

        with pytest.raises(FileNotFoundError):
            concat_pdfs([nonexistent], output_file)

    def test_concat_directory_with_pdfs(self, temp_dir, multiple_pdf_files):
        """Test concatenating PDFs from a directory."""
        output_file = temp_dir / "concatenated_dir.pdf"

        result = concat_pdfs([temp_dir], output_file)

        assert result == output_file
        assert output_file.exists()

        reader = PdfReader(str(output_file))
        assert len(reader.pages) == 3
