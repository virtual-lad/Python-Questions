'''Valid Pin
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false.

"1234"   -->  true
"12345"  -->  false
"a234"   -->  false'''

def pin():
    pin = input('Please enter your PIN: ')
    if len(pin) == 4 or len(pin) == 6:
        if pin.isnumeric():
            return True
    else:
        return False
    
print(pin())

# THE END