# str.format()

> Using the `.format()` method to insert variables into strings with positional placeholders.

---

## 📌 Overview

`str.format()` is one of Python's traditional string formatting methods. It works by placing curly braces `{}` inside a string as placeholders, and passing the values to fill them in as arguments to the `.format()` method.

---

## 🧠 Key Concepts

1. **Positional Placeholders:** `{0}`, `{1}`, `{2}`... refer to the position of the arguments passed to `.format()`, in order.
2. **Reusing Arguments:** The same positional index can be used more than once within the same string.
3. **Expressions Inside Arguments:** While you can't run arbitrary code inside the `{}` themselves, you *can* pass the result of function calls or expressions (like `name1.upper()` or `age + 5`) as arguments to `.format()`.

---

## 💻 Code Breakdown

```python
message1 = "we are: {0}, and {1}, and we are {2} years old".format(name1, "John", age)
```
`{0}` maps to `name1`, `{1}` maps to `"John"`, and `{2}` maps to `age`.

```python
message2 = "we are: {0}, and {1}, and we are {2} years old".format(name1.upper(), "John".lower(), age + 5)
```
Here, the arguments themselves are transformed *before* being inserted: `.upper()`, `.lower()`, and `age + 5` are all evaluated first, and their results are what get placed into `{0}`, `{1}`, and `{2}`.

---

## 🚀 How to Run

```bash
python main.py
```

**Expected output:**
```
we are: Tomas, and John, and we are 10 years old
we are: TOMAS, and john, and we are 15 years old
```