# Implement your function below.
def most_frequent(given_list):
    max_count = -1
    max_item = None

    counter = {}

    for item in given_list:
        if item not in counter:
            counter[item] = 1 # has seen the item for the 1st time
        else:
            counter[item] += 1
        if counter[item] > max_count:
            max_count = counter[item]
            max_item = item

    return max_item

# NOTE: The following input values will be used for testing your solution.
# most_frequent(list1) should return 1
list1 = [1, 3, 1, 3, 2, 1]
# most_frequent(list2) should return 3
list2 = [3, 3, 1, 3, 2, 1]
# most_frequent(list3) should return None
list3 = []
# most_frequent(list4) should return 0
list4 = [0]
# most_frequent(list5) should return -1
list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, -1]

print(most_frequent(list1))
print(most_frequent(list2))
print(most_frequent(list3))
print(most_frequent(list4))
print(most_frequent(list5))
