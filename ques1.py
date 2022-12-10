import re
def isValid(s):
    Pattern = re.compile("\W?\d*\W?\d{3}\W*\d{3}\W?\d{4}")
    return Pattern.match(s)
s = ['2124567890','212-456-7890','(212)456-7890','(212)-456-7890','212.456.7890','212 456 7890',\
    '+12124567890','+12124567890','+1 212.456.7890','+212-456-7890','1-212-456-7890']
for i in s:
    if (isValid(i)):
        print ("Valid Number")    
    else :
        print ("Invalid Number")
input()
 