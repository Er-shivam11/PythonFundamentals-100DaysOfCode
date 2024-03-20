#tuple operation
my_tuple=(1,3,4,5,6,8)
# print(my_tuple)

#concatenation

new_tple=my_tuple + (2,3,5)
# print(new_tple)

#slicing
slice=new_tple[1:4]
# print(slice)

#indexing
index=slice[2]  #error tell yes or no fast
# print(index)
# no error beacuse 0.1.2 on 2 if you see number was 5 


#tuples method
my_tuples=(1,1,2,3,4,4,45,5,5,5)

#count
count=my_tuples.count(21)  #0 because its not presen tin the tuple 
# print(count)

#now we will see tuple vs list

list=[1,2,3]
tuple=(1,2,3)
# so vascally we will see first mutable ex:
list[0]=0
# print(list)

#that  means list can be change thats why list are mutable in nature

# now let see for tuple it will through an erro i guess let see wht you say ?

tuple[0]=0
print(tuple)

# so whether you change bracket or assign any item it will not update or change the existing thats why 
#we call this as immutable in nature.

