# Expense Tracker

A simple console expense tracker written in Python. It stores your expenses in a local JSON file and shows totals by category.

## Features

- Add an expense: category, amount and an optional comment
- Show all expenses as a numbered list
- Show the total amount for each category
- Data is saved automatically after every added expense
- Negative amounts are allowed (for example, a refund)
- If the data file is damaged or has an unexpected structure, it is renamed to `saved_data.json.corrupted` (then `.corrupted1`, `.corrupted2`, ...) and a new empty file is created

## Requirements

- Python 3.12 or newer (the code uses `match` and nested quotes inside f-strings)
- No external libraries, only the standard library

## How to run

```bash
python3 main.py
```

On the first launch, `saved_data.json` is created automatically.

## Usage

```
===Main menu===
0. Exit
1. Show all expenses
2. Add expenses
3. Total expenses
```

Enter the number of an action and press Enter. When adding an expense:

1. Enter a category name (it cannot be empty; it is saved in lowercase)
2. Enter an amount (rounded to 2 decimal places; `nan` and `inf` are rejected)
3. Enter a comment, or type `0` to skip it

## Data format

Expenses are stored in `saved_data.json` as a list of objects:

```json
[
  {
    "Category": "food",
    "Amount": 12.5,
    "Comment": "lunch"
  }
]
```

## Known limitations

- No editing or deleting of expenses
- No dates yet
- The check of a manually edited data file is not complete, so a broken file may still cause an error

## What I practiced

Functions, working with JSON files, input validation, exception handling, and publishing a project on GitHub.
