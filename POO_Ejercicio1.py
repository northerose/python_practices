"""Realizar un programa que conste de una clase llamada Alumno que tenga como atributos 
el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos 
y mostrar un mensaje con el resultado de la nota y si ha aprobado o no."""

import string

class Student:
    def __init__(self, name, score):
        self.name = name.lower()
        self.score = score

    def student_db(self):
        students = [
            {"name": "lin", "score": 8}, 
            {"name": "yuki", "score": 6},
            {"name": "rose", "score": 5},
            {"name": "django", "score": 6},
            {"name": "rollo", "score": 8}
        ]
        return students
 

    def validate_student(self, name):
        exists = False
        for student in self.student_db():
            if name == student["name"]:
                exists = True
                break
        if not exists:
            raise ValueError("NameError, Estudent not in database")

    
    def validate_name(self, name):
        chars = string.punctuation
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        for element in name:
            if element in chars or element in numbers:
                raise ValueError("NameError, please introduce a real name")

    def validate_score(self, score):
        try:
            score = int(score)
        except:
            raise ValueError("ValueError, please introduce a real score")

        if score > 10 and score < 1:
            raise ValueError("ValueError, score must be between 1 and 10")
   
    def give_information(self):
        errors =[]
        try:
            self.validate_student(self.name)
        except Exception as error:
            errors.append(error)

        try:
            self.validate_name(self.name)
        except Exception as error:
            errors.append(error)
        
        try:
            self.validate_score(self.score)
        except Exception as error:
            errors.append(error)

        if errors:
            return errors
            
        return f"Student:{self.name}, score: {self.score}"



name = input("Please introduce student: ")
score = input("Please introduce score: ")

student = Student(name, score)
result = student.give_information()
print(result)




