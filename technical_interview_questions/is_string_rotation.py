# String Rotation: Given two strings, s1 and s2, write code to check if s2 is
# a rotation of s1 (e.g. "waterbottle" is a rotation of "erbottlewat")

import string

test_rot_str_1 = "waterbottle"
test_rot_str_2 = "erbottlewat"

test_rot_str_3 = "watertables"
test_rot_str_4 = "erbottlewat"


import string

def is_str_rotation(s1, s2):

    if len(s1) != len(s2):
        return False

    s1 = s1.lower()
    s2 = s2.lower()

    # Use a hash table

    dict_1 = dict.fromkeys(list(string.ascii_lowercase), 0)
    dict_2 = dict.fromkeys(list(string.ascii_lowercase), 0)

    for i in range(len(s1)):
        dict_1[s1[i]] += 1
        dict_2[s2[i]] += 1

    return dict_1 == dict_2


print(is_str_rotation(test_rot_str_1,test_rot_str_1))

print(is_str_rotation(test_rot_str_3, test_rot_str_4))
