
with open('questions.txt', 'r') as f:
	file = f.read().split('\n')

	questions = []

	# Cleaning up questions file
	for i, line in enumerate(file):
		questions.append(line.split('|'))

	for i, question in enumerate(questions):
		for j, part in enumerate(question):
			questions[i][j] = questions[i][j].strip()

def getQuestionFunction(number):
	if len(questions) < number:
		return {'Invalid Data': f'Max question is {len(questions)}'}


	question = questions[number-1]

	data = {
		'question': question[0],
		'choices': question[1:-1],
		'answer': question[-1]
	}

	return data;
