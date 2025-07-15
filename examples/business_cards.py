"""
Example: Business Card Sheet Generation

This example demonstrates how to create a sheet of business cards
from a single business card design using the grid imposition.
"""

import subprocess
import sys
from pathlib import Path


def create_business_card_sheet():
    """Create a sheet of business cards from a single card design."""

    # Input and output paths
    input_card = Path("business-card.pdf")  # Single business card design
    output_sheet = Path("business-card-sheet.pdf")

    # Check if input file exists
    if not input_card.exists():
        print(f"Error: {input_card} not found!")
        print("Please create a business card PDF file first.")
        return False

    # Command to create business card sheet
    cmd = [
        sys.executable, "-m", "print_tools", "imposition", "grid",
        str(input_card),
        "-o", str(output_sheet),
        "--paper", "A4",
        "--padding", "20",  # 20pt padding around edges
        "--gap", "5"        # 5pt gap between cards
    ]

    print("Creating business card sheet...")
    print(f"Input: {input_card}")
    print(f"Output: {output_sheet}")

    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✅ Business card sheet created successfully!")
        print(f"📄 Output saved to: {output_sheet}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error creating business card sheet: {e}")
        print(f"Command output: {e.stdout}")
        print(f"Command error: {e.stderr}")
        return False


if __name__ == "__main__":
    create_business_card_sheet()
