groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Дмитрий",
        "surname": "Сидоров",
        "exams": ["Математика", "Информатика", "Физика"],
        "marks": [3, 4, 4]
    },
    {
        "name": "Андрей",
        "surname": "Кузнецов",
        "exams": ["Web", "ИС", "История"],
        "marks": [5, 4, 5]
    }
]


def print_students(students):
    print("Имя".ljust(12), "Фамилия".ljust(12), "Экзамены".ljust(30), "Оценки")
    for student in students:
        print(
            student["name"].ljust(12),
            student["surname"].ljust(12),
            str(student["exams"]).ljust(30),
            student["marks"]
        )


def filter_students_by_avg(students, min_avg):
    result = []
    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        if avg > min_avg:
            result.append(student)
    return result


if __name__ == "__main__":
    min_avg = float(input("Введите минимальный средний балл: "))
    filtered = filter_students_by_avg(groupmates, min_avg)

    print("\nСтуденты с средним баллом выше", min_avg)
    print_students(filtered)