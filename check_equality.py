import math


def check_equality(x1, x2, y1, y2):
    length = math.sqrt(math.pow((x2 - x1), 2)) + math.sqrt(math.pow((y2 - y1), 2))
    return length


def check_length(length1, length2):
    if length1 == length2:
        return "Both line1 and line2 are equal"
    else:
        return "Both lines are not equal"


if __name__ == "__main__":
    line1 = check_equality(1, 2, 3, 4)
    line2 = check_equality(5, 6, 7, 8)
    result = check_length(line1, line2)
    print(result)