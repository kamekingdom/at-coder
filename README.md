# 🧮 AtCoder Python Framework

A lightweight and colorized local test runner for AtCoder problem solving using Python. Includes features for sample case setup, auto-run testing, diff highlighting, and clipboard auto-copy on full success.

---

## 🧰 Tools Included

### `runner.py`
- Runs your AtCoder solution against `input{i}.txt` and `answer{i}.txt`
- Displays colorized result: `[AC]`, `[WA]`, `[TLE]`, `[RE]`, `[NI]`, `[NA]`, `[FN]`
- Shows diffs if output is wrong
- Automatically copies your code to clipboard on full AC (via `pyperclip`)
- Uses `colorama` for terminal color feedback

### `sample.py`
- Assists in generating `input1.txt`, `answer1.txt`, ... in appropriate folders
- Lets you enter multi-line samples from contests

---

## 🗂 Directory Structure

```
at-coder/
├── runner.py
├── sample.py
├── a.py
├── b.py
...
├── a/
│   ├── input1.txt
│   ├── answer1.txt
│   ├── input2.txt
│   ├── answer2.txt
│   └── ...         # Your solution script
├── b/
│   └── ...         # Next problem
└── ...
```

Each folder (`a/`, `b/`, etc.) represents a problem, and contains:
- `input{i}.txt` for input cases
- `answer{i}.txt` for expected output
- `{problem}.py` as your code

---

## 🚀 Usage

### Generate sample input/output
```bash
python sample.py
```
> Prompts you to enter Input 1–3 and Answer 1–3, stores them in e.g. `a/`

### Run a problem interactively
```bash
python runner.py
```
> Prompts for problem name (e.g. `a`) and runs `a/a.py` against `a/input{i}.txt`

---

## 🧠 Features

- 🟥 **WA Diff Highlighting**
- 🟩 **Green [AC]** if all correct
- 📋 **Auto Copy to Clipboard** on full AC
- 📁 **Sample management** with `sample.py`
- 🔍 **Color-coded debug printouts**

---

## 🧩 Requirements

- Python 3.x
- [colorama](https://pypi.org/project/colorama/)
- [pyperclip](https://pypi.org/project/pyperclip/)

Install dependencies:
```bash
pip install colorama pyperclip
```

---

## 📄 License

MIT License

---

Created by [@kamekingdom](https://github.com/kamekingdom)
