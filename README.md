# Reverse Polish Notation Calculator
Simple Reverse Polish Notation calculator. It works with integer numbers only and the basic operators (+, -, *, /). The division result is the integer part of it.

## How it works:
1. Read a input.
2. If it is an integer (operand), push to the stack.
3. If it is an operator, pop the last and second-to-last operands off the list, do the operation and then push it back to the stack.
4. If it is empty, close the program.

## Usage:
1. ```git clone https://github.com/crespo/reverse-polish-notation.git```
2. ```cd ./reverse-polish-notation```
3. ```python main.py```
4. ```Type a integer number or a basic operator (+ = sum, - = subtraction, * = multiplication, / = division) and ↵ Enter.```
5. ```When you've finished, type ↵ Enter again and the program should stop.```

