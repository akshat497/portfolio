import json
class student:
    def __init__(self,name,age,marks):

        self.name=name
        self.age=age
        self.marks=marks
    def average(self):
        print(sum(self.marks))

        return sum(self.marks)/len(self.marks)
    def dictionary(self):
        return {
            "Name":self.name,
            "age":self.age,
            "marks":self.marks,
            "average":self.average()
        }


        
student_db={}

def addstudent(): 
    marks=[]
    name=input("enter students name")
    age=int(input("enter students age"))
    for i in range(3):
        subject=int(input(f"enter marks for subject {i+1}"))
        marks.append(subject)

    s=student(name,age,marks)
    student_db[name]=s.dictionary()

    
    print("student added successfully")
def insertDb():
    print("student inserted successfully")
def loadFromDB():
    print("student loaded successfully")


def insertDb():
   try:
        file=open("students.txt","w")
        json.dump(student_db,file)
        print("saved in database successfully")
   except:
        print("Error while dumping error")


def loadFromDB():
    try:
        file=open("students.txt","r")
        data=json.load(file)
        
        student_db.update(data)
        print(student_db)

    except:
        print("error in loading")
while(True):
    print("1 add student")
    print("2 insert in db")
    print("3 load from db")
    print("4 to exit")
    choice=int(input("Enter your choice"))

    if(choice==1):
        addstudent()
    elif(choice==2):
        insertDb()
    elif(choice==3):
        loadFromDB()
    elif(choice==4):
        break