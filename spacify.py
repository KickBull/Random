

def spacify(input_equation: str) -> str:
    """Mathematical equation space fixer.
    Example:

    input: 4- (3 /2)*-16^ 12 -1*(+13)
    output: 4 - (3 / 2) * -16^12 - 1 * (+13)
    """

    buffer = ""
    operators = ["+", "-", "*", "/", "^"]
    output = ""

    for char in list(input_equation):
        if len(buffer + char) <= 2:
            buffer += char
        else:
            buffer = buffer[1]
            buffer += char

        if len(buffer) > 1:
            if buffer[1] in operators:
                if buffer[1] in ("+", "-") and not output[-1].isdigit() and output[-1] != ")" or buffer[1] == "^":
                    output += buffer[1]
                else:
                    output += f" {buffer[1]} "
            elif buffer[1] == " ":
                pass
            else:
                output += buffer[1]
        else:
            output = buffer[0]

    return output
