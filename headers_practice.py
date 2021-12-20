import requests
import os
import pickle

list = [1, 2, 3, 4, 7, 'ewen', {'a': [1, 2, 3]}]

# open_file = open('pickle_practice', 'wb')

# pickle.dump(list, open_file)

read_file = open('cache1', 'rb')

print(pickle.load(read_file))

# if os.path.isfile('pickle_cache5'):
#     print(True)
# else:
#     print(False)

# open_file = open('pickle_cache5', 'wb')

# pickle.dump([], open_file)

# print(pickle.load(open('pickle_cache5', 'rb')))

# if pickle.load(open('pickle_cache5', 'rb')):
#     print(True)
# else:
#     print(False)




