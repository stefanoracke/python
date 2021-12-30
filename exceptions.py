#Errors and exceptions

from typing import final


x= int(input("Ingrese el valor de x: "))

#raise
'''if x<0:
    raise Exception("x Should be positive")'''


#assert
#assert(x>=0), 'x is not positive'



try:
    a= 5 / x
except:
    print('An error happened')


try:
    a= 5 / x
except Exception as e:
    print(e)
else:
    print("Everithing is fine")
finally:
    print("Clearing up...\n\n\n")


class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(n):
    if n>100:
        raise ValueTooHighError('Value is too high')

    if n<5:
        raise ValueTooSmallError('Value is too small', n)

try:
    test_value(x)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)



