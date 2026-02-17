userInput = "dog"

match userInput:
    case "dog":
        print("Bark")
    case "cat":
        print("Meow")
    case "cow":
        print("Moo")
    case _:
        print("got unknown value")