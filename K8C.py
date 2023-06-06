import random

print("Running KopalConsole8")

class ConsoleLanguage:
    def __init__(self):
        self.jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why don't skeletons fight each other? They don't have the guts!",
            "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
            "What did one wall say to the other wall? I'll meet you at the corner!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
        ]
        self.variables = {}

    def execute_command(self, command):
        if command.startswith("<p>"):
            self.print_message(command)
        elif command == "<p<j><p>":
            self.print_joke()
        elif command == "<p<l><p>":
            self.print_commands()
        elif command.startswith("<v<") and command.endswith("<v>"):
            self.create_variable(command)
        elif command.startswith("<p<v<") and command.endswith("<p>"):
            self.print_variable(command)
        elif command == "<q>":
            self.exit_program()

    def print_message(self, message):
        print(message.strip("<p>"))

    def print_joke(self):
        joke = random.choice(self.jokes)
        print(joke)

    def create_variable(self, command):
        variable_name = command.split("<v<")[1].split("<")[0]
        variable_value = command.split("<v<")[1].split("<")[1].strip(">")
        self.variables[variable_name] = variable_value

    def print_variable(self, command):
        variable_name = command.strip("<p<v<").strip("<p>")
        if variable_name in self.variables:
            print(self.variables[variable_name])
        else:
            print(f"Variable '{variable_name}' not found.")

    def print_commands(self):
        print("Available commands:")
        print("<p>Hello<p> - Print a message")
        print("<p<j><p> - Print a random joke")
        print("<p<l><p> - Print available commands")
        print("<v<variable_name<value<v> - Declare a variable")
        print("<p<v<variable_name<p> - Print the value of a variable")
        print("<q> - Quit the console")

    def exit_program(self):
        print("Exiting the console...")
        exit()


def main():
    console = ConsoleLanguage()

    while True:
        user_input = input("Enter a command: ")
        console.execute_command(user_input)


if __name__ == '__main__':
    main()
