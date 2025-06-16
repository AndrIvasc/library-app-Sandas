A simple console-based Python application to manage physical book copies entirely in memory (no file or database persistence).

## Features

- Add new book copies (title, author, year)  
- Borrow and return by unique copy ID  
- Search by title/author, showing only the newest edition  
- List all copies with availability status  

## Setup
bash//
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## Usage

python main.py

Follow the on-screen menu to add, borrow, return, search, or list books.  

## Project Structure

.
├── main.py
├── cli.py
├── models.py
├── library.py
└── tests/       # unit tests
└────test_library.py
─────test_models.py
