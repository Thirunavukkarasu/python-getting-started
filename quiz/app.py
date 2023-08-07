from Question import Question

question_prompts = [
    "What is your favourite frontend framework/library?\n (a) Angular\n (b) Vue\n (c) React\n\n",
    "What is your favourite SSR framework/library?\n (a) RemixJS\n (b) NextJS\n (c) Other\n\n",
    "What is your favourite CSS framework/library?\n (a) Bootstrap\n (b) Chakara\n (c) TailwindCSS\n\n",
 ]

questions = [
    Question(question_prompts[0],"c"),
    Question(question_prompts[1],"b"),
    Question(question_prompts[2],"c"),
]

def test_score():
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if(answer == question.answer):
            score = score+1
    
    print("You got " + str(score) + "/" + str(len(questions))+" correct!")

test_score()
