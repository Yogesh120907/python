"""
Experiment 19: Graphical data-entry form (Tkinter + SQLite) to manage library records
(Add, Issue, Return, and Search operations).
"""
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox


class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System (SQLite)")
        self.root.geometry("760x500")

        self.conn = sqlite3.connect("library_records.db")
        self.create_table()

        form_frame = tk.LabelFrame(root, text="Book Details", padx=10, pady=10)
        form_frame.pack(fill="x", padx=12, pady=8)

        tk.Label(form_frame, text="Book ID:").grid(row=0, column=0, sticky="w", padx=5, pady=4)
        self.book_id_var = tk.StringVar()
        tk.Entry(form_frame, textvariable=self.book_id_var, width=20).grid(row=0, column=1, padx=5, pady=4)

        tk.Label(form_frame, text="Title:").grid(row=0, column=2, sticky="w", padx=5, pady=4)
        self.title_var = tk.StringVar()
        tk.Entry(form_frame, textvariable=self.title_var, width=28).grid(row=0, column=3, padx=5, pady=4)

        tk.Label(form_frame, text="Author:").grid(row=1, column=0, sticky="w", padx=5, pady=4)
        self.author_var = tk.StringVar()
        tk.Entry(form_frame, textvariable=self.author_var, width=20).grid(row=1, column=1, padx=5, pady=4)

        tk.Label(form_frame, text="Issued To:").grid(row=1, column=2, sticky="w", padx=5, pady=4)
        self.borrower_var = tk.StringVar()
        tk.Entry(form_frame, textvariable=self.borrower_var, width=28).grid(row=1, column=3, padx=5, pady=4)

        btn_frame = tk.Frame(root, pady=6)
        btn_frame.pack(fill="x", padx=12)

        tk.Button(btn_frame, text="Add Book", width=13, command=self.add_book).pack(side="left", padx=4)
        tk.Button(btn_frame, text="Issue Book", width=13, command=self.issue_book).pack(side="left", padx=4)
        tk.Button(btn_frame, text="Return Book", width=13, command=self.return_book).pack(side="left", padx=4)
        tk.Button(btn_frame, text="Search Title", width=13, command=self.search_book).pack(side="left", padx=4)
        tk.Button(btn_frame, text="Show All", width=12, command=self.load_books).pack(side="left", padx=4)

        columns = ("book_id", "title", "author", "status", "issued_to")
        self.tree = ttk.Treeview(root, columns=columns, show="headings", height=14)
        for col, heading in zip(columns, ["Book ID", "Title", "Author", "Status", "Issued To"]):
            self.tree.heading(col, text=heading)
            self.tree.column(col, width=140)
        self.tree.pack(fill="both", expand=True, padx=12, pady=8)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        self.load_books()

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS books (
                book_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                status TEXT DEFAULT 'Available',
                issued_to TEXT DEFAULT '-'
            )
        """)
        self.conn.commit()

    def add_book(self):
        bid, title, author = self.book_id_var.get().strip(), self.title_var.get().strip(), self.author_var.get().strip()
        if not (bid and title and author):
            messagebox.showwarning("Input Error", "Book ID, Title, and Author are required.")
            return
        try:
            self.conn.execute(
                "INSERT INTO books (book_id, title, author, status, issued_to) VALUES (?, ?, ?, 'Available', '-')",
                (bid, title, author)
            )
            self.conn.commit()
            self.load_books()
            self.clear_inputs()
            messagebox.showinfo("Success", f"Book '{title}' added.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Duplicate ID", f"Book ID '{bid}' already exists.")

    def issue_book(self):
        bid = self.book_id_var.get().strip()
        borrower = self.borrower_var.get().strip()
        if not (bid and borrower):
            messagebox.showwarning("Input Error", "Provide Book ID and Borrower name to issue.")
            return
        cur = self.conn.execute("SELECT status FROM books WHERE book_id = ?", (bid,))
        row = cur.fetchone()
        if not row:
            messagebox.showerror("Not Found", "Book ID not found.")
        elif row[0] == "Issued":
            messagebox.showwarning("Unavailable", "Book is already issued.")
        else:
            self.conn.execute(
                "UPDATE books SET status = 'Issued', issued_to = ? WHERE book_id = ?",
                (borrower, bid)
            )
            self.conn.commit()
            self.load_books()
            messagebox.showinfo("Issued", f"Book '{bid}' issued to {borrower}.")

    def return_book(self):
        bid = self.book_id_var.get().strip()
        if not bid:
            messagebox.showwarning("Input Error", "Enter or select a Book ID to return.")
            return
        cur = self.conn.execute("SELECT status FROM books WHERE book_id = ?", (bid,))
        row = cur.fetchone()
        if not row:
            messagebox.showerror("Not Found", "Book ID not found.")
        elif row[0] == "Available":
            messagebox.showinfo("Info", "Book is already marked Available.")
        else:
            self.conn.execute(
                "UPDATE books SET status = 'Available', issued_to = '-' WHERE book_id = ?",
                (bid,)
            )
            self.conn.commit()
            self.load_books()
            messagebox.showinfo("Returned", f"Book '{bid}' returned successfully.")

    def search_book(self):
        query = self.title_var.get().strip()
        for item in self.tree.get_children():
            self.tree.delete(item)
        cur = self.conn.execute(
            "SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR book_id LIKE ?",
            (f"%{query}%", f"%{query}%", f"%{query}%")
        )
        for row in cur.fetchall():
            self.tree.insert("", "end", values=row)

    def load_books(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in self.conn.execute("SELECT * FROM books"):
            self.tree.insert("", "end", values=row)

    def on_select(self, _event):
        selected = self.tree.focus()
        if selected:
            vals = self.tree.item(selected, "values")
            self.book_id_var.set(vals[0])
            self.title_var.set(vals[1])
            self.author_var.set(vals[2])
            self.borrower_var.set("" if vals[4] == "-" else vals[4])

    def clear_inputs(self):
        self.book_id_var.set("")
        self.title_var.set("")
        self.author_var.set("")
        self.borrower_var.set("")


if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
