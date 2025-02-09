import time
from binary_tree import BinaryTree 

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

'''
    Original Solution Given
    O(n^2)
'''
# duplicates = [] # Space: O(n)
# for name_1 in names_1: # Time: O(n)
#     for name_2 in names_2: # Time: O(n)
#         if name_1 == name_2:
#             duplicates.append(name_1)

'''
    Solution With Binary Search Tree
    O(nlogn)
'''
# name_tree = BinaryTree()
# for name in names_1:
#     name_tree.insert(name)
# duplicates = []
# for name in names_2:
#     if name_tree.contains(name):
#         duplicates.append(name)

'''
    Solution With Dictionary
    O(n)
'''
name_dict = {} # Space: O(n)
for name in names_1: # Time: O(n)
    name_dict[name] = True
duplicates = [] # Space: O(n)
for name in names_2: # Time: O(n)
    if name_dict.get(name, None):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")