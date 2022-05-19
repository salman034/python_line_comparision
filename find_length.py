import math


def find_length(x1, x2, y1, y2):
    length = math.sqrt(math.pow((x2 - x1), 2)) + math.sqrt(math.pow((y2 - y1), 2))
    return length


if __name__ == "__main__":
    line = find_length(5, 6, 15, 21)
    print("The length of line is :{} ".format(line))
