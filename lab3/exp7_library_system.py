class LibraryItem:
    def __init__(self, item_id: str, title: str):
        self.item_id = item_id
        self.title = title
        self.is_issued = False

    def issue(self) -> str:
        if not self.is_issued:
            self.is_issued = True
            return f"Item '{self.title}' issued successfully."
        return f"Item '{self.title}' is already issued."

    def return_item(self) -> str:
        if self.is_issued:
            self.is_issued = False
            return f"Item '{self.title}' returned successfully."
        return f"Item '{self.title}' was not issued."

class Book(LibraryItem):
    def __init__(self, item_id: str, title: str, author: str):
        super().__init__(item_id, title)
        self.author = author

class Magazine(LibraryItem):
    def __init__(self, item_id: str, title: str, issue_number: int):
        super().__init__(item_id, title)
        self.issue_number = issue_number

class Journal(LibraryItem):
    def __init__(self, item_id: str, title: str, volume: int):
        super().__init__(item_id, title)
        self.volume = volume

if __name__ == "__main__":
    items: list[LibraryItem] = [
        Book("B001", "Clean Code", "Robert C. Martin"),
        Magazine("M101", "National Geographic", 2024),
        Journal("J501", "IEEE Software", 41)
    ]
    for item in items:
        print(item.issue())
        print(item.return_item())
