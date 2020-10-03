"""
Anagram:

Given two strings, check whether two given strings are anagram of each other or not. 
An anagram of a string is another string that contains same characters, only the order 
of characters can be different. For example, “act” and “tac” are anagram of each other.

"""

input_str_1 = "practice makes perfect"
input_str_2 = "perfect makes practice"

input_str_3 = "allergy"
input_str_4 = "allergic"


def is_anagram(s1,s2):
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    if len(s1) != len(s2):
        return False

    s1 = s1.lower()
    s2 = s2.lower()

    alphabet = "abcdefghijklmnopqrstuvxwyz"

    dict_1 = dict.fromkeys(list(alphabet), 0)
    dict_2 = dict.fromkeys(list(alphabet), 0)

    print(dict_1)
    
    
    for i in range(len(s1)):
        dict_1[s1[i]] += 1
        dict_2[s2[i]] += 1

    return dict_1 == dict_2

print(is_anagram(input_str_1, input_str_2))

print(is_anagram(input_str_3, input_str_4))
