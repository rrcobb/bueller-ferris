---
language: python
tags: functions lists sorting
---
#Bueller, Ferris
Today, you're going to use your knowledge of python to help out your teachers.

At the beginning of the semester, the office sends your teacher a list of students, helpfully alphabetized by first name, like this:

```python
['Araceli Tews', 'Astrid Maxson', 'Bessie Myrie', 'Chaya Berryman', 'Cliff Okeefe', 'Deetta Gillian', 'Edmundo Vitolo', 'Gilberte Ragin', 'Gustavo Wethington', 'Howard Luby', 'Lasonya Strong', 'Loreta Gilliard', 'Matt Couchman', 'Merissa Ferro', 'Mickey Turnbough', 'Minnie Curl', 'Raye Cadet', 'Stan Jawad', 'Thao Hinton', 'Werner Paek']
```
But, when your teacher takes attendance, they like to read the names in order by *last name*. They don't want to sort the list by hand, and they don't know enough programming to sort the list themselves. What a conundrum.

Help your teacher re-sort the list of students by last name instead of first name. They need names like "Bueller, Ferris" instead of "Ferris Bueller". In bueller.py, write a function sort_by_last_name that takes a list of names as input and returns the names sorted alphabetically by last name, written "Last, First".

Given the input above, your function should return:
```python
['Berryman, Chaya', 'Cadet, Raye', 'Couchman, Matt', 'Curl, Minnie', 'Ferro, Merissa', 'Gillian, Deetta', 'Gilliard, Loreta', 'Hinton, Thao', 'Jawad, Stan', 'Luby, Howard', 'Maxson, Astrid', 'Myrie, Bessie', 'Okeefe, Cliff', 'Paek, Werner', 'Ragin, Gilberte', 'Strong, Lasonya', 'Tews, Araceli', 'Turnbough, Mickey', 'Vitolo, Edmundo', 'Wethington, Gustavo']
```
### Procedure
1. Download the files
2. In terminal, run the tests with `python bueller_test.py` - at first, there will be an error because the function isn't written.
3. Write your solution in bueller.py
4. Run the tests again, and iterate until you pass

###Bonus Challenges:
 - What should your program do with middle names? What about initials? What about Jr. or III?
 - Make your script more versatile. Instead of just writing a function, it should take the path to a file as an argument on the command line.  You should get the above output for `$python help_teacher.py names.txt`
 - Build your own sorting function - don't use python's built-in sorting.
