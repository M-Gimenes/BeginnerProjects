# Beginner Projects

A collection of small projects built during my early steps into programming. Each one targets a specific concept — from sorting algorithms and statistical analysis in Python to a functional web calculator in JavaScript.

---

## Projects

### Calculator — `Calculator/`
A browser-based calculator built with vanilla HTML, CSS, and JavaScript.

**Features:**
- Four arithmetic operations: addition, subtraction, multiplication, and division
- Support for chained operations (e.g. `3 + 5 * 2`)
- Sign toggle (`+/-`), step-back clear (`C`), and full reset (`AC`)
- Decimal point input

**Stack:** HTML · CSS · JavaScript

---

### Sorting Algorithm — `SortAlg.py`
An interactive CLI program that demonstrates a **selection sort** implementation in Python.

**Features:**
- Manually add individual numbers or generate random datasets (10 to 10,000 entries)
- Sort in ascending or descending order
- Configurable random draw range (lower and upper bounds)

**Stack:** Python

---

### Statistical Text Analyzer — `TxtOutput/Txt.py`
Reads datasets from plain-text files and produces a formatted statistical report.

**Computed metrics:**
- Mean, variance, and standard deviation
- Mode (with unimodal / bimodal / multimodal classification)
- Frequency histogram bucketed in ranges of 10

Output is written to `texts/histogram.txt` in a clean, aligned format.

**Stack:** Python

---

## What I Learned

| Concept | Project |
|---|---|
| DOM manipulation and event handling | Calculator |
| Sorting algorithm design from scratch | SortAlg |
| File I/O and descriptive statistics | TxtOutput |
| Python control flow and data structures | SortAlg · TxtOutput |

---

## Running the Projects

**Calculator** — open `Calculator/index.html` in any browser.

**SortAlg**
```bash
python SortAlg.py
```

**TxtOutput** — run from inside the `TxtOutput/` directory so the relative file paths resolve correctly:
```bash
cd TxtOutput
python Txt.py
```
Output will be saved to `TxtOutput/texts/histogram.txt`.
