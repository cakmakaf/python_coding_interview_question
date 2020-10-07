"""
Ex: 242

242 / 2 = 121 r -> 0
121 / 2 = 60 r -> 1
60 / 2 = 30 r -> 0
30 / 2 = 15 r -> 0
15 / 2 = 7 r -> 1
7 / 2 = 3 r -> 1
3 / 2 = 1 r -> 1
1 / 2 = 0 r -> 1

242 = (11110010)_2

"""
from stack import Stack

def div_by_2(dec_num):
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

print(div_by_2(242))
print(div_by_2(5698746523049948))
