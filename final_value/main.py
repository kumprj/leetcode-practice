# There is a programming language with only four operations and one variable X:

#     ++X and X++ increments the value of the variable X by 1.
#     --X and X-- decrements the value of the variable X by 1.

# Initially, the value of X is 0.

# Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.


def main():
    # operations = ["--X","X++","X++"]
    operations = ["++X","++X","X++"]
    X = 0
    for op in operations:
        if '--' in op:
            X -=1
        elif '++' in op:
            X += 1

    print(X)

    pass
if __name__ == "__main__":
    main()