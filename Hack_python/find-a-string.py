import re


def count_substring(string, sub_string):
    result = 0
    for n in range(len(string) + 1):
        s = string[n:]
        if re.match(sub_string, s):
            result += 1
    return result


if __name__ == '__main__':
    string = input("string: ").strip()
    sub_string = input("sub_string: ").strip()

    count = count_substring(string, sub_string)
    print(count)
