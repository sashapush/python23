"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
#Solution from professor
# read from questions.txt and append each line into a list
questions = open("questions.txt", "r")  # read from questions.txt
# # read all lines and get rid of line break for each line, then append each stripped line to a list
question_list = [line.strip() for line in questions]
questions.close()
score = 0  # initialize score
total = len(question_list)  # set total score
for line in question_list:
    # split equation with `=` into question and answer
    q, a = line.split("=")
#     # print question and wait for user to input their answer
    answer = input(f"{q}=")
    if answer == a:
        score+=1
#
result = open('result.txt', "w")
result.write(f"Your final score is {score}/{total}.")
result.close()



#3rd version, sligh
# correct_answers = 0
#
# with open("questions.txt", 'r') as file:
#     for count, line in enumerate(file):
#         question = line.split("=")[0]
#         answer = line.split("=")[1].strip()
#
#         user_input = input("{0}=".format(question))
#         if user_input == answer: #compare input with answer
#             correct_answers += 1
#     file.close()
#
# #write results to file
# results_file = open('result.txt', 'w')
# results_file.write(f"Your final score is {correct_answers}/{count+1}")
# results_file.close()

#My second version:
#https://pynative.com/python-count-number-of-lines-in-file/#h-steps-to-get-line-count-in-a-file
correct_answers = 0
# read from `questions.txt`
with open("questions.txt", 'r') as file:
    for count, line in enumerate(file): #enumerate from link above
        question = line.split("=")[0]
        answer = line.split("=")[1].strip()
        user_input = input("{0}=".format(question))  # on udemy f strings are not accepted; Need to use string concatenation or format.
        #user_input = input(f'{line.split("=")[0]}=') #ask for user input; on udemy f strings are not accepted; Need to use string concatenation or format.
        print("Answer " + answer)
        if user_input == answer: #compare input with answer
            correct_answers += 1
    file.close()
    print(f"Score = {correct_answers}/{count+1}")
#write results to file
results_file = open('result.txt', 'w')
results_file.write(f"Your final score is {correct_answers}/{count+1}.")
results_file.close()


#my version
# correct_answers = 0
# questions = open("questions.txt", 'r')
# #total = len(questions.readlines())
# #print(f"Total is {total}")
# # read from `questions.txt`
# for line in questions:
#     #print(line.strip()[-1])
#     user_input = input(f"Please answer the question: {line.strip()[:-1]} ")
#
#     if user_input == line.strip()[-1]:
#         correct_answers += 1
#
# results_file = open('result.txt', 'w')
# results_file.write(f"Your final score is {correct_answers/len(questions)}")
# results_file.close()