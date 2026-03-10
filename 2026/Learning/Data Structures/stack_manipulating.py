# small program that allows user to manipulate a stack by pushing, popping and peeking

# for user to input the option they want and it is validated
def user_decision():
    while True:
        decision = input("Decision: ")
        decision = decision.upper()

        if decision != "V" and decision != "A" and decision != "R" and decision != "Q":
            print("Enter a valid leter")
            continue
        
        return decision

# executes what user asked for in user_decision()
def stack_action(decision, stack):
    if decision == "V":
        if not stack:
            print("Stack is empty")
        else:
            print(f"Your current stack is:\n")
            for item in reversed(stack):
                print(item)

    elif decision == "A":
        item = input("New item: ")
        stack.append(item)

    elif decision == "R":
        if not stack:
            print("Stack already empty.")
        else:
            print("Top item removed.")
            stack.pop()
    
    return stack




# -- main --
def main():
    print("\n--Item stacking--")
    print("Enter V to view your stack. Press A to add an item press R to remove the top item.")
    print("press Q to quit the program.\n")

    user_stack = []
    while True:
        # calls function to ask user what they want to do with the stack
        decision = user_decision()
        if decision == "Q":
            return None

        user_stack = stack_action(decision, user_stack)


main()