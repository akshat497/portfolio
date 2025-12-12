import json
import datetime
import os

class student:
    def __init__(self,name,sid):
        self.name=name
        self.sid=sid
    def dictionary(self):
        return {
            "name":self.name,
            "sid":self.sid
        }
    
def load_data(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return {}

student_obj=load_data("students.json")
Book_obj=load_data("books.json")
issued_books=load_data("issued_books.json")

def AddStudent():
    name=input("enter student name")
    sid=int(input("enter student Id"))
    stu=student(name,sid)
    student_obj[sid]={"name":name}
    stu.dictionary()
    file=open("students.json","w")
    json.dump(student_obj,file,indent=4)


    print("student addeded successfully")

def addBook():
    Bname=input("enter book name ")
    Bid=int(input("enter book Id "))
    Title=input("enter Book title ")
    Book_obj[Bid]={"name":Bname,"Title":Title,"available":True}
    file=open("books.json","w")
    json.dump(Book_obj,file,indent=4)

    print("Book added successfully")

def IssueBook():
    Sid=input("enter student id  ")
    Bid=input("enter Book id  ")
    print(student_obj)
    if Sid not in student_obj:
        return print("wrong student id")
    
    if Bid not in Book_obj:
        return print("wrong Book id")
    print(Book_obj[Bid]['available'])
    if not Book_obj[Bid]["available"]:
        return print("Book is issued to someone else")
    
    days=int(input("enter number of days for how long u want this book"))

    issue_date = datetime.date.today()
    due_date = issue_date + datetime.timedelta(days=days)
    issued_books[Bid]={
        "student_id":Sid,
        "issueDate":str(issue_date),
        "dueDate":str(due_date)
    }
    file=open("issued_books.json","w")

    Book_obj[Bid]["available"] = False
    
    f=open("books.json","w")
    json.dump(Book_obj, f, indent=4)

    json.dump(issued_books,file,indent=4)
    print("Book issues successfully")

def ReturnBook():
    bid=input("enter book id")
    
    if bid not in issued_books:
        return print("this book is never issued")
    
    info = issued_books[bid]
    sid = info["student_id"]

    # due_date = datetime.datetime.strptime(info["due_date"], "%Y-%m-%d").date()
    # today = datetime.date.today()
    
    print(f"Book Title: {Book_obj[bid]['Title']}")
    print(f"Issued to: {student_obj[sid]['name']}")
    

    #  # Fine Calculation
    # if today > due_date:
    #     days_late = (today - due_date).days
    #     fine = days_late * 10   # Rs. 10 per day
    #     print(f"\n❗ Book returned late by {days_late} days")
    #     print(f"💰 Fine to be paid: Rs. {fine}")
    # else:
    #     print("\nReturned on time. No fine!")

     # Mark book as available
    Book_obj[bid]["available"] = True
    f=open("books.json","w")
    json.dump(Book_obj, f, indent=4)

    # Remove from issued list

    del issued_books[bid]
    f=open("issued_books.json","w")
    json.dump(issued_books, f, indent=4)

    print("Book returned successfully")

while(True):
    print("1 add student")
    print("2 add book")
    print("3 issue book")
    print("4 return book")
    print("5 exit ")

    choice=int(input("enter your choice!"))


    if(choice==1):
        AddStudent()
    elif choice==2:
        addBook()
    elif choice==3:
        IssueBook()
    elif choice==4:
        ReturnBook()
    elif choice==5:
        break

