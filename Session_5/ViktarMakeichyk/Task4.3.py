# Task 4.3
# File data/students.csv stores information about students in CSV format. This file contains the student’s names,
# age and average mark.

# 1. Implement a function which receives file path and returns names of top performer students
# def get_top_performers(file_path, number_of_top_students=5):
#    pass

# print(get_top_performers("students.csv"))
# >>> ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']

# 2. Implement a function which receives the file path with students info and writes CSV student information to the
# new file in descending order of age. Result:
# student name,age,average mark
# Verdell Crawford,30,8.86
# Brenda Silva,30,7.53
# ...
# Lindsey Cummings,18,6.88
# Raymond Soileau,18,7.


import csv


def get_top_performers(file_path, number_of_top_students=5):

    with open(file_path, "r") as csv_students_file:
        students_data = list(csv.reader(csv_students_file, delimiter=","))
    students_data = sorted(students_data[1:], key=lambda x: float(x[2]), reverse=True)
    return list(students_data[:number_of_top_students][i][0] for i in range(number_of_top_students))


def export_csv(file_path):
    with open(file_path, "r") as csv_students_data:
        students_data = list(csv.reader(csv_students_data, delimiter=","))

    with open("students_ordered_by_age.csv", "w", newline="") as file_out:
        data_holder = csv.writer(file_out)
        data_holder.writerow((students_data[0]))
        students_data = sorted(students_data[1:], key=lambda x: float(x[1]), reverse=True)

        for line in students_data:
            data_holder.writerow(line)


print(get_top_performers("data/students.csv"))
export_csv("data/students.csv")
