var_a = 400
var_b = '200' + '200'
var_c = 400.0
var_d = 200 + 200

# 1. what is the result of :
print(var_a == var_b)   # result: False cause the values are not the same one is 400 the other 200200
print(var_a is var_b)   # result: False cause not the same Value and not the same Data type one is int (integer) seccond is str (string)

# 2. what is the result of 
print(var_a == var_c)   # result: True the Value is the same; even though one is int and one is float
print(var_a is var_c)   # result: False because one is int and seccond is float .. not the same Data Type

#3. what is the result of :
print(var_a == var_d)   # result: True same Value .. same int result / value
print(var_a is var_d)   # result: True in the end same Datatype and same number (value)

# == checks if the math values are the same 
# 'is' checks if all is the same: same type,value a.s.o.