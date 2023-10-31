class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_student = {}

    def rate_hw_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'
    
    def avg_rating(self):
        grades_count = 0
        grades_sum = 0
        for grade in self.grades_student:
            grades_count += len(self.grades_student[grade])
            grades_sum += sum(self.grades_student[grade])
        return grades_sum / grades_count

    def __str__(self):
        return (f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}\n'
        f'Средняя оценка за домашние задания: {self.avg_rating()}\n'
        f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Невозможно сравнить!')
            return
        return self.avg_rating() > other.avg_rating()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades_lecturer = {}

    def avg_rating(self):
        grades_count = 0
        grades_sum = 0
        for grade in self.grades_lecturer:
            grades_count += len(self.grades_lecturer[grade])
            grades_sum += sum(self.grades_lecturer[grade])
        return grades_sum / grades_count

    def __str__(self):
        return (f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}\n'
        f'Средняя оценка за лекции: {self.avg_rating()}')

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Невозможно сравнить!')
            return
        return self.avg_rating() > other.avg_rating()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades_student:
                student.grades_student[course] += [grade]
            else:
                student.grades_student[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

some_student = Student('Ruoy', 'Eman', 'man')
second_student = Student('Ivan', 'Ivanov', 'man')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']
second_student.finished_courses += ['Введение в программирование']

some_reviewer = Reviewer('Some', 'Buddy')
second_reviewer = Reviewer('Oleg', 'Petrov')
some_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['Python']

some_lecturer = Lecturer('Lom', 'Pud')
second_lecturer = Lecturer('Marat', 'Basharov')
some_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Python']

some_reviewer.rate_hw_student(some_student, 'Python', 10)
some_reviewer.rate_hw_student(second_student, 'Python', 8)
second_reviewer.rate_hw_student(some_student, 'Python', 9)
second_reviewer.rate_hw_student(second_student, 'Python', 9)

some_student.rate_hw_lecturer(some_lecturer, 'Python', 10)
some_student.rate_hw_lecturer(second_lecturer, 'Python', 9)
second_student.rate_hw_lecturer(some_lecturer, 'Python', 8)
second_student.rate_hw_lecturer(second_lecturer, 'Python', 10)

# для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def students_rate(students_list, course_name):
    some_list = []
    summ = 0
    count = 0
    for student_hw in students_list:
        for key, value in student_hw.grades_student.items():
          if key == course_name:
            some_list.append(value)
    for i in some_list:
        for n in i:
            summ += n
            count += 1
    avg_rating_all = summ / count
    return f'Средняя оценка за домашние задания по всем студентам в рамках курса {course_name}: {avg_rating_all}'

# для подсчета средней оценки за лекции всех лекторов в рамках курса
def lecturers_rate(lecturers_list, course_name):
    some_list = []
    summ = 0
    count = 0
    for lecturer_hw in lecturers_list:
        for key, value in lecturer_hw.grades_lecturer.items():
          if key == course_name:
            some_list.append(value)
    for i in some_list:
        for n in i:
            summ += n
            count += 1
    avg_rating_all = summ / count
    return f'Средняя оценка за лекции всех лекторов в рамках курса {course_name}: {avg_rating_all}'

# вызов всеx методов и функции по задаче
print(some_student.grades_student)
print(second_student.grades_student)
print('-----')
print(some_lecturer.grades_lecturer)
print(second_lecturer.grades_lecturer)
print('-----')
print(some_reviewer)
print(second_reviewer)
print('-----')
print(some_lecturer)
print(second_lecturer)
print('-----')
print(some_student)
print(second_student)

# проверка > (__gt__)
if some_student > second_student:
    print("Первый студент учится лучше!")
else:
    print("Второй студент учится лучше!")

if some_lecturer > second_lecturer:
    print("Первый лектор лучше преподает")
else:
    print("Второй лектор лучше преподает")

# средние оценки по студентам и лекторам в рамках одного курса
print(students_rate([some_student, second_student], 'Python'))
print(lecturers_rate([some_lecturer, second_lecturer], 'Python'))