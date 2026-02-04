a = 2

match a:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case "a":
        print("a")
    case (1,2):
        print("(1,2)")
    case _:
        print("Other stuff")

a = "a"

match a:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case "a":
        print("a")
    case (1,2):
        print("(1,2)")
    case _:
        print("Other stuff")

a = (1,2)

match a:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case "a":
        print("a")
    case (1,2):
        print("(1,2)")
    case _:
        print("Other stuff")

a = 10.0

match a:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case "a":
        print("a")
    case (1,2):
        print("(1,2)")
    case _:
        print("Other stuff")