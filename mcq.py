from question import Question
question_prompt = [
    "what is my name?\n (a)james\n (b) devil\n (c)evildad\n\n",
    "who is my friend?\n (a) a dog\n (b)a cat\n (c) a human \n\n",
    "what is the capital of india ?\n (a)chicago\n (b)paris\n (c)delhi\n\n",
    ]
questions = [
    Question(question_prompt[0], "c"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "c"),

]
def run_test(questions) :
    score = 0
    for question in questions :
        answer = input(question.prompt)
        if answer == question.answer :
            score += 1
    print("you got :"  + str(score) + "/" +   str(len(questions)) + "correct")

run_test(questions)