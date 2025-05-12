# AtCoder Framework

A lightweight and colorized local test runner for AtCoder problem solving using Python. Includes features for sample case setup, auto-run testing, diff highlighting, and clipboard auto-copy on full success.

---

## Framework Included

### `runner.py`

* Runs your AtCoder solution against `input{i}.txt` and `answer{i}.txt`
* Displays colorized result: `[AC]`, `[WA]`, `[TLE]`, `[RE]`, `[NI]`, `[NA]`, `[FN]`
* Shows diffs if output is wrong
* Automatically copies your code to clipboard on full AC (via `pyperclip`)
* Uses `colorama` for terminal color feedback

### `sample.py`

* Assists in generating `input1.txt`, `answer1.txt`, ... in appropriate folders
* Lets you enter multi-line samples from contests

---

## Directory Structure

```
at-coder/ abcXXX
├── runner.py
├── sample.py
├── a/
│   ├── input1.txt
│   ├── answer1.txt
│   ├── input2.txt
│   ├── answer2.txt
├── b/
│   └── ...         # Next problem
├── a.py
├── b.py
└── ... 
```

Each folder (`a/`, `b/`, etc.) represents a problem, and contains:

* `input{i}.txt` for input cases
* `answer{i}.txt` for expected output
* `{problem}.py` as your code

---

## Usage

### Generate sample input/output

```bash
python sample.py
```

> Prompts you to enter Input 1–3 and Answer 1–3, stores them in e.g. `a/`

### Run a problem interactively

```bash
❯ python runner.py
Problem : c
#sample1[AC] -- 1.228 sec
#sample2[AC] -- 0.185 sec
#sample3[AC] -- 0.195 sec

[[ALL ACCEPTED]]
20XX-XX-XX XX:XX:XX [Copied!]
```

```bash
❯ python runner.py
Problem : e
#sample1[WA] -- 0.192 sec
[[Input]]
1 1 1 1
[[Output]]
10
[[Expected]]
5

#sample2[WA] -- 0.187 sec
[[Input]]
1 2 4 8
[[Output]]
5512
[[Expected]]
2211

#sample3[WA] -- 0.488 sec
[[Input]]
834150 21994 467364 994225
[[Output]]
239672234
[[Expected]]
947921688
```

> Prompts for problem name (e.g. `a`) and runs `a/a.py` against `a/input{i}.txt`

---

## Requirements

* Python 3.x
* [colorama](https://pypi.org/project/colorama/)
* [pyperclip](https://pypi.org/project/pyperclip/)

Install dependencies:

```bash
pip install colorama pyperclip
```

---

## License

MIT License

---

Created by [@kamekingdom](https://github.com/kamekingdom)
