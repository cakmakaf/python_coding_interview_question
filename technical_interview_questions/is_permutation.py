

"""
Given two strings, write a function to decide if one is a permutation
of the other.
"""
# "driving"
# "drivign" <- Permutation.
# "ddriving" <- Not a permutation.
# "riving" <- Not a permutation.
# "criving" <- Not a permutation.

# "the cow jumps over the moon."
# "the moon jumps over the cow." <- Permutation.
# "the cow      jumps over the moon." <- Permutation.


s1 = "driving"
s2 = "drtvign"

def is_permutation(s1, s2):

    # Remove spaces
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    # Check the length of both strings
    if len(s1) != len(s2):
        return False

    for c in s1:
        if c in s2:
            s2 = s2.replace(c, "")

    return len(s2) == 0


print(is_permutation(s1, s2))

    


