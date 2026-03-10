#10/03/2026 - watching a video about data structures. theme: stacks

# stack: LIFO - Last-In First-Out. Works like an actual stack where the last item added is the first to get out.
# If you want the first item you need to remove the ones in the top or else it might fall.

# The most common and simple way to use a stack in Python is with a standard list.


def main():

    stack = []

# popping items from stack
    stack.append("A")
    stack.append("B")
    stack.append("C")

    print(f"\nStack of letters: {stack}")

# while stack has items, pop them
    while stack:
        # prints the top item of the stack, the one going to be popped
        print(f"The next item to be popped is: {stack[-1]}")

        popped_item = stack.pop()
        print(f"Item popped: {popped_item}")
        print(f"Stack now: {stack}\n")
        if not stack:
            print("Stack is empty")


main()