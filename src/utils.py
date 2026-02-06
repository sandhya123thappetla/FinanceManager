def get_input(message):
    value = input(message).strip()
    if value == "":
        print("Invalid input!")
        return None
    return value
