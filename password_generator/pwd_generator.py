import random, string

def create_password(length):
    """ args: length of password to create (at least 5) """

    # initialize characters
    LOWER = string.ascii_lowercase
    UPPER = string.ascii_uppercase
    DIGITS = string.digits
    PUCTUATIONS = string.punctuation

    chars = (LOWER, UPPER, DIGITS, PUCTUATIONS)

    # initialize password to create
    pwd = []

    if length < 5:
        print("Length of password must be at least 5.")
    else:
        while len(pwd) < length:
            # choose a character randomly from lower, upper, digit and punctuation
            n = random.randint(0, len(chars) - 1)
            c = chars[n]
            i = random.randint(0, len(c) - 1)
            pwd.append(c[i])

    return ''.join(pwd)

if __name__ == "__main__":
    while True:
        print("*" * 20)
        print("Commands:")
        print("q: quit")
        print("p: create a new password")
        print("*" * 20)
        cmd = input(":")
        if cmd == 'q':
            break
        if cmd == 'p':
            try:
                num = int(input("Enter a number. It must be greater than or equal to 5:\n"))
                if num < 5:
                    print("Length of password must be at least 5.")
                else:
                    created_pwd = create_password(num)
                    print("Your password is: {}".format(created_pwd))
            except ValueError:
                print("Invalid input. Try again...")
