# Given the names and grades for each student in a class of students,
# store them in a nested list and print the name(s) of any student(s)
# having the second lowest grade.
#
# Note: If there are multiple students with the second lowest grade,
# order their names alphabetically and print each name on a new line.
#
# Constraints:
# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.
#
# There are students in this class whose names and grades are assembled to build the following list:
# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#
# The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry,
# so we order their names alphabetically and print each name on a new line.
#
# would print:
# Berry
# Harry
#

# sort student records by student score and identify the student(s) with second lowest scores
def second_lowest_score(student_names):

        # sort by the student score, with student(s) with the lowest score in ascending order
        student_names.sort(key = lambda l: l[1])

        # check to see which is second lowest score, must return all students that have second
        # lowest score
        # second_lscore_student[0] is names
        # second_lscore_student[1] is score
        # get the item in the list that has the name and score of 2nd lowest record
        second_lscore_student = student_names[1]

        # create a list of all the students that have the 2nd lowest score
        all_low_names = [name for name,score in student_names if score == second_lscore_student[1]]

        return(all_low_names)


# outer list
student_records = []

if __name__ == '__main__':
    # the for loop input is to enter the number of students that will be processed
    for _ in range(int(input())):

        # inner list
        one_student = []

        # input student name and append to inner list
        name = input()
        one_student.append(name)

        # input student score and append to inner list
        score = float(input())
        one_student.append(score)

        # append inner list (one_student) to outer list (student_records)
        student_records.append(one_student)

    # get student(s) with second lowest score
    students_2nd_lowest_score = second_lowest_score(student_records)

    # constraint of at least one or more students with lowest score
    num_students_lowest = (len(students_2nd_lowest_score))

    if (num_students_lowest >= 1 and num_students_lowest <= 5):
        # use print '\n'.join(students_2nd_lowest_score) so each entry in the list is printed
        # on a separate line
        print('\n'.join(students_2nd_lowest_score))
    else:
        print("Have constraint of at least 1 student with 2nd lowest score but not more than 5.")
