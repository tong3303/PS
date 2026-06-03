students = [
    ("김철수", 80, 90),
    ("이영희", 95, 85),
    ("박민수", 80, 95),
    ("최지우", 95, 100)
]

students.sort(key = lambda x: (x[1], x[2]), reverse=True)

print(students)

'''
최지우 (95, 100)
이영희 (95, 85)
박민수 (80, 95)
김철수 (80, 90)
'''