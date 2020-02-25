# this code is NOT foolproof (too lazy to even try), enter the inputs carefully
# also, it's not commented, why? cause I -as I mentioned before- am too lazy

def gpa_calc (grades_list, subject_hours, num_of_subs, total_hours, max_grade=100):
	
	total_gpa = []

	for subject in range(num_of_subs):
		sub_gpa = (grades_list[subject]*4)/max_grade
		sub_gpa *= subject_hours[subject]
		total_gpa.append(sub_gpa)
	
	GPA = (sum(total_gpa)/total_hours)
	
	return GPA


number_of_subjects = int(input("enter how many SUBJECTS you toke\n"))
total_hours = int(input("\nenter how many HOURS you toke\n"))
total_grade = int(input('\nenter the total grade (the default is 100 marks)\n'))

grades = input('\nenter your grades seperated by spaces\n')
grades =[int(i) for i in grades.split(" ")]

credits = input("\nenter each subject credit hours seperated by spaces\n")
credits = [int(i) for i in credits.split(" ")]
print('your GPA is: %.3f' %gpa_calc(grades, credits, number_of_subjects, total_hours, total_grade))

'''
example on how the inputs should look like

>>enter how many SUBJECTS you toke
	6
	
>>enter how many HOURS you toke
	15
	
>>enter the total grade (the default is 100 marks)
	100

>>enter your grades seperated by spaces
	100 100 100 100 100 100
	
>>enter each subject credit hours seperated by spaces
	3 3 3 2 2 2
	
>>your GPA is: 4.000

'''
