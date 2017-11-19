
def _is_prime(number):
    if number<2:                        #numbers equal to 1 and below are not prime numbers
        return False
    if number%2==0 and number>2:        #all even numbers except 2 are not prime numbers
        return False
    for i in range (3,number,2):        #checks if number is divisible by any number between 3 and number. 2 steps to skip even numbers. This can be improved with int(n**0.5) + 1 which I have not figured out yet. 
            if number%i == 0:
                return False
    return True                         #loop ends here if above conditions not met. We have a PRIME number!


def list_of_prime_numbers(max_number):
    numberList=[]                       #creates an empty list 'numberList'
    for i in range(max_number+1):       #Stop is max_number +1 to ensure given number is also tested.
        if _is_prime(i)==True:          #calls _is_prime(number) function
            numberList.append(i)        #appends prime numbers to 'numberList'
    return numberList                   #returns final numberList
# =================== #
# ====== Tests ====== #
# =================== #

# Test: `is_prime`


def test_big_number_prime_true():
    assert _is_prime(19) is True


def test_big_number_prime_false():
    assert _is_prime(20) is False


def test_two_prime():
    assert _is_prime(2) is True


def test_three_prime():
    assert _is_prime(3) is True


def test_four_prime():
    assert _is_prime(4) is False


# Test: `list_of_prime_numbers`

def test_big_number_list():
    assert list_of_prime_numbers(19) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_list_one():
    assert list_of_prime_numbers(2) == [2]


def test_list_zero():
    assert list_of_prime_numbers(0) == []
