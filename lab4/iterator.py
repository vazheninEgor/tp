from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass
    
    @abstractmethod
    def next(self):
        pass

class StudentIterator(Iterator):
    def __init__(self, students):
        self.students = students
        self.position = 0
    
    def has_next(self):
        return self.position < len(self.students)
    
    def next(self):
        if self.has_next():
            student = self.students[self.position]
            self.position += 1
            return student
        else:
            raise StopIteration("No more students")

class StudentCollection:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def create_iterator(self):
        return StudentIterator(self.students)

if __name__ == "__main__":
    students = StudentCollection()
    students.add_student("Alice")
    students.add_student("Bob")
    students.add_student("Charlie")
    
    iterator = students.create_iterator()

    while iterator.has_next():
        print(iterator.next())