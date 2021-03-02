def common_elements(A,B):
    pA = 0 # pointer in A
    pB = 0 # pointer in B
    result = []

    while pA < len(A) and pB < len(B):
        if A[pA] == B[pB]: # elements match
            result.append(A[pA])
            pA += 1
            pB += 1
        # we do the following below because they are sorted
        elif A[pA] > B[pB]:
            pB += 1 # move pointer only in B
        else: # B[pB] > A[pA]
            pA += 1 # move pointer only in A

    return result

# NOTE: values for tests
# arrays have same lenght
arrayA1 = [1, 3, 4, 6, 7, 9]
arrayB1 = [1, 2, 4, 5, 9, 10]

arrayA2 = [1, 2, 3]
arrayB2 = [4, 5, 6]

print(common_elements(arrayA1, arrayB1))
print(common_elements(arrayA2, arrayB2))
