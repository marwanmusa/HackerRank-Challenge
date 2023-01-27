from datetime import date

"""
Task:
    Your local library needs your help! Given the expected and actual return dates for a library book,
    create a program that calculates the fine (if any). The fee structure is as follows:

    1. If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0).
    2. If the book is returned after the expected return day but still within the same calendar month and year
       as the expected return date, fine = 15 Hackos * (the number of days late).
    3. If the book is returned after the expected return month but still within the same calendar year
       as the expected return date, the fine = 500 Hackos * (the number of months late).
    4. If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos.
"""

date_returned = input()
date_due = input()

def calculate_fine(a, b):
    ret = a.split()
    due = b.split()

    fine = int()
    fixed_fine = 10000

    dR = date(int(ret[2]), int(ret[1]), int(ret[0]))
    dD = date(int(due[2]), int(due[1]), int(due[0]))

    if a == b:
        return 0
    else:
        if dR.year == dD.year:
            if dR.month > dD.month:
                fine = 500*(dR.month-dD.month)
            elif dR.day > dD.day:
                fine = 15*(dR.day-dD.day)
        elif dR.year < dD.year:
            return 0
        else:
            return fixed_fine
    return fine

print(calculate_fine(date_returned, date_due))