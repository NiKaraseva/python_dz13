import csv

class MyException(Exception):
    pass

class InvalidNameException(MyException):
    def __init__(self):
        self.message = f'Invalid value: full name should be istitle and isalpha'
        super().__init__(self.message)

class InvalidSubjectException(MyException):
    def __init__(self, subject_name: str):
        self.message = f'Subject {subject_name} not found'
        super().__init__(self.message)

class InvalidGradeException(MyException):
    def __init__(self, grade_res: int):
        self.message = f'Grade {grade_res} is invalid, it should be between 2 and 5'
        super().__init__(self.message)

class InvalidTestResException(MyException):
    def __init__(self, test_res: int):
        self.message = f'Grade {test_res} is invalid, it should be between 0 and 100'
        super().__init__(self.message)


class CheckName:

    def __set_name__(self, owner, name):
        self._param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)\

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self._param_name, value)

    def validate(self, value):
        if not value.isalpha() or not value.istitle():
            raise InvalidNameException()


class Student:
    name = CheckName()
    surname = CheckName()
    patronymic = CheckName()


    def __init__(self, name: str, surname: str, patronymic: str, file_name: str):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.subjects = self.sub_from_csv(file_name)
        self.grades = {subject: [] for subject in self.subjects}
        self.test_results = {subject: [] for subject in self.subjects}


    def sub_from_csv(self, file_name: str):
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            return next(reader)


    def __str__(self):
        return f'Student: name = {self.name}, surname = {self.surname}, patronymic = {self.patronymic}'


    def add_grades(self, subject: str, grade: int):
        if subject not in self.subjects:
            raise InvalidSubjectException(subject)
        if 2 > grade or grade > 5:
            raise InvalidGradeException(grade)
        self.grades[subject].append(grade)


    def add_test_results(self, subject: str, t_res: int):
        if subject not in self.subjects:
            raise InvalidSubjectException(subject)
        if 0 > t_res or t_res > 100:
            raise InvalidTestResException(t_res)
        self.test_results[subject].append(t_res)


    def average_grade(self):
        sum_grade = sum([sum(grade) for grade in self.grades.values()])
        sum_sub = sum([len(grade) for grade in self.grades.values()])
        if sum_sub:
            return sum_grade / sum_sub


    def average_test_results(self):
        for subject in self.subjects:
            if self.test_results[subject]:
                average_t_res = {subject: sum(self.test_results[subject]) / len(self.test_results[subject])}
            return average_t_res


if __name__ == '__main__':
    st1 = Student('Ivan', 'Ivanov', 'Ivanovich', 'sub.csv')
    print(st1)
    # InvalidNameException
    # st2 = Student('Petr1', 'Petrov', 'Petrovich', 'sub.csv')
    # print(st2)

    # InvalidSubjectException
    # st1.add_test_results('literature', 34)

    st1.add_grades('math', 3)
    st1.add_grades('math', 4)
    st1.add_grades('physics', 5)

    # InvalidGradeException
    # st1.add_grades('physics', 10)


    st1.add_test_results('math', 67)
    st1.add_test_results('math', 54)

    # InvalidTestResException
    # st1.add_test_results('physics', 115)



