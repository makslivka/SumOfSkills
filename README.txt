# SumOfSkills.py

**Version 1.0.0

The code is used to calculate a sum of a chosen skill for chosen year and month for a given data set.


It requires an input in .xlsx format with a number of numerically defined skills at a certain month of a year for different members and locations, e. g.:

| Location | Member | Skill | 2021-01 | 2021-02 | 2021-03 |


## How to use?

Steps:
1. Run SumOfSkills.py
2. Define the location of the file
3. Input the name of a skill, a year and a month
4. Get the answer
5. Choose if you want to specify the calculations (by naming a location (steps 6a-7a) or a member (steps 6b-7b)), choose another skill, year and month (return to step 3) or another file (return to step 2), or to end the program
6a. Specify the location
7a. Get the answer
6b. Specify the member
7b. Get the answer


## Functions within the code

def DataLink():
Used to find the datafile in the system.
    Returns:
        Data taken from an .xlsx file

def MainSum(data):
Used to calculate a sum of a chosen skill for chosen year and month.
    Input:
        Data taken from an .xlsx file

def Mem(data):
Used to calculate a sum of the skill for a chosen member.
    Input:
        Data taken from an .xlsx file
    Returns:
        Position of that member in the column

def Loc(data):
Used to calculate a sum of the skill for a chosen location.
    Input:
        Data taken from an .xlsx file
    Returns:
        Position of that location in the column


## Warnings

File location at step 2 (see: "How to use?") must be defined correctly.


## Copyright

© Maksim Slivka, 18/08/2020
