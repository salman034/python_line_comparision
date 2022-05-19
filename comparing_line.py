import math


def comparing_line(x1, x2, y1, y2):
    length = math.sqrt(math.pow((x2 - x1), 2)) + math.sqrt(math.pow((y2 - y1), 2))
    return length


def check_length(length1, length2):
    if length1 == length2:
        return "Both the lines are equal"
    elif length1 > length2:
        return "line1 is greater then line2"
    elif length1 < length2:
        return "line1 is smaller then line2"


if __name__ == "__main__":
    line1 = comparing_line(1, 2, 3, 4)
    line2 = comparing_line(5, 6, 7, 10)
    print("The length of line1 is :{} ".format(line1))
    print("The length of line2 is :{} ".format(line2))
    result = check_length(line1, line2)
    print(result)
