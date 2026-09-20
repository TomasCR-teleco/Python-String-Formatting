# F-Strings

> Using f-strings (formatted string literals) to embed variables and expressions directly inside a string.

---

## 📌 Overview

F-strings, introduced in Python 3.6, let you embed expressions directly inside string literals by prefixing the string with `f` (or `F`) and wrapping the expression in curly braces `{}`. They are generally the more readable and efficient way to format strings in modern Python.

---

## 🧠 Key Concepts

1. **Basic Syntax:** Prefixing a string with `f"..."` allows variables to be inserted directly using `{variable}`.
2. **Lowercase `f` vs. Uppercase `F`:** Both are valid and behave identically — the choice is purely stylistic. Lowercase `f` is the more common convention.
3. **Expressions Inside `{}`:** Unlike `.format()`, f-strings let you write expressions and function/method calls directly inside the braces, and they are evaluated at runtime — e.g. `{name.upper()}` or `{age + 5}`.

---

## 💻 Code Breakdown

```python
message1 = f"My name is {name} and I am {age} years old."
message2 = F"My name is {name} and I am {age} years old."
```
Both lines produce the exact same result — `f` and `F` are interchangeable.

```python
message3 = f"My name is {name.upper()} and I am {age + 5} years old."
```
Here the expressions `name.upper()` and `age + 5` are evaluated directly inside the braces, and their results are inserted into the string.

---

## 🚀 How to Run

```bash
python main.py
```

**Expected output:**
```
My name is Tomas and I am 10 years old.
My name is Tomas and I am 10 years old.
My name is TOMAS and I am 15 years old.
```