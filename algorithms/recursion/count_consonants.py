
"""
Given a string, count the number of consonants.

A consonant is a letter that is not a vowel, 
i.e. letter that is not a,e,i,o, or u

"""


vowels = "aeiou"

input_str = "abc de"
input_str2 = "LuCiDPrograMMiNG"


def iterative_count_consonants(input_str):
    consonant_count = 0
    for i in range(len(input_str)):
        if input_str[i].lower() not in vowels and input_str[i].isalpha():
            consonant_count += 1
    return consonant_count


def recursive_count_consonants(input_str):
    if input_str == '':
        return 0

    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + recursive_count_consonants(input_str[1:])
    else:
        return recursive_count_consonants(input_str[1:])


print(iterative_count_consonants(input_str))
print(recursive_count_consonants(input_str))

print(iterative_count_consonants(input_str2))
print(recursive_count_consonants(input_str2))
