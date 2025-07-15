"""Integration tests for the CLI interface."""
import subprocess
import sys

import pytest


class TestCLIIntegration:
    """Integration tests for the CLI commands."""

    def test_cli_help(self):
        """Test that the main CLI help works."""
        result = subprocess.run(
            [sys.executable, "-m", "print_tools", "--help"],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0
        assert "Print Tools CLI" in result.stdout
        assert "concat" in result.stdout
        assert "imposition" in result.stdout
        assert "split" in result.stdout
        assert "templating" in result.stdout

    def test_concat_command_help(self):
        """Test concat command help."""
        result = subprocess.run(
            [sys.executable, "-m", "print_tools", "concat", "--help"],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0
        assert "Concatenate multiple PDF files" in result.stdout

    def test_imposition_command_help(self):
        """Test imposition command help."""
        result = subprocess.run(
            [sys.executable, "-m", "print_tools", "imposition", "--help"],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0
        assert "Perform various imposition layouts" in result.stdout

    def test_templating_command_help(self):
        """Test templating command help."""
        result = subprocess.run(
            [sys.executable, "-m", "print_tools", "templating", "--help"],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0
        assert "Generate PDFs from a PDF template" in result.stdout

    @pytest.mark.integration
    def test_concat_integration(self, multiple_pdf_files, temp_dir):
        """Test full concat workflow."""
        output_file = temp_dir / "concatenated.pdf"

        cmd = [
            sys.executable, "-m", "print_tools", "concat",
            *[str(f) for f in multiple_pdf_files],
            "-o", str(output_file)
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        assert result.returncode == 0
        assert output_file.exists()

    @pytest.mark.integration
    def test_templating_integration(self, sample_pdf_file, sample_text_blocks_file, temp_dir):
        """Test full templating workflow."""
        output_dir = temp_dir / "templating_output"

        cmd = [
            sys.executable, "-m", "print_tools", "templating", "overlay",
            str(sample_pdf_file),
            str(sample_text_blocks_file),
            str(output_dir)
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        assert result.returncode == 0
        assert output_dir.exists()
        output_files = list(output_dir.glob("block_*.pdf"))
        assert len(output_files) == 3
