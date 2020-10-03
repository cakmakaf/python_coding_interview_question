"""

String Compression: Implement a method to perform basic string compression
using the counts of repeated characters. For example, the string aabcccccaaa
would become a2b1c5a3. If the"compressed" string would not become smaller than
the original string, your method should return the original string. You can
assume the string has only uppercase and lowercase letters (a-z).

"""

input_str_test_1 = "aabcccccaaa"
input_str_test_2 = "aaaaaabbccbcaabb"


def str_comp(inp_str):
    comp_str = ""

    count = 1

    for i in range(len(inp_str) - 1):
        if inp_str[i] == inp_str[i+1]:
            count +=1

        else:
            comp_str += inp_str[i] + str(count)
            count = 1

    comp_str += inp_str[i] + str(count)

    if len(comp_str) >= len(inp_str):
        return inp_str
    else:
        return comp_str


print(str_comp(input_str_test_1))
print(str_comp(input_str_test_2))
