
"""
we will be considering the so-called "array advance game". In this game, you are given an array of non-negative integers. For example:

 [3, 3, 1, 0, 2, 0, 1].

Each number represents the maximum you can advance in the array.

Question:
Is it possible to advance from the start of the array to the last element?


"""


def array_advance(A):

    furthest_reached = 0
    last_idx = len(A) - 1
    i = 0
    while i <= furthest_reached and furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, A[i]+i)
        i += 1

    return furthest_reached >= last_idx


# True: Possible to navigate to last index in A:
# Moves: 1,3,2
A = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A))

# False: Not possible to navigate to last index in A:
A1 = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A1))
        



# Object oriented Sltn

class ArrayAdvance(object):
       def canJump(self, A):
           n = len(A)-1
           for i in range(n-1,-1,-1):
               if A[i] + i>=n:
                   n = i
           return n == 0


obj_1 = ArrayAdvance()
print(obj_1.canJump(A))

