school_ball = [
	{'school_class': '4a', 'scores': [3,4,4,5,2]},
	{'school_class': '8a', 'scores': [4,5,4,2,2]},
	{'school_class': '9a', 'scores': [4,5,4,2,1]}
]   

def avg_bal_school(school_journal):
	all_ball_school = int(0)
	count_ball_school = int(0)
	for school in school_journal:
		all_ball_school += sum(school['scores'])
		count_ball_school += len(school['scores'])
		summ_ball = 0
		summ_ball += sum(school['scores']) / len (school['scores'])
		number_class = school['school_class']
		print(f'Класс: {number_class} средний балл класса {summ_ball}')
	print('_____________________________________')
	avg_bal_school = all_ball_school / count_ball_school
	print(f'Средняя оценка всей школы: {avg_bal_school}')

shcool_boy = avg_bal_school(school_ball)