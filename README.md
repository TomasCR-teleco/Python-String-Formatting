# Python String Formatting

> A structured guide to string formatting in Python, comparing f-strings and str.format() across their syntax, format specifiers, and practical use cases.

> 🎓 Part of my self-directed learning alongside the Telecommunications Technology Engineering degree at Universitat Politècnica de València (UPV).

---

## 📌 Overview

This repository documents the two main approaches to string formatting in Python. Each directory isolates a specific layer of the topic — syntax, format specifiers, and applied examples — so the progression from basic concept to practical usage is explicit and easy to follow.

---

## 🛠️ Modules Summary

| Module | Core Focus | Concepts Implemented |
| :--- | :--- | :--- |
| 🔤 **[F-Strings](./01-f-strings)** | Syntax & Definition | Literal string interpolation and embedded expressions. |
| 🧩 **[str.format()](./02-str-format)** | Syntax & Definition | Positional and named placeholders via the `.format()` method. |
| 🎛️ **[Format Specifiers](./03-format-specifiers)** | Formatting Mini-Language | Alignment, padding, precision, percentages, scientific notation, hex, dates. |
| 🚀 **[Examples](./04-examples)** | Applied Practice | Practical scenarios combining both methods with format specifiers. |

---

## 🧠 Key Learnings & Architecture Evolution

1. **Separation of Concerns:** Splitting "what a method is" (`01-f-strings`, `02-str-format`) from "what it can do" (`03-format-specifiers`), so each layer can be learned independently.
2. **Format Specifier Mini-Language:** Understanding the shared `{:spec}` grammar that both f-strings and `.format()` rely on internally.
3. **Method Equivalence:** Recognizing that f-strings and `.format()` solve the same formatting problems, differing mainly in syntax and evaluation context.
4. **Applied Practice:** Reinforcing theory with side-by-side examples (`con_fstring.py` / `con_format.py`) for each formatting case.

---

## 🚀 How to Run

### Prerequisites
* Python 3.6+ installed (f-strings require 3.6; the `=` debugging specifier requires 3.8+).

### Execution

Explained in each of the folders README's.