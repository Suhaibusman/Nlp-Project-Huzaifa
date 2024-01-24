import os
import pickle
'''
file_path = 'featurevector.pkl'

# Check if the file exists
if os.path.exists(file_path):
    # Get the file size
    file_size = os.path.getsize(file_path)

    # Check if the file size is greater than 0
    if file_size > 0:
        # File is not empty
        with open(file_path, 'rb') as file:
            content = pickle.load(file)
        print("File is not empty. Content loaded.")
    else:
        print("File is empty.")
else:
    print("File does not exist.")

'''

file_path = 'featurevector.pkl'
file_size = os.path.getsize(file_path)

if file_size == 0:
    print("The file is empty.")
else:
    print('file ok')