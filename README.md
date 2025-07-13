# LaTeX OCR Batch Processor

A Python script that automatically processes PNG images containing mathematical formulas, converts them to LaTeX code using OCR, and compiles them into a single organized document. Built on top of [LaTeX-OCR](https://github.com/lukas-blecher/LaTeX-OCR) by Lukas Blecher.

## Features

- 🔍 **Batch Processing**: Automatically processes all PNG files in a directory
- 🧮 **Formula Recognition**: Uses [LaTeX-OCR](https://github.com/lukas-blecher/LaTeX-OCR) for accurate LaTeX formula recognition
- 📝 **Single Document Output**: Combines all formulas into one LaTeX file
- 🏷️ **Smart Tagging**: Numbers formulas using source filename as tags
- 📄 **PDF Compilation**: Automatically compiles to PDF if LaTeX is installed
- 🎨 **Professional Layout**: Creates well-formatted document with sections and metadata

## Requirements

### Python Dependencies
```bash
pip install pix2tex Pillow
```

### LaTeX Distribution (Optional, for PDF compilation)
- **Windows**: [MiKTeX](https://miktex.org/) or [TeX Live](https://www.tug.org/texlive/)
- **Linux**: `sudo apt install texlive-full`
- **macOS**: `brew install --cask mactex`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sergikapone/LaTeXPiX.git
cd LaTeXPiX
```

2. Install dependencies:
```bash
pipenv install pix2tex Pillow
```

## Usage

1. Place your PNG files containing mathematical formulas in the same directory as the script
2. Run the script:
```bash
python main.py
```

3. The script will:
   - Find all PNG files in the current directory
   - Process each image with OCR
   - Generate a single `all_formulas.tex` file
   - Compile to `all_formulas.pdf` (if LaTeX is available)

## Configuration

You can customize the script by modifying these variables:

```python
input_folder = "."  # Change to process different directory
output_name = "all_formulas"  # Change output filename
```

## Output Structure

The generated LaTeX document includes:

- Title page with metadata
- Organized sections for each formula
- Source filename references
- Tagged equations using filename as labels
- Professional formatting with proper spacing

### Example Output

```latex
\subsection{Formula 1: quadratic_formula}
Source: quadratic_formula.png
\begin{equation}
\tag{quadratic_formula}
x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}
\end{equation}
```

## Error Handling

The script includes robust error handling:

- Validates image file existence
- Handles OCR recognition failures gracefully
- Continues processing if individual images fail
- Provides detailed error messages and progress updates

## File Structure

```
├── main.py                  # Main script
├── Pipfile                  # Python dependencies
├── README.md                # This file
├── *.png                    # Your formula images
└── all_formulas.tex         # Generated output
```

## Dependencies

- **pix2tex**: Neural network-based LaTeX OCR (from [LaTeX-OCR](https://github.com/lukas-blecher/LaTeX-OCR))
- **Pillow**: Image processing library
- **pathlib**: Path manipulation utilities

## Limitations

- Only processes PNG format images
- Requires clear, well-lit formula images for best results
- OCR accuracy depends on image quality and formula complexity
- LaTeX compilation requires proper LaTeX distribution installation

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [LaTeX-OCR](https://github.com/lukas-blecher/LaTeX-OCR) by Lukas Blecher for the excellent OCR model
- LaTeX community for the typesetting system
- Contributors and testers

## Troubleshooting

### Common Issues

**"pdflatex not found"**
- Install LaTeX distribution
- Script will still generate .tex file without PDF compilation

**Poor OCR results**
- Ensure high-quality, clear images
- Check that formulas are properly cropped
- Verify adequate contrast and resolution

## Demo


<div align="center">
  <a href="https://youtu.be/IgwOWNt0RjE">
    <img src="https://img.youtube.com/vi/IgwOWNt0RjE/maxresdefault.jpg" alt="LaTeX OCR Demo" width="600"/>
  </a>
</div>

<div align="center">
  <a href="https://youtu.be/pF-Ot1G6Nzo">
    <img src="https://img.youtube.com/vi/pF-Ot1G6Nzo/maxresdefault.jpg" alt="LaTeX OCR Demo" width="600"/>
  </a>
</div>

<div align="center">
  <a href="https://youtu.be/6YsapjC-SGg">
    <img src="https://img.youtube.com/vi/6YsapjC-SGg/maxresdefault.jpg" alt="LaTeX OCR Demo" width="600"/>
  </a>
</div>

