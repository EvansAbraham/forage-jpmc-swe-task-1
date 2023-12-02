# JPMorgan Chase & Co Software Engineering Job Virtual Job Simulation Task 1

## Table of Contents
1. [Introduction](#introduction)
2. [Project Overview](#project-overview)
3. [Code Explanation](#code-explanation)
4. [Unit Tests](#unit-tests)
5. [How to Run](#how-to-run)
6. [License](#license)

## Introduction
This project is part of the Software Engineering Job Virtual Job Simulation provided by JPMorgan Chase & Co via The Forge platform. It involves a simulated trading application implemented in Python.

## Project Overview
The project includes the following files:
- `client3.py`: Main codebase for querying stock prices, calculating ratios, and other functionalities.
- `client_test.py`: Unit tests for the `client3.py` codebase.
- `server3.py`: Simulated server API for providing stock quotes.
- `requirements.txt`: Lists the project dependencies.
- `test.csv`: Sample CSV file used in the project.

## Code Explanation
- `client3.py`: Contains functions for querying stock prices, calculating ratios, and handling data points. The `getDataPoint` function extracts relevant information from stock quotes, and the `getRatio` function calculates the ratio between two prices.

- `client_test.py`: Includes unit tests using the `unittest` framework to ensure the correctness of the code in `client3.py`. Each test case evaluates specific scenarios to validate the functionality of the code.

- `server3.py`: Simulates a server API that provides stock quotes. This file is part of the overall simulation.

## Unit Tests
The unit tests in `client_test.py` cover scenarios such as calculating average prices, handling cases where bid prices are greater than ask prices, handling zero ask prices, and managing empty quotes. Additional tests can be added to cover various edge cases.

## How to Run
1. Ensure you have the required dependencies installed by running:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the unit tests using the following command:
   ```bash
   python -m unittest client_test.py
   ```
   
## License
This project is licensed under the [MIT License](LICENSE).

---
