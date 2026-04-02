# Assignment 7 – Measurement Converter GUI

## Student Info
- Student: <Brian Moore>

## Description
- A PySide6 desktop GUI that converts between inches and meters and back.
- Validates all input and displays results rounded to three decimal places.

## Tools / Versions
- Python 3.11+
- PySide6 6.x
- IDE: VS Code

## How to Run
1. Install PySide6 if needed: pip install PySide6
2. Place house.png in the same folder as converter.py
3. Run: python converter.py

## File Structure
- house.png
- converter.py
- Assignment_7_readme.md

## Test Cases
- empty input: Error: "Please enter a value."
- ABC: Error: "Value entered is not numeric."
- -5: Error: "Value must be positive."
- 5.5 inches to meters: 5.500 inches = 0.140 meters
- 10 meters to inches: 10.000 meters = 393.701 inches

## Attributions
- PySide6 official docs: https://doc.qt.io/qtforpython-6/
- No external code was copied. All logic is original.