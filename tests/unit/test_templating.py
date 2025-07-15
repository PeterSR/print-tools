"""Unit tests for print_tools.core.templating module."""
from pypdf import PdfReader

from print_tools.core.templating import create_labeled_pdfs


class TestCreateLabeledPdfs:
    """Test create_labeled_pdfs function."""

    def test_create_labeled_pdfs_basic(self, sample_pdf_file, sample_text_blocks_file, temp_dir):
        """Test basic PDF labeling functionality."""
        output_dir = temp_dir / "output"

        create_labeled_pdfs(
            template_path=sample_pdf_file,
            blocks_path=sample_text_blocks_file,
            output_dir=output_dir,
        )

        assert output_dir.exists()
        output_files = list(output_dir.glob("block_*.pdf"))
        assert len(output_files) == 3  # Three blocks in the sample file

        # Verify all output files exist and are valid PDFs
        for pdf_file in output_files:
            assert pdf_file.exists()
            reader = PdfReader(str(pdf_file))
            assert len(reader.pages) == 1

    def test_create_labeled_pdfs_custom_params(self, sample_pdf_file, sample_text_blocks_file, temp_dir):
        """Test PDF labeling with custom parameters."""
        output_dir = temp_dir / "custom_output"

        create_labeled_pdfs(
            template_path=sample_pdf_file,
            blocks_path=sample_text_blocks_file,
            output_dir=output_dir,
            font_name="Times-Roman",
            font_size=24,
            line_spacing=8,
            text_colour="#FF0000",
        )

        assert output_dir.exists()
        output_files = list(output_dir.glob("block_*.pdf"))
        assert len(output_files) == 3

    def test_create_labeled_pdfs_empty_blocks(self, sample_pdf_file, temp_dir):
        """Test with empty blocks file."""
        blocks_file = temp_dir / "empty_blocks.txt"
        blocks_file.write_text("")
        output_dir = temp_dir / "empty_output"

        create_labeled_pdfs(
            template_path=sample_pdf_file,
            blocks_path=blocks_file,
            output_dir=output_dir,
        )

        # Should create output directory but no PDF files
        assert output_dir.exists()
        output_files = list(output_dir.glob("block_*.pdf"))
        assert len(output_files) == 0

    def test_create_labeled_pdfs_single_block(self, sample_pdf_file, temp_dir):
        """Test with single block."""
        blocks_file = temp_dir / "single_block.txt"
        blocks_file.write_text("Single line block")
        output_dir = temp_dir / "single_output"

        create_labeled_pdfs(
            template_path=sample_pdf_file,
            blocks_path=blocks_file,
            output_dir=output_dir,
        )

        assert output_dir.exists()
        output_files = list(output_dir.glob("block_*.pdf"))
        assert len(output_files) == 1
        assert output_files[0].name == "block_001.pdf"
