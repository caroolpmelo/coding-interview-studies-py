# Implement your function below.
def non_repeating(given_string):
    char_count = {}

    for item in given_string:
        if item not in char_count:
            char_count[item] = 1
        else: 
            char_count[item] += 1
    
    for item in given_string:
        if char_count[item] == 1:
            return item

    return None

# NOTE: The following input values will be used for testing your solution.
print(non_repeating("abcab")) # should return 'c'
print(non_repeating("abab")) # should return None
print(non_repeating("aabbbc")) # should return 'c'
print(non_repeating("aabbdbc")) # should return 'd'
