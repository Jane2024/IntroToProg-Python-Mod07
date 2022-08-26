#Title
M.Bruce
Aug 21, 2022
IT FDN 110 (B)
Assignment 07
Link:(GitHub repository)- https://github.com/Jane2024/IntroToProg-Python-Mod07
Link:(GitHub Webpage)-


## Introduction
This week covered reading and writing to text files, reading and writing to binary files using Pickle and error handling with try/except blocks. In addition, learning how to use markdown language to format a GitHub web page. The assignment for the week had us research Pickles in Python and error handling, then create demos to shown these principles in action. This knowledge document will cover the above topics and also be reflected on the newly created GitHub web page.


## Text Files

Read and Write Modes
In Python, we have learned to open a file for read or write:
file = open(file_name, "r"), file = open(file_name, "w"), then
used data= file.read() and file.write(strData +”\n”)  file objects to read and write data from and to text files. 
Then closed the file: file.close().

This would read in all data from a text file or write a string to a text file. There are other options that extend this functionality to perform more specific read/write tasks.

## Append Mode
When opening a file for write in “w” access mode, if there is existing data in a current file, it will be deleted. If opening a file for write, numerous write calls can be done and it will append data as long as the file remains open. Once the file is closed, a new open for write call in “w” access mode will delete the contents and overwrite with new content. Additional access modes allow new data to be appended to existing files. One would be with the append access mode: open(file_name, "a").
