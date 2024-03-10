class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        self.all_books.append(self)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.book == self]

    def authors(self):
        return list(set(contract.author for contract in self.contracts()))


class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self.all_authors.append(self)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        return list(set(contract.book for contract in self.contracts()))

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("The book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("The date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("The royalties must be an integer.")
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("The author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("The book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("The date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("The royalties must be an integer.")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return sorted([contract for contract in cls.all_contracts if contract.date == date], key=lambda x: x.date)
