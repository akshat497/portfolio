import datetime
import json
import os

# ============================
# LOAD DATA (If files exist)
# ============================
def load_data(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return {}

students = load_data("students.json")
books = load_data("books.json")
issued_books = load_data("issued_books.json")    # key = book_id, value = details


# ============================
# SAVE DATA
# ============================
def save_data():
    with open("students.json", "w") as f:
        json.dump(students, f, indent=4)
    with open("books.json", "w") as f:
        json.dump(books, f, indent=4)
    with open("issued_books.json", "w") as f:
        json.dump(issued_books, f, indent=4)


# ============================
# ADD STUDENT
# ============================
def add_student():
    sid = input("Enter student ID: ")
    name = input("Enter student name: ")

    students[sid] = {"name": name}
    save_data()
    print("Student added successfully!\n")


# ============================
# ADD BOOK
# ============================
def add_book():
    bid = input("Enter book ID: ")
    title = input("Enter book title: ")

    books[bid] = {
        "title": title,
        "available": True
    }
    save_data()
    print("Book added successfully!\n")


# ============================
# ISSUE BOOK
# ============================
def issue_book():
    sid = input("Enter student ID: ")
    bid = input("Enter book ID: ")

    if sid not in students:
        print("Student does not exist!")
        return
    
    if bid not in books:
        print("Book does not exist!")
        return

    if not books[bid]["available"]:
        print("Book is already issued to someone else!")
        return

    days = int(input("Enter number of days to issue: "))

    issue_date = datetime.date.today()
    due_date = issue_date + datetime.timedelta(days=days)

    issued_books[bid] = {
        "student_id": sid,
        "issue_date": str(issue_date),
        "due_date": str(due_date)
    }

    books[bid]["available"] = False
    save_data()

    print(f"Book issued successfully! Due date: {due_date}\n")


# ============================
# RETURN BOOK
# ============================
def return_book():
    bid = input("Enter Book ID to return: ")

    if bid not in issued_books:
        print("This book is not issued!")
        return

    info = issued_books[bid]
    sid = info["student_id"]

    due_date = datetime.datetime.strptime(info["due_date"], "%Y-%m-%d").date()
    today = datetime.date.today()

    print(f"Book Title: {books[bid]['title']}")
    print(f"Issued to: {students[sid]['name']}")
    print(f"Due Date: {due_date}")
    print(f"Return Date: {today}")

    # Fine Calculation
    if today > due_date:
        days_late = (today - due_date).days
        fine = days_late * 10   # Rs. 10 per day
        print(f"\n❗ Book returned late by {days_late} days")
        print(f"💰 Fine to be paid: Rs. {fine}")
    else:
        print("\nReturned on time. No fine!")

    # Mark book as available
    books[bid]["available"] = True

    # Remove from issued list
    del issued_books[bid]

    save_data()
    print("\nBook returned successfully!\n")


# ============================
# MAIN MENU LOOP
# ============================
while True:
    print("\n========= LIBRARY MANAGEMENT SYSTEM =========")
    print("1. Add Student")
    print("2. Add Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")
    print("=============================================")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        add_book()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        print("Thank you for using the Library System!")
        break
    else:
        print("Invalid choice. Try again.\n")
