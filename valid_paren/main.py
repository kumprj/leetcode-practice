
def main():
    s = "(())"
    my_stack = [] # check data type
    for item in s[::1]:
        if item == "(" or item == "{" or item == "[":
            my_stack.append(item) # get proper syntax for pushing to stack
        else:
            my_stack.pop() # remove from stack, maybe check if it equals the type that went in?
    
    print(my_stack) # if my_stack is empty, this is a success.
    if not my_stack:
        print('Valid Paren')
    else:
        print('Not Valid Paren')


if __name__ == "__main__":
    main()
