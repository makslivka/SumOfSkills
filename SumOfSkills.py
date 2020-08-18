
import pandas as pd

def DataLink():
    """ Used to find the datafile in the system.
    Returns:
        Data taken from an .xlsx file"""
    
    LocationIn = input('Enter the location of the file (format: C:\\Users\\...\\File_Name.xlsx)\n')
    data = pd.read_excel(LocationIn)
    MainSum(data)

#--------------------------------------------------------------
    
def MainSum(data):
    """ Used to calculate a sum of a chosen skill for chosen year and month.
    Input:
        Data taken from an .xlsx file"""

    i = 0
    while i == 0:
        SkillIn = input('Enter the skill: ') 
        Skill = data['Skill'].str.find(SkillIn)+1
        i = Skill.sum()
        if i == 0:
            print('The skill wasn\'t found')
    
    while True:
        try:
            while True:
                try:
                    Year = input('Enter the year: ') 
                    Month = input('Enter the month: ') 
                    DateIn = '01-' + Month + '-' + Year + ' 00:00:00'
                    DateInpd = pd.to_datetime([DateIn], dayfirst=True)
                except ValueError:
                    print('\nAn error occured defining the date.')
                    print('The year should be digital (e.g. 2021, 21, etc.)')
                    print('The month should be in standard format (e.g. January, jan, 01, etc.)')
                    continue
                else:
                    break
            Date = data[DateInpd]
            Sum = Date.loc[Skill == 1].sum()
        except KeyError:
            print('\nThe given date is out of range')
            continue
        else:
            break
    
    input('The sum for this skill in that month and year: \n' + str(round(Sum[0], 4)))
    

    while True:
        print('\nIf you want to specify a location for this skill and date, enter 1')
        print('If you want to specify a member for this skill and date, enter 2')
        print('If you want to calculate another skill and date combination for this data, enter 3')
        print('If you want to use another set of data, enter 4')
        print('If you want to finish, enter 0')
        Q = input('Choose a scenario: ')
        if Q == '1':
            Location = Loc(data)
            SumMem = Date.loc[Skill == 1].loc[Location == 1].sum()
            input('The skill of this location: \n' + str(round(SumMem[0], 4)))
        elif Q == '2':
            Member = Mem(data)
            SumMem = Date.loc[Skill == 1].loc[Member == 1].sum()
            input('The skill of this member: \n' + str(round(SumMem[0], 4)))
        elif Q == '3':
            MainSum(data)
            break
        elif Q == '4':
            DataLink()
            break
        elif Q == '0':
            break

#--------------------------------------------------------------
    
def Mem(data):
    """ Used to calculate a sum of the skill for a chosen member.
    Input:
        Data taken from an .xlsx file
    Returns:
        Position of that member in the column"""
    
    i = 0
    while i == 0:
        MemberIn = input('Enter a member\'s name: ') 
        Member = data['Member'].str.find(MemberIn)+1
        i = Member.sum()
        if i == 0:
            print('The member wasn\'t found')
    return Member

#--------------------------------------------------------------

def Loc(data):
    """ Used to calculate a sum of the skill for a chosen location.
    Input:
        Data taken from an .xlsx file
    Returns:
        Position of that location in the column"""
    
    i = 0
    while i == 0:
        LocationIn = input('Enter a location: ') 
        Location = data['Location'].str.find(LocationIn)+1
        i = Location.sum()
        if i == 0:
            print('The location wasn\'t found')
    return Location

#--------------------------------------------------------------
    
DataLink()



