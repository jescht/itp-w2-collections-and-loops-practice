def create_box(height, width, character):
    if height>=1 and width>=1:
        box=""
        for j in range(width):
            box +=(str(character))
        return (box + "\n")*height

#create a box with outer border only
def create_hollow_box(height, width,character):                         
  newLine=""
  for i in range(height):
      if i == 0 or i == height-1:                                   #creates the first and last line of the box
        newLine+= (width*character) + "\n" 
      else: 
        newLine+= (character + " "*(width-2) + character) + "\n"    #creates the hollow space in between two borders
  return newLine

# Tests:

first_box_expected = """
****
****
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()


first_hollow_box_expected = """
****
*  *
****
""".lstrip()

second_hollow_box_expected = """
@
""".lstrip()

third_hollow_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
x                      x
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()

def test_first_box():
    assert create_box(3, 4, '*') == first_box_expected


def test_second_box():
    assert create_box(1, 1, '@') == second_box_expected

# Write your own test using the `third_box_expected` box
def test_third_box():
    assert create_box(3, 24, 'x') == third_box_expected
    
#tests for hollow box    
def test_first_hollow_box():
    assert create_hollow_box(3, 4, '*') == first_hollow_box_expected


def test_second_hollow_box():
    assert create_hollow_box(1, 1, '@') == second_hollow_box_expected

def test_third_hollow_box():
    assert create_hollow_box(3, 24, 'x') == third_hollow_box_expected