grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny' , 'Bilbo' , 'Steve' , 'Khendrik' , 'Aaron'}
#print(grades)
#print(students)
#print(len(grades[0]))
#print(sum(grades[0]))
#print((sum(grades[0]))/(len(grades[0])))
students = list(students)
#print(students.sort())
#print(students)
students.sort()
#print({students[0] : grades[0]})
average_grades = [((sum(grades[0]))/(len(grades[0]))) , ((sum(grades[1]))/(len(grades[1]))) , ((sum(grades[2]))/(len(grades[2]))),((sum(grades[3]))/(len(grades[3]))) , ((sum(grades[4]))/(len(grades[4])))]
#print(average_grades)
rating_log = {students[0] : average_grades[0] , students[1] : average_grades[1] , students[2] : average_grades[2] , students[3] : average_grades[3] , students[4] : average_grades[4]}
print(rating_log)