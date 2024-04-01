
# Developer Guide for Advanced Network Scanner Tool

This guide is intended for developers who wish to contribute to the Advanced Network Scanner Tool. It provides an overview of the project structure, setup for development, guidelines for contributing, and information on building and testing the tool.

## Project Structure

The project is organized into several key directories and files:

- `gui/`: Contains the PyQt GUI application files.
- `network_scanner/`: Includes the core network scanning and analysis logic.
- `vulnerability/`: Houses the vulnerability scanning functionality.
- `docs/`: Documentation for the project.
- `tests/`: Unit and integration tests for the project.
- `main_window.py`: The main entry point for the GUI application.
- `requirements.txt`: Lists all the dependencies required to run the project.
- `setup.py`: Script for installing and distributing the tool.

## Setting Up the Development Environment

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/jfuchs01/advanced-network-scanner.git
   ```
2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Contributing to the Project

1. **Fork the Repository**: Make a fork of the project on GitHub to your account.
2. **Create a Feature Branch**: 
   ```bash
   git checkout -b feature-branch-name
   ```
3. **Make Changes**: Develop new features or fix bugs and commit your changes.
4. **Write Tests**: Add or update tests related to the changes you've made.
5. **Run Tests**: Ensure all tests pass and your changes do not introduce new issues.
6. **Submit a Pull Request**: Push your branch to your fork and open a pull request to the main project.

## Coding Standards

- Follow PEP 8 for Python code style.
- Write clean, readable, and well-documented code.
- Ensure code is well-tested and includes new tests for added functionality.

## Building and Testing

- To test the application, run:
  ```bash
  python -m unittest discover tests
  ```




