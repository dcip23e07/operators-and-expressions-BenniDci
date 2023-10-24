# What do the following expressions evaluate to?

print((5 > 4) and (3 == 5)) 
# output False 
# first check first value is bigger than the seccond output here is True 
# seccond check first value equals the seccond value output here is False 
# If one or all of the given Values is False it will Output False only if all values defined by 'and' are True than it prints True

print(not(5 > 4))
# result from print is False.. because Output would be True and the 'not' turns the Question basically around 

print((5 > 4) or (3 == 5))
# First True seccond False... one of the 2 is True that is the check from 'or' so print output will be True

print(not ((5 > 4) or (3 == 5)))
# It check if eighter first or seccond check is True because of the 'or' after that the 'not' will give us the opossite output so False 

print((True and True) and (True == False))
# First is a True seccond is a False .. for 'and' we need all included to be True so this one is a False

print((not False) or (not True))
# One is True with is all that the 'or' check needs to put out True
