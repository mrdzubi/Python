class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        sum_ = 0
        overal_score = 0
        count = 0
        for course, score in self.grades.items():
            for sum_score in score:
                sum_ += sum_score
            else:
                average_score = sum_ / len(score)
                overal_score += average_score
                count += 1
                sum_ = 0
        else:
            return round(overal_score / count, 2)

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
               f'Средняя оценка за домашнее задание: {self.average_rating()}\n'
               f'Курсы в процессе изучения: {(", ".join(map(str, self.courses_in_progress)))}\n'
               f'Заершенные курсы:{(", ".join(map(str, self.finished_courses)))}')
        return res

    def __lt__(self, other):
        if self.average_rating() > other.average_rating():
            return f'Ученик {self.name} порядочнее {other.name}'
        else:
            return f'Ученику {self.name} надо догнать успеваемость {other.name}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rating(self):
        sum_ = 0
        overal_score = 0
        count = 0
        for course, score in self.grades.items():
            for sum_score in score:
                sum_ += sum_score
            else:
                average_score = sum_ / len(score)
                overal_score += average_score
                count += 1
                sum_ = 0
        else:
            return round(overal_score / count, 2)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating()}'
        return res

    def __lt__(self, other):
        if self.average_rating() > other.average_rating():
            return f'Лектор {self.name} интереснее {other.name}'
        else:
            return f'Лектору {self.name} надо прокачать очки харизмы {other.name}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


vanya = Lecturer('Ivan', 'Ivanov')
vanya.courses_attached.append('Python')
vanya.courses_attached.append('Git')

olya = Lecturer('Olga', 'Ivanova')
olya.courses_attached.append('Python')
olya.courses_attached.append('Git')

andrew = Student('Andrew', 'Terentev', 'male')
andrew.courses_in_progress.append('Python')
andrew.courses_in_progress.append('Git')
andrew.add_courses('photo')
andrew.rate_lecturer(vanya, 'Python', 4)
andrew.rate_lecturer(vanya, 'Git', 6)
andrew.rate_lecturer(olya, 'Python', 7)
andrew.rate_lecturer(olya, 'Git', 5)

sonya = Student('Sonya', 'Ivanova', 'female')
sonya.courses_in_progress.append('Python')
sonya.courses_in_progress.append('Git')
sonya.add_courses('photo')
sonya.rate_lecturer(vanya, 'Python', 6)
sonya.rate_lecturer(vanya, 'Git', 2)
sonya.rate_lecturer(olya, 'Python', 4)
sonya.rate_lecturer(olya, 'Git', 8)

bob = Reviewer('Bob', 'Bobson')
bob.rate_hw(andrew, 'Python', 3)
bob.rate_hw(andrew, 'Python', 3)
bob.rate_hw(andrew, 'Python', 4)
bob.rate_hw(sonya, 'Python', 3)
bob.rate_hw(sonya, 'Python', 7)
bob.rate_hw(sonya, 'Python', 3)
print(bob)
print('____________________________________________________________________________')

naruto = Reviewer('Naruto', 'Uzumaki')
naruto.rate_hw(andrew, 'Git', 6)
naruto.rate_hw(sonya, 'Git', 9)
print(naruto)
print('____________________________________________________________________________')

cheburashka = Mentor('Oleg', 'Olegovich')
print(cheburashka)
print('____________________________________________________________________________')

gena = Mentor('Gennadiy', 'Bukin')
print(gena)
print('____________________________________________________________________________')
print(vanya)
print(vanya.average_rating())
print('____________________________________________________________________________')
print(olya)
print(olya.average_rating())
print('____________________________________________________________________________')
print(vanya > olya)
print('____________________________________________________________________________')
print(andrew)
print(andrew.average_rating())
print('____________________________________________________________________________')
print(sonya)
print(sonya.average_rating())
print('____________________________________________________________________________')
print(sonya > andrew)
print('____________________________________________________________________________')

print(andrew.grades)

student_list = [andrew, sonya]
student_average = {}
lecturer_list = [vanya, olya]
lecturer_average = {}


def average_student(student_list, courses):
    for stud in student_list:
        for courses_, score in stud.grades.items():
            sum_ = 0
            if courses_ == courses:
                for k in score:
                    sum_ += k
                else:
                    average = round(sum_ / len(score), 2)
                    student_average[courses] = [average]
                    print(f'{stud.name} {stud.surname} средний балл по {courses} = {average}')
    else:
        return ''


print(average_student(student_list, 'Python'))


def average_lecturer(lecturer_list, courses):
    for lect in lecturer_list:
        for courses_, score in lect.grades.items():
            sum_ = 0
            if courses_ == courses:
                for k in score:
                    sum_ += k
                else:
                    average = round(sum_ / len(score), 2)
                    lecturer_average[courses] = [average]
                    print(f'{lect.name} {lect.surname} средний балл по {courses} = {average}')
    else:
        return ''


print(average_lecturer(lecturer_list, 'Python'))
