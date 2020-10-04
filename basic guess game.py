code_word = "priya"
guess = ""
guess_count= 0
guess_limit= 3
out_of_gusses=False
while guess != code_word and not out_of_gusses :
    if guess_count< guess_limit:
        guess = input("enter guess : ")
        guess_count+=1
    else:
        out_of_gusses=True
if out_of_gusses:
    print("you lose!")
else:
    print("congrats, YOU WIN !")