__author__ = 'tkhirianov'

class UniversityMember:
    passToUniversity = ''
    status = True

    def checkStatus(self):
        return self.status

    def dismiss(self):
        self.status = False
        self.pass_to_university = None

class Student(UniversityMember):
    group = None

class Teacher(UniversityMember):
    cathedral = None

class Administrator(UniversityMember):
    pass


