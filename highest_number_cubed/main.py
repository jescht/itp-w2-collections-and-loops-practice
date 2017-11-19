def highest_number_cubed(limit):
    cubedList =[]                   #creates empty list "cubedList"
    for i in range (1,limit):       #adds every cube number from 1 until limit to list
        if i**3 < limit:
            cubedList.append(i)
    return cubedList[-1]            #returns the last number (highest cube) on cubedList. Can add .sort() to ensure list sorted lowest to highest.
    

def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
