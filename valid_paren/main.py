
def main():
    print(isValid("[[][[]"))


# Need to solve the pop, it cant pop on any of the 'end' - it needs to match.
def isValid(s: str) -> bool:
    stack = list()
    for item in s[::1]:
        if item == "(": stack.append(")")
        elif item == "[": stack.append("]")
        elif item == "{": stack.append("}")
        else:
            if not stack:
                return False
            if stack.pop() != item:
                return False
            
    return True if not stack else False
if __name__ == "__main__":
    main()
