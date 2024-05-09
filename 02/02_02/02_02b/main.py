''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''
student_pet_cnt = [0,1,2,3,4,0,3,2,1,0,0,3,2,1,0,0,2]

number_of_students = len(student_pet_cnt)

print(number_of_students)

sum = 0
for count in student_pet_cnt:
  sum = sum + count
print(sum)
print(sum/len(student_pet_cnt))