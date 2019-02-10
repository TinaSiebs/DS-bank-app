# Bank App

## Setup

```sh
git clone https://github.com/neuefische/DS-bank-app.git
```

```sh
conda env create --file environment.yml
source activate neue-fische-bank-app
```

## Usage

```sh
conda env update --file environment.yml
source activate neue-fische-bank-app
jupyter notebook
```


## Lessons

### Lesson 1

```bash
 # Check out the branch
 git checkout lesson_1

 # Run the tests
 pytest
 flake8

 # Commit and push your results
 git add .
 git commit -m 'Implement bank'
 git push
```

Die Bank soll folgende Eigenschaften haben:

Properties:
- Namen (String)
- Accounts (List)
- Transactions (List)

Methods:
- open_account()
- add_transaction()

### Lesson 2

```
 # Check out the branch
 git remote add upstream https://github.com/neuefische/DS-bank-app.git
 git checkout -b lesson_2 upstream/lesson_2
 git push -u origin lesson_2

 # Run the tests
 pytest tests/app/test_account.py
 pytest tests/app/test_transaction.py
 pytest tests/app/test_bank.py

 # Commit and push your results
 git add .
 git commit -m 'Implement bank with accounts and transactions'
 git push
```

### Lesson 3

```
 # Check out the branch
 git fetch --all
 git checkout -b lesson_3 upstream/lesson_3
 git push -u origin lesson_3

 # Update the app module
 conda env update --file environment.yml

 # Run the tests
 pytest tests/app/test_bank_initialization.py
 pytest tests/app/test_bank_accounts_interaction.py
 pytest tests/app/test_bank_transactions_interaction.py

 # Commit and push your results
 git add .
 git commit -m 'Implement bank with pandas'
 git push
```


## Tests

```sh
pytest # tests
```

```sh
flake8 # codestyle - Should return `0` if all checks are passed successfully.
```
