"""Unit tests for print_tools.utils.parsing module."""
from print_tools.utils.parsing import parse_blocks


class TestParseBlocks:
    """Test parse_blocks function."""

    def test_parse_multiple_blocks(self, temp_dir):
        """Test parsing multiple blocks separated by ---."""
        blocks_file = temp_dir / "test_blocks.txt"
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

        blocks = list(parse_blocks(blocks_file))

        assert len(blocks) == 3
        assert blocks[0] == ["First Block", "Line 1", "Line 2"]
        assert blocks[1] == ["Second Block", "Another line"]
        assert blocks[2] == ["Third Block", "Final content"]

    def test_parse_single_block(self, temp_dir):
        """Test parsing a single block without separators."""
        blocks_file = temp_dir / "single_block.txt"
        content = """Single Block
Line 1
Line 2"""
        blocks_file.write_text(content)

        blocks = list(parse_blocks(blocks_file))

        assert len(blocks) == 1
        assert blocks[0] == ["Single Block", "Line 1", "Line 2"]

    def test_parse_empty_file(self, temp_dir):
        """Test parsing an empty file."""
        blocks_file = temp_dir / "empty.txt"
        blocks_file.write_text("")

        blocks = list(parse_blocks(blocks_file))

        assert len(blocks) == 0

    def test_parse_with_blank_lines(self, temp_dir):
        """Test parsing blocks with blank lines (should be ignored)."""
        blocks_file = temp_dir / "blank_lines.txt"
        content = """

First Block


Line 1

---


Second Block

Another line


---

Third Block

"""
        blocks_file.write_text(content)

        blocks = list(parse_blocks(blocks_file))

        assert len(blocks) == 3
        assert blocks[0] == ["First Block", "Line 1"]
        assert blocks[1] == ["Second Block", "Another line"]
        assert blocks[2] == ["Third Block"]

    def test_parse_only_separators(self, temp_dir):
        """Test parsing file with only separators."""
        blocks_file = temp_dir / "only_seps.txt"
        content = """---
---
---"""
        blocks_file.write_text(content)

        blocks = list(parse_blocks(blocks_file))

        assert len(blocks) == 0

    def test_parse_trailing_separator(self, temp_dir):
        """Test parsing blocks with trailing separator."""
        blocks_file = temp_dir / "trailing_sep.txt"
        content = """First Block
Line 1
---
Second Block
Line 2
---"""
        blocks_file.write_text(content)

        blocks = list(parse_blocks(blocks_file))

        assert len(blocks) == 2
        assert blocks[0] == ["First Block", "Line 1"]
        assert blocks[1] == ["Second Block", "Line 2"]
