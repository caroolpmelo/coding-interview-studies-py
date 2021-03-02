# arrays contains same elements with same order but different indexes?
def is_rotation(A,B): # O(2n) ==> O(n)
    if len(A) != len(B):
        return False

    keyA = A[0]
    keyB = -1

    # tries to find A element in B
    for index in range(len(B)):
        if B[index] == keyA:
            keyB = index

    if keyB == -1:
        return False # didn't find A item in B

    for index in range(len(A)):
        # sums indexes and divide to get B original index reference to A
        # bIndex should say the index where the value is the same as in A
        # ex.: A = [1, 2, 3, 4, 5, 6, 7]; B = [4, 5, 6, 7, 1, 2, 3]
        # A[4] is 5, using as it's below, 5 should be in B[1] (1 is bIndex)
        bIndex = (keyB + index) % len(A)
        if A[index] != B[bIndex]:
            return False # it's a diferent value or position, so it's not rotated

    return True

# NOTE: values for tests
# there're no duplicates
arrayA1 = [1, 2, 3, 4, 5, 6, 7]
arrayB1 = [4, 5, 6, 7, 1, 2, 3]

arrayA2 = [1, 2, 3, 4, 5, 6, 8]
arrayB2 = [4, 5, 6, 7, 1, 2, 3]

arrayA3 = [1, 2, 3, 4, 5, 6, 7]
arrayB3 = [4, 5, 7, 6, 1, 2, 3]

print(is_rotation(arrayA1, arrayB1))
print(is_rotation(arrayA2, arrayB2))
print(is_rotation(arrayA3, arrayB3))
