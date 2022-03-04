class School:
    class_roster = []
    
    def __init__(self):
        pass

    def add_student(self, name, grade):
        self.name = name
        self.grade = grade
        
        return True

    def roster(self):
        name = self.name

        return self.class_roster

    def grade(self, grade_number):
        self.grade_number = grade_number
        pass

    def added(self):
        pass


# school = School()
# print(school.add_student(name="Aimee", grade=2))

school = School()
print(school.roster())