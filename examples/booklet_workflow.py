"""
Example: Booklet Creation Workflow

This example demonstrates creating a professional booklet from individual pages,
including proper page ordering for saddle-stitching.
"""

import subprocess
import sys
from pathlib import Path


def create_booklet():
    """Create a booklet from individual page files."""

    # Input and output paths
    pages_dir = Path("pages")
    output_booklet = Path("booklet.pdf")
    temp_combined = Path("temp_combined.pdf")

    # Check if pages directory exists
    if not pages_dir.exists():
        print(f"Error: {pages_dir} directory not found!")
        print("Please create a 'pages' directory with PDF files.")
        return False

    # Step 1: Concatenate all individual pages
    print("Step 1: Combining individual pages...")
    concat_cmd = [
        sys.executable, "-m", "print_tools", "concat",
        str(pages_dir),
        "-o", str(temp_combined)
    ]

    try:
        subprocess.run(concat_cmd, check=True, capture_output=True, text=True)
        print(f"✅ Pages combined into {temp_combined}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error combining pages: {e}")
        return False

    # Step 2: Create booklet layout
    print("Step 2: Creating booklet layout...")
    booklet_cmd = [
        sys.executable, "-m", "print_tools", "imposition", "booklet",
        str(temp_combined),
        "-o", str(output_booklet),
        "--paper", "A4",
        "--padding", "10"
    ]

    try:
        subprocess.run(booklet_cmd, check=True, capture_output=True, text=True)
        print(f"✅ Booklet created: {output_booklet}")

        # Clean up temporary file
        temp_combined.unlink()
        print("🧹 Temporary files cleaned up")

        print("\n📖 Booklet Creation Complete!")
        print(f"Your booklet is ready: {output_booklet}")
        print("\n📋 Printing Instructions:")
        print("1. Print double-sided, flip on short edge")
        print("2. Fold in half along the center")
        print("3. Staple along the fold (saddle-stitch)")

        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ Error creating booklet: {e}")
        # Clean up on error
        if temp_combined.exists():
            temp_combined.unlink()
        return False


if __name__ == "__main__":
    create_booklet()
