# Python Maths

A study collection of Python notebooks and small scripts for arithmetic, algebra,
trigonometry, calculus, probability, linear algebra, graphing, and data
visualization.

## Quick Start

Create a virtual environment from the project root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Launch the notebooks:

```bash
jupyter lab
```

Run one of the script lessons:

```bash
python "Data Visualization/die_visual.py"
python "Data Visualization/eq_world_map.py"
python "Data Visualization/rw_visual.py"
```

Some examples create HTML files in `Data Visualization/`, and some open a
Matplotlib window.

## Folder Map

- `Arithmetic/`, `Algebra 1/`, `Algebra 2/`, `Calculus/`, `Linear Algebra/`,
  `Number Theory/`, `Trigonometry/`: notebook lessons by topic.
- `Graphing and visualization/`, `Graphing and conic sections/`,
  `Art from trigonometry/`: graphing and creative math notebooks.
- `Probabilities and histogram/`: probability notebooks and sample data.
- `Data Visualization/`: runnable Python scripts, CSV/JSON data, and generated
  HTML charts.
- `Resources/`: original/reference notebook collections.

## Notes

The script files now use `main()` guards where practical, so they can be imported
for experiments without immediately running the full lesson.
