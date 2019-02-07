import app


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.transactions = []

    def open_account(self, account):
        assert type(account) == app.Account, 'Account should be an app.Account'
        assert account.number not in self.accounts, 'Account number 1 already taken!'
        self.accounts.update({account.number: account})
        return account

    def add_transaction(self, *, sender, recipient, subject, amount):

        transaction = app.Transaction(sender=sender.number, recipient=recipient.number, subject=subject, amount=amount)

        self.transactions.append(transaction)

        assert sender.number in self.accounts, 'Sender has no account yet!'
        assert recipient.number in self.accounts, 'Recipient has no account yet!'

        return transaction










