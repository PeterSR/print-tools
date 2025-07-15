# Examples

This directory contains example scripts demonstrating various Print Tools capabilities.

## Available Examples

### business_cards.py
Creates a sheet of business cards from a single card design using grid imposition.

**Usage:**
```bash
# Place your business card PDF as 'business-card.pdf'
python business_cards.py
```

### booklet_workflow.py
Complete workflow for creating a professional booklet from individual pages.

**Usage:**
```bash
# Create a 'pages' directory with your PDF pages
mkdir pages
# Add your PDF files to the pages directory
python booklet_workflow.py
```

### name_badges.py
Generates name badges from a template and a list of names.

**Usage:**
```bash
# Create badge-template.pdf and names.txt
python name_badges.py
```

## Running Examples

1. **Install Print Tools** (if not already installed):
   ```bash
   pip install print-tools
   ```

2. **Navigate to examples directory**:
   ```bash
   cd examples
   ```

3. **Prepare your input files** as described in each example

4. **Run the example script**:
   ```bash
   python script_name.py
   ```

## Creating Your Own Examples

Feel free to create your own example scripts! Here's a basic template:

```python
"""
Example: Your Use Case

Description of what this example demonstrates.
"""

import subprocess
import sys
from pathlib import Path


def your_function():
    """Your function description."""

    # Input validation
    input_file = Path("input.pdf")
    if not input_file.exists():
        print("Error: input.pdf not found!")
        return False

    # Build command
    cmd = [
        sys.executable, "-m", "print_tools",
        "command", "subcommand",
        str(input_file),
        "-o", "output.pdf"
    ]

    # Execute
    try:
        subprocess.run(cmd, check=True)
        print("✅ Success!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        return False


if __name__ == "__main__":
    your_function()
```

## Tips

- Always validate input files exist before processing
- Use descriptive output filenames
- Include progress messages for user feedback
- Handle errors gracefully with helpful messages
- Clean up temporary files when done
