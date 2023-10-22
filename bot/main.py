class NameNotFoundError(Exception):
    pass

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except NameNotFoundError as name:
            return f"Name \"{name}\" not found"
        
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error        
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        raise(NameNotFoundError(name))


@input_error
def show_phone(args, contacts):
    name = args
    if name in contacts:
        return contacts[name]
    else:
        raise(NameNotFoundError(name))


def show_all(contacts):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    print("Welcome to the assistant bot!")
    contacts = {}
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)
        except KeyboardInterrupt:
            command = "exit"
        
        if command in ["exit", "close"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()