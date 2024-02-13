class NegativeAgeError(Exception):
    pass


#Begin Conversation
name = input("Enter your name:")
print("Hello", name, "How are you today?")

while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise NegativeAgeError()
        break
    except ValueError:
        print("Hey! That wasn't a valid integer. Try Again! \n")
    except EOFError:
        print("Hey! You can't break out of the program now!")
    except KeyboardInterrupt:
        print("Okay, whatever I'm bailing. Have a default value 12")
        age = 12
        break
    except NegativeAgeError:
        print("You can't be negative age stupid duck")

print("Wow! That's old. I'm only", age//2)