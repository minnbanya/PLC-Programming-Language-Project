# PLC Programming Language Project

This project is part of the coursework for the Programming Languages and Compilers course. It features a custom programming language that allows users to explore basic concepts such as variable management, control flow, and arithmetic operations within a simple interpreter environment.

## Students Information
- **Name**: Minn Banya
- **Student ID**: st124145
- **Name**: Phone Myint Zaw
- **Student ID**: st124359
- **Name**: Puthi Soptey
- **Student ID**: st124390
- **Course**: Programming Languages and Compilers

## Installation and Setup

To get started with this programming environment, you'll need to have Python installed on your computer.

### Steps to Setup

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourGithubUsername/PLC-Programming-Language-Project  
2. Change into the project directory:
    ```bash
    cd PLC-Programming-Language-Project
3. Run the program using Python:
    ```bash
    python3 main.py
## Language Syntax Guide

This section provides a detailed guide to the syntax of the custom programming language developed for this project. The language supports basic arithmetic operations, variable assignments, conditional statements, loops, and printing output to the console.

## Usage

Upon running the command, the user interface for the programming language interpreter will launch. Users can enter programs directly into the provided input box.

### Syntax Guide

#### Variable Assignment

- **Syntax**: `variable_name = expression;`
- **Example**: `x = 5;`

#### Arithmetic Expressions

- **Operators**: `+`, `-`, `*`, `/`
- **Usage**: Perform arithmetic operations.
- **Example**: `result = 10 + 5;`

#### Relational Expressions

- **Operators**: `==`, `!=`, `>`, `<`
- **Usage**: Evaluate relational conditions.
- **Example**: `is_greater = x > y;`

#### Control Structures

##### If Statement

- **Syntax**: `if (condition) { statements } else { statements }`
- **Usage**: Execute statements conditionally.
- **Example**:
  ```plaintext
  if (x > 5) {
    PRINT("x is greater than 5");
  } else {
    PRINT("x is not greater than 5");
  }
#### While Loop
- **Syntax**: while (condition) { statements }
- **Usage**: Repeat statements while the condition is true.
- **Example**:
  ```plaintext
  x = 0;
  while (x < 5) {
    PRINT(x);
    x = x + 1;
  }
#### Printing Output
- **Syntax**: print(expression);
- **Usage**: Display the result of an expression.
- **Example**: 
  ```plaintext
  print("Hello, world!");

