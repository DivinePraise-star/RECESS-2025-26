#File handling
#file handling is a way to store data in a file and retrieve it when needed. In Python, we can use the built-in open() function to open a file and perform various operations on it.    

##There are different modes in which we can open a file:
#1. 'r' - Read mode: This is the default mode. It opens a file for reading. If the file does not exist, it raises a FileNotFoundError.
#2. 'w' - Write mode: It opens a file for writing. If the   file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.
#3. 'a' - Append mode: It opens a file for appending. If the file does not exist, it creates a new file. The data is added to the end of the file.
#4. 'x' - Exclusive creation mode: It creates a new file and opens it for writing. If the file already exists, it raises a FileExistsError. 
#5. 'b' - Binary mode: It opens a file in binary mode. This is used for non-text files such as images or audio files.   
#6. 't' - Text mode: It opens a file in text mode. This is the default mode and is used for text files. 
#7. '+' - Read and write mode: It opens a file for both reading and writing. If the file does not exist, it creates a new file. 

#Common files:
#Text files: These files contain plain text and can be opened in read or write mode. They usually have a .txt extension.
#Binary files: These files contain data in binary format and can be opened in read or write mode. They usually have a .bin extension.            
#csv files: These files contain comma-separated values and can be opened in read or write mode. They usually have a .csv extension.     
#json files: These files contain data in JSON format and can be opened in read or write mode. They usually have a .json extension.  
#excel files: These files contain data in Excel format and can be opened in read or write mode. They usually have a .xlsx extension.    

#file handling operations:
#1. Reading a file: We can read the contents of a file using the read() method. It reads the entire file and returns it as a string. We can also use the readline() method to read a single line from the file or the readlines() method to read all the lines in the file and return them as a list of strings.                                                
#2. Writing to a file: We can write data to a file using the write() method. It writes the specified string to the file. We can also use the writelines() method to write a list of strings to the file.        
#3. Closing a file: It is important to close a file after we are done with it to free up system resources. We can use the close() method to close a file. Alternatively, we can use the with statement to automatically close the file after the block of code is executed. 
##4. Deleting a file: We can delete a file using the os module. We can use the os.remove() method to delete a file. We can also use the os.rmdir() method to delete an empty directory or the shutil.rmtree() method to delete a directory and its contents.
#5. opening a file in binary mode: We can open a file in binary mode by adding 'b' to the mode. For example, 'rb' opens a file for reading in binary mode and 'wb' opens a file for writing in binary mode. This is useful when working with non-text files such as images or audio files.  
#6. Checking if a file exists: We can check if a file exists using the os.path module. We can use the os.path.exists() method to check if a file or directory exists. We can also use the os.path.isfile() method to check if a path is a file and the os.path.isdir() method to check if a path is a directory.    
#7. Renaming a file: We can rename a file using the os module. We can use the os.rename() method to rename a file or directory. 

#SYNTAX:
#file = open('filename', 'mode')
#file.close()
#file = read('filename')
#file = write('filename', 'data')
#file = append('filename', 'data')
#file = delete('filename')
#file = rename('old_filename', 'new_filename')
#file = check_exists('filename')
#file = check_isfile('filename')
#file = check_isdir('directoryname')

#Examples:
from pathlib import Path

student_file = Path(__file__).with_name('student.txt')

#Reading a file:
with open(student_file, 'r') as file:
    content = file.read()
    print(content)

#. Reading a file:
file = open(student_file, 'r')
content = file.read()
print(content)
file.close()    

#Reading a file using with statement:
with open(student_file, 'r') as file:
    content = file.read()
    print(content)

#Reading a file line by line:
file = open(student_file, 'r') 
print(file.readline())
print(file.readline())

#Reading a file line by line using a loop:
with open(student_file, 'r') as file:
    for line in file:
        print(line.strip()) 

#2. Writing to a file:
file = open('my_file.txt', 'w')
file.write('Hello, this is a test file.')
file.close()

#Write/create a file with content"i love pyhton programming" in the first line and "i love data science" in the second line. Save the file as report.txt
file = open('report.txt', 'w')
file.write('I love python programming\n')
file.write('I love data science')
file.close()

#using with statement to write to a file:
with open('report.txt', 'w') as file:
    file.write('I love python programming\n')
    file.write('I love data science')   

#appending to a file:
file = open('report.txt', 'a')
file.write('\nI love machine learning')
file.close()    

#using with statement to append to a file:
with open('report.txt', 'a') as file:
    file.write('\nI love machine learning') 


#Real-life example of file handling:
#1. Storing user data: We can use file handling to store user data such as login credentials, preferences, and settings in a file. This allows us to retrieve the data when needed and provide a personalized experience to the user.
#2. Logging: We can use file handling to log events and errors in a file. This allows us to track the behavior of our application and identify issues when they arise.  
#3. Data analysis: We can use file handling to read and write data in various formats such as CSV, JSON, and Excel. This allows us to analyze the data and generate insights that can be used to make informed decisions.
#4. Configuration files: We can use file handling to read and write configuration files that contain settings and parameters for our application. This allows us to easily modify the behavior of our application without changing the code.    
#5. Backup and restore: We can use file handling to create backups of important files and restore them when needed. This allows us to protect our data from loss or corruption. 

#Attendance management system: We can use file handling to create an attendance management system that stores the attendance records of students in a file. This allows us to easily track the attendance of students and generate reports when needed. 
file = open('attendance.txt', 'w')
file.write('Name,Date,Status\n') 
#save the attendance records of students in the file
file.write('John,2023-01-01,Present\n')
#
print('Attendance records saved successfully.')   
file.close()

#CSV file handling: We can use the csv module in Python to read and write CSV files. This allows us to easily work with tabular data and perform various operations on it.
import csv
#how do use csv files.
#syntax:
#file = open('filename.csv', 'mode')
#file = csv.reader(file)
#file = csv.writer(file)
#file = csv.DictReader(file)
#file = csv.DictWriter(file, fieldnames=['field1', 'field2', 'field3'])

#reading a csv file:
with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#writing to a csv file:
with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'Grade'])
    writer.writerow(['John', 20, 'A'])
    writer.writerow(['Jane', 21, 'B'])
    writer.writerow(['Jim', 22, 'C'])

#add my registration number, name, age, gender, course and score to the csv file using a dictionary.
with open('students.csv', 'a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Registration Number', 'Name', 'Age', 'Gender', 'Course', 'Score'])
    writer.writerow({'Registration Number': 'S12345', 'Name': 'Tendo', 'Age': 20, 'Gender': 'Male', 'Course': 'Computer Science', 'Score': 85})


#using json files: We can use the json module in Python to read and write JSON files. This allows us to easily work with structured data and perform various operations on it. 
#What is json file: JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate. It is commonly used for transmitting data between a server and a web application as an alternative to XML. JSON files have a .json extension and contain data in key-value pairs, similar to a Python dictionary. 
#fromat of json file:
#{
#   "key1": "value1",
#    "key2": "value2",   
#    "key3": {
#        "subkey1": "subvalue1",    
#        "subkey2": "subvalue2"
#    }
#}

#syntax:
#with open('filename.json', 'r') as file:
#    data = json.load(file)
#with open('filename.json', 'w') as file:
#    json.dump(data, file, indent=4)
#file = open('filename.json', 'r')
#file = open('filename.json', 'w')

#Example of a json file:
import json

People = [
    {
        "name": "John",
        "age": 30,
        "city": "New York"
    },
    {
        "name": "Jane",
        "age": 25,
        "city": "Los Angeles"
    },
    {
        "name": "Jim",
        "age": 22,
        "city": "Chicago"
    },
    {
        "name": "Jill",
        "age": 28,
        "city": "Houston"
    },
    {
        "name": "Jack",
        "age": 35,
        "city": "Phoenix"
    },
    {
        "name": "Jenny",
        "age": 27,
        "city": "Philadelphia"
    },
    {
        "name": "Joe",
        "age": 32,
        "city": "San Antonio"
    },
    {
        "name": "Jessica",
        "age": 29,
        "city": "San Diego"
    },
    {
        "name": "Jordan",
        "age": 31,
        "city": "Dallas"
    },
    {
        "name": "Jasmine",
        "age": 26,
        "city": "San Jose"
    }
]

with open('data.json', 'w') as file:
    json.dump(People, file)

print('Data saved to data.json successfully.')    

#Data Serialization: We can use the pickle module in Python to serialize and deserialize Python objects. 
# This allows us to easily save and load complex data structures such as lists, dictionaries, and custom objects.
# 
# How to use pickle module:
# Syntax:
# import pickle
# # Saving an object to a file:
# with open('filename.pkl', 'wb') as file:
#   pickle.dump(object, file)
# # # Loading an object from a file:
# with open('filename.pkl', 'rb') as file:    
#     object = pickle.load(file)

#Example of using pickle module:
import pickle

data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Saving data to a file
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Loading data from a file
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
