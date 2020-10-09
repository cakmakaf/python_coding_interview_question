# Given a string, calculate the length of the string.

input_str = "LucidProgramming"
empty_str = ""

# Standard Pythonic way:
# print(len(input_str))

# Iterative length calculation: O(n)


def iterative_str_len(input_str):
    count = 0
    for i in range(len(input_str)):
        count += 1
    return count

# Recursive length calculation: O(n)


def recursive_str_len(input_str):
    if input_str == '':
        return 0
    return 1 + recursive_str_len(input_str[1:])


print(iterative_str_len(input_str))
print(recursive_str_len(input_str))
print(recursive_str_len(empty_str))
