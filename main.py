from PIL import Image
from pix2tex.cli import LatexOCR
import os
import subprocess
import sys
import glob
from pathlib import Path

def process_all_png_images(input_folder=".", output_name="formulas"):
    """
    Processes all PNG files in a folder and creates one .tex file with numbered formulas
    """

    # Find all PNG files
    png_files = glob.glob(os.path.join(input_folder, "*.png"))

    if not png_files:
        print("No PNG files found in the folder!")
        return False

    print(f"Found {len(png_files)} PNG files")

    try:
        # Initialize model once
        print("Loading OCR model...")
        model = LatexOCR()

        # Collect all formulas
        formulas = []

        for png_file in sorted(png_files):
            print(f"Processing: {png_file}")

            try:
                # Load image
                img = Image.open(png_file)

                # Recognize LaTeX
                latex_code = model(img)

                # Get filename without extension for tag
                file_stem = Path(png_file).stem

                # Add to list
                formulas.append({
                    'filename': png_file,
                    'stem': file_stem,
                    'latex': latex_code
                })

                print(f"  Recognized: {latex_code[:50]}...")

            except Exception as e:
                print(f"  Error processing {png_file}: {e}")
                continue

        if not formulas:
            print("No formulas were recognized successfully!")
            return False

        # Create LaTeX document
        latex_document = create_latex_document(formulas)

        # Save to .tex file
        tex_filename = f"{output_name}.tex"
        with open(tex_filename, 'w', encoding='utf-8') as f:
            f.write(latex_document)
        print(f"LaTeX code saved to {tex_filename}")

        # Compile to PDF
        return compile_to_pdf(tex_filename, output_name)

    except Exception as e:
        print(f"General error: {e}")
        return False

def create_latex_document(formulas):
    """
    Creates LaTeX document with numbered formulas
    """

    # Document header
    latex_document = """\\documentclass{article}
\\usepackage{amsmath}
\\usepackage{amssymb}
\\usepackage{amsfonts}
\\usepackage[utf8]{inputenc}
\\usepackage[russian]{babel}
\\usepackage{geometry}
\\geometry{a4paper, margin=2cm}

\\title{Recognized Formulas}
\\author{LaTeX OCR}
\\date{\\today}

\\begin{document}

\\maketitle

\\section{Formulas}

"""

    # Add each formula
    for i, formula in enumerate(formulas, 1):
        latex_document += f"\\subsection{{Formula {i}: {formula['stem']}}}\n\n"
        latex_document += f"Source: \\texttt{{{formula['filename']}}}\n\n"
        latex_document += f"\\begin{{equation}}\n"
        latex_document += f"\\tag{{{formula['stem']}}}\n"
        latex_document += f"{formula['latex']}\n"
        latex_document += f"\\end{{equation}}\n\n"
        latex_document += "\\hrule\n\n"

    latex_document += "\\end{document}"

    return latex_document

def compile_to_pdf(tex_filename, output_name):
    """
    Compiles .tex file to PDF
    """

    # Check for pdflatex availability
    try:
        subprocess.run(['pdflatex', '--version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Warning: pdflatex not found. Only .tex file created")
        return True

    print("Compiling to PDF...")

    # Compile twice for correct references
    for i in range(2):
        result = subprocess.run([
            'pdflatex',
            '-interaction=nonstopmode',
            tex_filename
        ], capture_output=True, text=True)

        if result.returncode != 0:
            print("Compilation error:")
            print(result.stdout)
            print(result.stderr)
            return False

    print(f"Successfully compiled to {output_name}.pdf")

    # Clean temporary files
    temp_extensions = ['.aux', '.log', '.out', '.toc']
    for ext in temp_extensions:
        temp_file = f"{output_name}{ext}"
        if os.path.exists(temp_file):
            os.remove(temp_file)

    return True

def create_simple_combined_tex(formulas, output_name):
    """
    Creates simple .tex file with formulas without compilation
    """

    latex_content = """\\documentclass{article}
\\usepackage{amsmath}
\\usepackage{amssymb}

\\begin{document}

"""

    for formula in formulas:
        latex_content += f"% From file: {formula['filename']}\n"
        latex_content += f"\\begin{{equation}}\n"
        latex_content += f"\\tag{{{formula['stem']}}}\n"
        latex_content += f"{formula['latex']}\n"
        latex_content += f"\\end{{equation}}\n\n"

    latex_content += "\\end{document}"

    with open(f"{output_name}.tex", 'w', encoding='utf-8') as f:
        f.write(latex_content)

    print(f"Simple LaTeX file saved as {output_name}.tex")

# Main function
if __name__ == "__main__":
    input_folder = "./files"  # Current folder, can be changed
    output_name = "all_formulas"  # Output filename

    print("=== LaTeX OCR for all PNG files ===")
    print(f"Searching for PNG files in: {os.path.abspath(input_folder)}")

    success = process_all_png_images(input_folder, output_name)

    if success:
        print("\n=== Done! ===")
        print(f"Results:")
        print(f"- {output_name}.tex")
        if os.path.exists(f"{output_name}.pdf"):
            print(f"- {output_name}.pdf")
    else:
        print("\n=== Process completed with errors ===")

    print(f"\nProcessed files in folder: {input_folder}")
    print("To change folder, edit the input_folder variable")
