from data import question_answers



def question_unit(input_question_list, current_question):

    choice = input_question_list[current_question]

    print(f"{current_question}\nSelect from these options: \n")


    

    for item in choice[0]:
        print(f"{item}")

    is_answer_option = False
    while is_answer_option == False:
        answer = input()
        if answer not in choice[0]:
            print("Not an answer. Try again")
        else:
            is_answer_option = True


    return answer, choice[choice[0].index(answer) + 1]





def flowchart(input_question_list, current_question):
    
    run = question_unit(input_question_list, current_question)

    if run[1] != "END":
        
        flowchart(input_question_list, run[1])
    else:
        print("END OF QUESTION LINE")

    return


'''test = question_unit(question_answers, "This is Question A")

print(test)'''

test = flowchart(question_answers, "This is Question A")

print(test)