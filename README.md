# OnSetto-Inc-engineering-challenge

# Banking Account Updater

Automation solution for updating banking details and payment information through the web application. 
It has 2 solutions: 
1. A web scraping.
2. A Python client.

## Tech Stack

- Python 3.11+
- Playwright
- Pytest

## Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── api client/
│   ├── api_client.py
│   ├── exceptions.py
│   └── run.py
└── web scraping/
    ├── conftest.py
    ├── pages/
    │   ├── __init__.py
    │   ├── account_page.py
    │   └── login_page.py
    └── tests/
        └── test_account_page.py
```

## Setup for web scraping part

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Create a virtual environment

#### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

#### Windows PowerShell

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 4. Configure environment variables

Create a `.env` file in the repository root with your test values. Change it with your data

Example:

```env
BASE_URL=https://marketplace.dev-challenge.com/login
LOGIN_USERNAME=username@test.com
LOGIN_PASSWORD=P@ssword123!
MFA_CODE=1234
```

> Note: avoid using reserved names like `USERNAME` on Windows because the OS may already set `USERNAME`.

## Running the web scraping tool: 

recommended one: because an actual navigator tap will open

```bash
pytest -s --headed --slowmo 1000 
```

or from the repository root:

```bash
pytest -s "web scraping/tests/test_account_page.py"
```

or to run the full suite:

```bash
pytest -s "web scraping/tests"
```

## Setup for the API client

The Python API client is a simple synchronous script that uses `requests` and `.env` values.

1. Activate the virtual environment:

#### Linux / macOS

```bash
source .venv/bin/activate
```

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create or update `.env` with your API credentials:

```env
LOGIN_USERNAME=username@test.com
LOGIN_PASSWORD=P@ssword123!
MFA_CODE=1234
```

4. Run the client from the repository root:

#### Linux / macOS

```bash
python "api client/run.py"
```

#### Windows PowerShell

```powershell
python "api client/run.py"
```

This will print the banking and payment update responses in the terminal.

## Notes

- Sensitive information is stored in `.env`.
- The `.env` file is excluded from version control.
- Stable selectors (`id` and `data-testid`) are used throughout the automation.

