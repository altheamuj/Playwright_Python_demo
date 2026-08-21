# Playwright Python Automation

> This project is still ongoing.

A hands-on end-to-end test automation project for the [OrangeHRM demo application](https://opensource-demo.orangehrmlive.com/), built with **Python**, **Playwright**, and **pytest**. It follows the **Page Object Model (POM)** design pattern for maintainable, scalable, and reusable test code.

This project is being developed as part of a personal learning journey in test automation, with a focus on writing clean, readable, and reliable UI tests.

---

## Tech Stack

- **Language:** Python
- **Automation Library:** Playwright
- **Test Framework:** pytest
- **Design Pattern:** Page Object Model (POM)
- **OS:** Linux Mint 22.2

---

## Project Structure

```
Playwright_Python_demo/
├── pages/                  # Page Object classes (locators + page actions)
├── tests/                  # Test cases
├── conftest.py             # Shared pytest fixtures (e.g. browser/page setup)
├── pytest.ini              # Pytest configuration
├── requirements.txt        # Project dependencies
├── .gitignore              # Ignored files (e.g. reports, __pycache__)
└── README.md                # This file
```

---

## Setup

Clone the repository:

```bash
git clone https://github.com/altheamuj/Playwright_Python_demo.git
cd Playwright_Python_demo
```

Create and activate a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Install the Playwright browsers:

```bash
playwright install
```

---

## Running Tests

Run the full test suite:

```bash
pytest
```

Run tests in headed mode (to watch the browser):

```bash
pytest --headed
```

Run a specific test file:

```bash
pytest tests/test_login.py
```

Run tests matching a keyword:

```bash
pytest -k "login"
```

---

## 🌐 Application Under Test

- **Site:** [https://opensource-demo.orangehrmlive.com/](https://opensource-demo.orangehrmlive.com/)
