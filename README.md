# aplikasi-perpustakaan

# Python CRUD Application for Library Book Borrowing
## Business Understanding
This project caters to the education/library services domain, specifically addressing the need to manage book borrowing data efficiently.
Book borrowing records are crucial for ensuring smooth library operations, tracking availability, and preventing data loss in manual systems.

## Benefits:
Improved data accuracy and consistency in book records

Streamlined borrowing and returning processes

Faster search for book availability and borrower history

Reduced risk of duplicate or missing records

Easier monitoring of library usage

## Target Users:
This application is designed for library staff and members:

Admin/Staff → manage book inventory, member data, and borrowing records

Members/Students → borrow and return books easily

# Features
## Create
Add new book entries with details like ID, title, author, year, stock

Add new member entries with details like ID, name, address, phone number

Validation rules: unique IDs, valid year range, non-empty names

## Read
Search and retrieve specific book records by ID or title

Display all books with availability status (available/borrowed)

Display all members with borrowed book information

## Update
Modify existing book data (title, author, year, stock)

Modify member data (name, address, phone number)

Synchronize updates with borrowing records

## Delete
Remove book records (only if not currently borrowed)

Remove member records (only if no active borrowings)

Confirmation prompts to avoid accidental deletions

Borrow & Return
Borrow books with stock validation and duplicate check

Return books with automatic stock restoration

Real-time synchronization between book and borrowing records

## Installation
Prerequisites
Python 3.13.9

No external database (data stored in memory using list of dict)

## Installation
bash
git clone https://github.com/Firsaadam03/aplikasi-perpustakaant
cd aplikasi-perpustakaan
python main.py
Usage
Run the application:

bash
python main.py
CRUD Operations:

Create: Add a new book or member record

Read: Search book by ID/title or view all members

Update: Change book/member details

Delete: Remove book/member record (with validation)

Borrow/Return: Manage borrowing and returning transactions

## Data Model
This project uses a list of dictionaries to represent data.
Fields stored:

Books (list_buku)
id (int): Unique identifier for each book

judul (string): Title of the book

penulis (string): Author name

tahun (int): Year of publication

stok (int): Number of available copies

Members (list_anggota)
id_anggota (int): Unique identifier for each member

nama (string): Member’s name

alamat (string): Address

no_telp (string): Phone number

Borrowings (list_peminjam)
id_anggota (int): Member ID

nama (string): Member’s name

id_buku (int): Book ID

judul_buku (string): Title of borrowed book

## Contributing
We welcome contributions to this project!
Please feel free to open a pull request or submit an issue if you encounter problems or have suggestions for improvements.
