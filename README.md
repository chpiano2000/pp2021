USTH ICT 2021 Advanced Programming with Python
=====================================================

Students are expected to:
* Fork this repository to your github account
* Push your commits regularly, with **proper** commit messages


Student Info
=========================

* Student Name: Vo Chi Dat
* Student ID: BI9-066


# Practice Session
## Labwork 1: Student mark managemet
1. Make a new Python program:
    * Name it «1.student.mark.py»
    * Use tuples, dicts, lists, NO objects/classes
    * Build a student mark management system
2. Function:
    2.1. Input Functions:
        * Input number of students in a class
        * Input student information: id, name, DoB
        * Input number of courses
        * Input course information: id, name
        * Select a course, input marks for student in this course
    2.2. Listing functions:
        * List courses
        * List students
        * Show student marks for a given course
## Labwork 2: OOP'ed student mark management
1. Copy your practical work 1 to 2.student.mark.oop.py
2. Make it OOP’ed
3. Same functions
    * Proper attributes and methods
    * Proper encapsulation
    * Proper polymorphism
## Labwork 3: Some maths and decorations
1. Copy your practical work 2 to 3.student.mark.oop.math.py
2. Use math module to round-down student scores to 1-digit decimal upon input, floor()
3. Use numpy module and its array to:
    * Add function to calculate average GPA for a given student
    * Sort student list by GPA descending
4. Decorate your UI with curses module
## Labwork 4: modularization
Split your program 3.student.mark.oop.math.py to modules and packages in a new pw4 directory
    * input.py: module for input
    * output.py: module for curses output
    * domains: package for classes
    * main.py: main script for coordination
## Labwork 5: persistent info
1. Copy your pw4 directory into pw5 directory
2. Update your input functions
    * Write student info to students.txt after finishing input
    * Write course info to courses.txt after finishing input
    * Write marks to marks.txt after finishing input
3. Before closing your program
    * Select a compression method
    * Compress all files aboves into students.dat
4. Upon starting your program
    * Check if students.dat exists
    * If yes, decompress and load data from it
## Labwork 6: pickled management system
1. Copy your pw5 directory into pw6 directory
2. Upgrade the persistence feature of your system to use pickle instead, still with compression
 