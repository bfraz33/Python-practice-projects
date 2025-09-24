Questions = {
    1:{"What character do you use to comment a line in Python?":"#"},
    2:{"Do endents matter in Python?":"Yes"},
    3:{"What is the extension for puython files?":".py"}
}

def show_questions():
    print("There are", len(Questions), "questions in this quiz.")

def Quiz():
    input("Please hit Emter to start:")
    for qnum, qdict in Questions.items():
        for question, answers in qdict.items():
            user_answer = input(f"{qnum}. {question}")
            if user_answer.strip().lower() == answers.strip().lower():
                print("Correct!✅")          
            else:
                print("Wrong❌")
                
if __name__=="__main__":
    show_questions()
    Quiz()     
