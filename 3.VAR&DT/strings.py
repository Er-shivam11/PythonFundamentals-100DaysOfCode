# string basic
string_var='hello shivambytes'
# print(string_var)

# string concatenation
var1='welcome'
var2='home'
var3=var1 + " " + var2
# print(var3)

# string slicing
var4=var3[2:]
# print(var4)

# string formatting
name="shivam"
age=24
# print("my name is {} and my age is {}.".format(name,age))

# string methods
sentence="hello shivam how you doing!!!"
uppervar=sentence.upper()
lowervar=sentence.lower()
capvar=sentence.capitalize()
# print(capvar)

# splitting and joining
csv_string="apple,banana,grapes"
split_list=csv_string.split(",")
# print("split list:",split_list)

joined_string="-".join(split_list)
print("joined splitlist:",joined_string)
