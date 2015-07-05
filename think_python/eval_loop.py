# Write a function called eval_loop that iteratively prompts the user, takes the resulting input and
# evaluates it using eval, and prints the result.
# It should continue until the user enters 'done', and then return the value of the last expression it
# evaluated.
answer = 0
def eval_loop():
    global answer

    while True:
        text = input("Enter done when finished\n")
        print(text)
        if text == "done":
            break
        answer = eval(text)
        print(answer)
eval_loop()
print("Thank you. Your last result is ", answer)

