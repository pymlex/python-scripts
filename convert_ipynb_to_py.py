"""
This script converts Jupyter Notebook (.ipynb) files into plain Python (.py) files
by collecting only code cells and joining them into a single text file.

It is useful when you need a source-only version of a notebook without markdown,
outputs, or other notebook-specific structure.
"""

import pathlib

import nbformat


def convert_notebook(path):
    with path.open("r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    cells = []
    for cell in nb.cells:
        if cell.cell_type == "code":
            cells.append(cell.source)

    content = "\n\n".join(cells)
    out = path.with_suffix(".py")
    out.write_text(content, encoding="utf-8")


def main(dir_path="."):
    p = pathlib.Path(dir_path)
    for path in p.glob("*.ipynb"):
        convert_notebook(path)


if __name__ == "__main__":
    main(".")