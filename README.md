# OnSetto-Inc-engineering-challenge

# Banking Account Updater

Automation solution for updating banking details and payment information through the web application.

## Tech Stack

- Python 3.11+
- Playwright
- Pytest

## Project Structure

```text
.
├── pages/
│   ├── login_page.py
│   └── account_page.py
├── tests/
│   └── test_account_update.py
├── .env.example
├── requirements.txt
├── Makefile
└── README.md
```

## Setup

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
make setup
```

or manually:

```bash
pip install -r requirements.txt
playwright install
```

### 4. Configure environment variables

Create a `.env` file from `.env.example`:

```bash
cp .env.example .env
```

Example:

```env
BASE_URL=https://example.com
USERNAME=test_user
PASSWORD=test_password
MFA_CODE=123456
```

## Running the tests

```bash
make test
```

or

```bash
pytest
```

## Notes

- Sensitive information is stored in `.env`.
- The `.env` file is excluded from version control.
- Stable selectors (`id` and `data-testid`) are used throughout the automation.