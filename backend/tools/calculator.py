
def tokenize(expression: str) -> list[str]:
    """
    Converts a mathematical expression into a list of tokens.

    Example:
        "20 + 30*5"
        ->
        ["20", "+", "30", "*", "5"]
    """

    tokens = []
    number_buffer = []

    VALID_OPERATORS = {"+", "-", "*", "/", "(", ")"}

    for char in expression:

        # Ignore spaces
        if char.isspace():
            continue

        # Build multi-digit numbers
        if char.isdigit():
            number_buffer.append(char)

        # Operator found
        elif char in VALID_OPERATORS:

            # Save completed number before operator
            if number_buffer:
                tokens.append("".join(number_buffer))
                number_buffer.clear()

            tokens.append(char)

        # Invalid character
        else:
            raise ValueError(f"Invalid character found: '{char}'")

    # Save last number (if any)
    if number_buffer:
        tokens.append("".join(number_buffer))

    return tokens

def validate(tokens: list[str]) -> bool:
    """
    Validates whether the token list forms a valid
    Version-1 mathematical expression.

    Valid:
        20 + 30
        100 * 5
        5 - 2 + 9

    Invalid:
        +20
        20+
        20++30
        20 30
    """

    VALID_OPERATORS = {"+", "-", "*", "/"}

    # Empty expression
    if not tokens:
        return False

    # Expression must end with a number
    if len(tokens) % 2 == 0:
        return False

    for index, token in enumerate(tokens):

        # Even index → Number
        if index % 2 == 0:
            if not token.isdigit():
                return False

        # Odd index → Operator
        else:
            if token not in VALID_OPERATORS:
                return False

    return True


def evaluate(tokens: list[str]):
    """
    Evaluates a validated mathematical expression.

    Version 1:
    - Integer arithmetic only
    - Left-to-right evaluation
    - No operator precedence
    """

    result = int(tokens[0])

    for index in range(1, len(tokens), 2):

        operator = tokens[index]
        number = int(tokens[index + 1])

        if operator == "+":
            result += number

        elif operator == "-":
            result -= number

        elif operator == "*":
            result *= number

        elif operator == "/":

            if number == 0:
                raise ZeroDivisionError("Division by zero.")

            result //= number

    return result


def calculate(expression: str):
    tokens = tokenize(expression)

    if not validate(tokens):
        return {
            "reply": "Invalid mathematical expression."
        }

    answer = evaluate(tokens)

    return {
    "reply": str(answer),
    "prompt_tokens": 0,
    "completion_tokens": 0
}