import os 
file_name = input('Enter file name: ') 
file_size = os.path.getsize(file_name) 
print('The size of the file is',file_size,'bytes')