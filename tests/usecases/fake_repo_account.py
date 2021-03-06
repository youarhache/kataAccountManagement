from bankaccount.entities.account import Account

class MemRepoAccounts:
    def __init__(self, db_session=None, entries=None):
        self._entries = []
        if entries:
            self._entries.extend(entries)

    def find_account(self, account_code= None):
        _elem = next((e for e in self._entries if e['code']==account_code), None)
        return Account.from_dict(_elem) if _elem else None

    def add_account(self, account=None):
        if account:
            self._entries.append(account.to_dict())

    def account_deposit(self, account=None, amount=None):
        _acc = self.find_account(account.code) if account else None
        if _acc:
            _balance = float(_acc.balance) + amount
            for e in self._entries:
                if e['code'] == _acc.code:
                    e['balance'] = _balance

    def account_withdraw(self, account=None, amount=None):
        _acc = self.find_account(account.code) if account else None
        if _acc:
            _balance = float(_acc.balance) - amount
            for e in self._entries:
                if e['code'] == _acc.code:
                    e['balance'] = _balance   