# introduction 
#single inheritance 

class Employee:
    company = "IBM"
    def show(self , name , id):
        print(f"{name} and {id}")

class Programmer(Employee):
    company = "GOOGLE"
    def language(self , name , language):
        print(f"{name} knows {language}")

a = Employee()
b = Programmer()

print(a.company , b.company)
a.show("aarushi" ,22)
b.language("harry" , "Python")