'''The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.'''
def average_marks(student_marks, query_name):
    marks = student_marks[query_name]
    average = sum(marks) / len(marks)
    print("{:.2f}".format(average))

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    average_marks(student_marks, query_name)