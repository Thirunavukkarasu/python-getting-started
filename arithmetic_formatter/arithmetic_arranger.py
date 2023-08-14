def arithmetic_arranger(problems, solver=False):
    no_of_problems = len(problems)
    if no_of_problems > 5:
        return "Error: Too many problems."

    # pluck the value using map method from problems list
    # and use set for removing the duplicate values
    operations = set(list(map(lambda x: x.split()[1], problems)))
    print(operations)
    if operations != {"+", "-"} and operations != {"+"}:
        return "Error: Operator must be '+' or '-'."

    numbers = []
    for p in problems:
        operand = p.split()
        numbers.extend([operand[0], operand[2]])

    if not all(list(map(lambda x: x.isdigit(), numbers))):
        return "Error: Numbers must only contain digits."

    if not all(list(map(lambda x: len(x) <= 4, numbers))):
        return "Error: Numbers cannot be more than four digits."

    top_row = ""
    bottom_row = ""
    line_row = ""
    result_row = ""
    for problem in problems:
        operands = problem.split(" ")
        first_number, operator, second_number = operands
        sum = 0
        if operator == "+":
            sum = int(first_number) + int(second_number)
        elif operator == "-":
            sum = int(first_number) - int(second_number)

        max_length = max(len(first_number), len(second_number)) + 2
        top = str(first_number).rjust(max_length)
        bottom = operator + str(second_number).rjust(max_length - 1)
        result = str(sum).rjust(max_length)
        line = ""
        for i in range(max_length):
            line += "-"

        if problem != problems[-1]:
            top_row += top + " " * 4
            bottom_row += bottom + " " * 4
            line_row += line + " " * 4
            result_row += result + " " * 4
        else:
            top_row += top
            bottom_row += bottom
            line_row += line
            result_row += result

    operations = ""
    if solver:
        operations = "\n".join([top_row, bottom_row, line_row, result_row])
    else:
        operations = "\n".join([top_row, bottom_row, line_row])
    # print(operations)
    return operations
