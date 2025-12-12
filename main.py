

# # ============================================
# #   DICTIONARY TEACHING TOOL FOR STUDENTS
# # ============================================

# # def show_menu():
# #     print("\n======= DICTIONARY LEARNING TOOL =======")
# #     print("1. Create a dictionary")
# #     print("2. Access a value")
# #     print("3. Add a new key-value pair")
# #     print("4. Update a value")
# #     print("5. Delete a key")
# #     print("6. Show all keys")
# #     print("7. Show all values")
# #     print("8. Show all items")
# #     print("9. Use get() function")
# #     print("10. Use pop() function")
# #     print("11. Use popitem() function")
# #     print("12. Use clear() function")
# #     print("13. CONVERT STRING IN LOWER CASE")
# #     print("14. CONVERT STRING IN UPPER CASE")
# #     print("==========================================")

# # def dictionary_tool():
# #     student_dict = {}  # empty dict
# #     print("\nA fresh dictionary has been created:", student_dict)

# #     while True:
# #         show_menu()
# #         choice = input("Choose an option (1-13): ")

# #         if choice == '1':
# #             key = input("Enter key: ")
# #             value = input("Enter value: ")
# #             student_dict[key] = value
# #             print("Dictionary created/updated:", student_dict)

# #         elif choice == '2':
# #             key = input("Enter key to access: ")
# #             print("Value:", student_dict.get(key, "Key not found"))

# #         elif choice == '3':
# #             key = input("Enter new key: ")
# #             value = input("Enter value: ")
# #             student_dict[key] = value
# #             print("Updated dictionary:", student_dict)

# #         elif choice == '4':
# #             key = input("Enter key to update: ")
# #             if key in student_dict:
# #                 value = input("Enter new value: ")
# #                 student_dict[key] = value
# #                 print("Updated dictionary:", student_dict)
# #             else:
# #                 print("Key not found!")

# #         elif choice == '5':
# #             key = input("Enter key to delete: ")
# #             if key in student_dict:
# #                 del student_dict[key]
# #                 print("Key deleted. Dictionary:", student_dict)
# #             else:
# #                 print("Key not found!")

# #         elif choice == '6':
# #             print("All keys:", list(student_dict.keys()))

# #         elif choice == '7':
# #             print("All values:", list(student_dict.values()))

# #         elif choice == '8':
# #             print("All items (key-value pairs):", list(student_dict.items()))

# #         elif choice == '9':
# #             key = input("Enter key for get(): ")
# #             print("Result:", student_dict.get(key, "Default: Key not found"))

# #         elif choice == '10':
# #             key = input("Enter key for pop(): ")
# #             print("Popped value:", student_dict.pop(key, "Key not found"))
# #             print("Dictionary:", student_dict)

# #         elif choice == '11':
# #             if student_dict:
# #                 print("Popped last item:", student_dict.popitem())
# #                 print("Dictionary:", student_dict)
# #             else:
# #                 print("Dictionary is empty!")

# #         elif choice == '12':
# #             student_dict.clear()
# #             print("Dictionary cleared:", student_dict)

# #         elif choice == '13':
# #             name=input("enter ur name here in upper case")
# #             print(name.lower())
              
# #         elif choice == '14':
# #             name=input("enter ur name here in lower case")
# #             print(name.upper()) 
            

# #         else:
# #             print("Invalid choice. Try again.")

# # # Run the tool
# # # dictionary_tool()


# # name = "Akshat"

# # age = 21

# # print(f"My name is {name} and I am {age} years old")

# # print("apple" "apple") 


# # class Student:

# #  school = "ABC International School" # class attribute

# #  def __init__(self, name, age):
# #      self.name = name # instance attributes
# #      self.age = age

# # s1 = Student("Aman", 18)

# # s2 = Student("Riya", 17)

# # print(s1.school, s2.school)

# # print(s1.name, s2.name)

# class Car:
#        name="akshat"
#        def __init__(abc, brand, color):
#                abc.brand = brand # attribute. #car1.branc="tesla"
#                abc.color = color #car1.color="red" 
#        def drive(abc):
#            print(f"{abc.brand} is driving...")
# # Object
# car1 = Car("Tesla", "Red")
# car2 = Car("BMW",'bluw')
# car1.drive()

# print(car2.name)


# class Employee:
#     company = "Google"          # class attribute shared by all employees

#     @classmethod#            meta
#     def change_company(cls, new_company):
#         cls.company = new_company #meta

# # Usage:
# print(Employee.company)         # "Google"
# Employee.change_company("Meta")
# print(Employee.company)         # "Meta"

# emp = Employee()
# emp.change_company("Amazon")    # works too
# print(Employee.company)         # "Amazon"


# f = open("new.txt", "r")
# content = f.read()
# print(content)
# f.close()

# f = open("new.txt", "r")
# line1 = f.readline()
# line2 = f.readline()
# print(line1)
# print(line2)

f=open("new.txt","w")
f.write("hello new text")
f.close()