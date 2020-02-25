# this code is NOT fool proof (too lazy to even try), enter the inputs carefully
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
print('your GPA is: %.4f' %gpa_calc(grades, credits, number_of_subjects, total_hours, total_grade))

'''
phy math elec CS eng ob ba
3 3 3 3 2 2 2
'''
