
#1
#name ="Boby"
#age ="10"
#here ="85"

#print("I am " + name.upper() + " My age is " + age + " My grandpa age is " + here);
#print(len(name))
#print(name.index("G"))






#2
#phrase ="Gogo"
#print(phrase.index("o"))






#3
#name = input("Name: ")
#print(name)

 
 



#4  
#Add Numbers and print 
#x = int(input("First Number: "));
#y = int(input("Sec Number: "));
 
#result = int(x + y);
#print(f"{x}+{y}={result}")








#5 - 4.6.1
#import matplotlib.pyplot as plt

#x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#y = [5, 2, 4, 4, 8, 7, 4, 8, 10, 9]

#plt.plot(x,y)
#plt.xlabel('Time (s)')
#plt.ylabel('Temperature (degC)')
#plt.show()


#6 - Circle Calculations
#r = float(input("Circle Radius: "));
#d = float(r*2);
#o = float(2*r*3.14);
#a = float((r*r)*3.14);
#print(f"Radius = {r}");
#print(f"Diameter = {d}");
#print(f"Circumference = {o}");
#print(f"Area = {a}");










#7 Opgaver 1-10





#7.1
#print("Twinkle, twinkle, little star, \n\t How I wonder what you are!\n\t");






#7.2
#import sys
#print(sys.version);







#7.3 - Show Dat and Time in a special format
#import datetime
#now = datetime.datetime.now();
#print("Current Time:");
#print(now.strftime("%Y-%m-%d %H:%M:%S"));






#7.4
#firstname = input("Firstname:");
#lastname = input("Lastname:");

#print(lastname + " " + firstname);






#7.5
#values = input("Input numbers seperated with comma: ")
#list = values.split(",")
#tuple = tuple(list)
#print('List : ', list)
#print('Tuple :' , tuple)






#7.6 - Write a Python program to accept a filename from the user and print the extension of that
#filename = input('Input the Filename: ')
#f_extens = filename.split(".") #Splits the string where is dot and "f_extens" becomes array
#print("Extension: " + repr(f_extens[-1])) #Takes the last item from the array








#7.7 - Write a Python program to display the first and last colors from the following list.
#color_list = ["Red","Green","White" ,"Black"]
#print("First: " + color_list[0] + " \nLast: " + color_list[-1])
# print( "%s %s"%(color_list[0],color_list[-1])) # %s %s "%" = is format the way how its displayed









#7.8 - Write a Python program to display the examination schedule. (extract the date from exam_st_date).
#exam_st_date = (11, 12, 2021)
#print("Exam Date: %i / %i / %i"%exam_st_date ) # Again formating with the %










#7.9 - Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

#a = int(input("Input an intiger: "))
#n1 = int( "%s" % a)
#n2 = int( "%s%s" % (a,a))
#n3 = int( "%s%s%s" % (a,a,a))
#print(n1 + n2 + n3)






 
 #8.1 - Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
 
#print(abs.__doc__)








#8.2 - Write a Python program to print the calendar of a given month and year.

#import calendar
#y = int(input("Input the year: "))
#m = int(input("Input the month: "))
#print(calendar.month(y, m))








#8.3 - Write a Python program to print the calendar of a given month and year.

#print("""aaa aaa aaaaa AAAAaa aaAAAaaA "bbbbBB" ..........
#CCCCCCCCC
#ddddddddddd eeeeeeeeeeeee
#gggggggggggggggggggggg""")










#8.4 - Write a Python program to calculate number of days between two dates.
#from datetime import date
#f_date = date(2021, 1, 1)
#l_date = date(2021, 7, 31)
#delta = l_date - f_date
#print(delta.days)










##8.5 - Write a Python program to get the the volume of a sphere with radius 6. 
#pi = 3.14159226
#r = float(input("Radius: "))
#V = 4.0/3.0*pi* r**3
#print("The Volume of the Sphere is: ",V)











#8.6 - Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
#def difference(n):
#     if n <= 17:
#         return 17 - n
#     else:
#         return (n - 17) * 2

#print(difference(22))
#print(difference(14))










#9 - start, stop, step
#for x in range(4, 12, 2):
# print(x)













#10 - Loop array - x = item value not index

#data =[1, 5, 6, 3, 12, 3]

#sum = 0


#for x in data:
#    sum = sum + x

#    #print(x) # x = the item itself from the array at the specific index so X is not the count or the index its the items value at the index 
#    print(sum)
    



# Fibonaci

#N = 10

#fib = [0, 1]

#for k in range(N-2):
#    fib_next = fib [k+1] + fib[k]
#    fib.append(fib_next)
    
#print(fib)










# 11 - While Loop

#m = 8

#while m> 2:
#    print(m)
#    m=m-1











 # 12 - For Loop

#m = 8
#s = 0

#for x in range(0, m-2):
# print(m - x)
# #s = float((x+1) / 2);
# #print(s)









#13 - Print From 2 to 5 index - From to 

#a = "Hello World!"

#print(a[2:5])
#print(a.split(" ")) # Split and becomes array












#14 - Dictionary

#my_Dictionary = {"Jan": "January", "Feb": "February", "Mar": "March"}
#my_Num_Dictionary = {0: "January", 1: "February", 2: "March"}

#print(my_Dictionary)
#print(my_Dictionary["Jan"])
#print(my_Dictionary.get("Jan"))
#print(my_Dictionary.get("Luv")) # NONE - Not exists
#print(my_Dictionary.get("Luv", "Not Valid")) # Defailt Value Not Valid

## With Nums
#print(my_Num_Dictionary[1])









#15 While Loop

#i = 1
#while i <= 10:
#    print(i)
#    i += 1

#print("Done")









#15 For loop

#my_string = "abcdefg"
#for x in my_string:
#    print(x)
    









##16 - Exponent Function

#print(2**3)

#def raise_to_power(base_num, pow_num):
#    result = 1
#    for i in range(pow_num):
#        result = result * base_num
#    return result



#print(raise_to_power(2, 3))










# 17 - Try Exept
#try:
#    number = int(input("Give me a number: "))
#    print(number)

#except:
#    print("Invalid Input")








# 2 --------------------------------------------------------
#try:
#    #value = 10/0
#    number = int(input("Give me a number: "))
#    print(number)


## First Specific Exception catch
#except ValueError:
#    print("Invalid Value: Should be int")


##Second Specific Excpetion Catch
#except ZeroDivisionError:
#    print("Division by ZERO !!!!!!!!!!!!!")



#    #GET THE ERROR MESSAGE
##except ZeroDivisionError as err:
##    print("Division by ZERO !!!!!!!!!!!!!" + err)




#18 - Open File

#txt_file = open("textFile.txt", "r") # Mode r = read, r+ = read and write,  w = write, a = append

#print(txt_file.read())
#print(txt_file.readline())
#print(txt_file.readlines())
#print(txt_file.readlines()[1])


## Read Lines
#for txt in txt_file.readlines():
#    print(txt)


#txt_file.close();












#19 - CLASS

## From the Student FILE import the student CLASS
#from student import student

#student1 = student("Gosho", 22, 12345678)

#print(student1.name)
#print(student1.age)
#print(student1.tlf)


## Class Method Example
#print(student1.is_over_18())










#20 - Inheritance

#from Chef import Chef

#myChef = Chef()
#myChef.make_chicken()
#myChef.make_salad()
#myChef.make_special_dish()


#---------------------------
#Import what you need
#from ChineseChef import ChineseChef

## New Obj
#myChef = ChineseChef()

##Own Method
#myChef.make_fried_rice()

## Inherited - Methods
#myChef.make_chicken()
#myChef.make_salad()
#myChef.make_special_dish()










##21 - Default values
## Default number = 1 if nothing is given to the method
#def method1(x=1):
#    return x **2

## Give 5 to the method
#call = method1(5)
#print(call)








#22 - Multiply word
# Default number = 1 if nothing is given to the method
#def method1(word, freq = 1):
#    print(word*freq)

#method1('Gosho', 10)









#23 - Sort List

#mylist = [7, 5, 1, 2]

## Sort1
#mylist.sort()

##Sort2
#new_list = sorted(mylist)
#print(new_list)








#24 - List eith 5 zeros

#mylist = [0] * 5
#print(mylist)

#mylist2 = [1,2,3,4,5]

## Concat
#newlist = mylist + mylist2
#print(newlist)









#25 - Print list range
#mylist2 = [1,2,3,4,5]

#a = mylist2[1:5]
#print(a)



#mylist3 = [1,2,3,4,5,6,7,8,9,10]
#b = mylist3[::2] # Take Every Second "kan be 3 etc."
#b = mylist3[::-2] # From the end every second
#print(b)









#26 - Copy List

#list_original = ["banana", "cherry", "apple"]

## Pointer to list_original
#list_pointer = list_original
#print(list_pointer)


## Deep Copy
##1 - Method
#list_deep_copy = list_original.copy()

##2 - Method
#list_deep_copy = list(list_original)

##3 - Method
#list_deep_copy = list_original[:]


## Append
#list_deep_copy.append("Ananas")

#print(list_deep_copy)












#27 - Copy list squared

#list4 = [1,2,3,4,5,6]
#b = [i*i for i in list4]

#print(list4)
#print(b)











##28 - Tuple - Tuple is imutable - this means ones created cant be changed - like list but list that cant be edited only readed

#mytuple = tuple(["Max", 28, "Boston"])
#print(mytuple)

#item = mytuple[2]
#print(item)









#28 - Tuple 2 

#my_tuple2 = (0, 1, 2, 3, 4)

#i1, *i2, i3 = my_tuple2

#print(i1) # First Item
#print(i3) # Last Item
#print(i2) # List without the first and the last Item









#29 Compare Time
#import timeit
#print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
#print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))










#30 - Get byte size
#import sys
#my_list = [0, 1, 2, "hello", True]
#my_tuple = (0, 1, 2, "hello", True)

#print(sys.getsizeof(my_list), "bytes")
#print(sys.getsizeof(my_tuple), "bytes")










#31 - Dictionary

#mydict = {"name": "Max", "age": 25, "city": "Somewere"}
#print(mydict)

 
#mydict2 = dict(name="Mary", age = 27, city ="Boston")
#print(mydict2)



## Read Dictionary
#value = mydict["name"]
#print(value)




# Delete in Dictionary #1
#del mydict["name"]

# Delete in Dictionary #2
#mydict.pop("name")

# Delete in Dictionary - Remove last item #3
#mydict.popitem()

#print(mydict)


# Check
#if "name" in mydict:
#    print(mydict["name"])



    # Loop in Dictionarry
#for key in mydict.keys():
#    print(key)


## Loop - Value
#for value in mydict.values():
#    print(value)



##Loop - and get - Both Key and Value

#for key, value in mydict.items():
#    print(key, value)






# Value int and Key int
#my_dict = {3: 9, 6: 36, 9: 81}
#print(my_dict)

#value = my_dict[3]
#print(value)



# Dictionary and tuple - cant use list only dict for key

#mytuple = (8, 7)
#mydict = {mytuple: 15}

#print(mydict)












##32 -  Sets
#myset = set()

#myset.add(12)
#myset.add(22)
#myset.add(32)
#myset.add(42)

##myset.remove(3)
##myset.clear() # Remove all
##myset.pop() # Remove last
#print(myset)




# Loop the set
#for i in myset:
#    print(i)




# If is in the set
#if 2 in myset:
#    print("yes")



#odds = {1, 3 ,5, 7 ,9}
#evens = {0, 2, 4, 6, 8}
#primes = {2, 3, 5, 7}


### Unions without dublicates
##u = odds.union(evens)
##print(u)




## Numbers that are found in both sets
#i = evens.intersection(primes)
#print(i)




## Print Only the Difference 
#setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
#setB = {1, 2, 3, 10, 11, 12}

##diff = setA.difference(setB)

## Take only the nubers that are not common in both sets
#diff = setB.symmetric_difference(setA)

#print(diff)








# 2-------------------------------------
#setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
#setB = {1, 2, 3, 10, 11, 12}

# Union without duplication
#setA.update(setB)
#print(setA)


# Only Common numbers remain after update
#setA.intersection_update(setB)
#print(setA)


# Update with only not common numbers
#setA.difference_update(setB)
#print(setA)


# Symmetric update
#setA.symmetric_difference_update(setB)
#print(setA)










#3 -------------------------------------

#setA = {1, 2, 3, 4, 5, 6}
#setB = {1, 2, 3}
#setC = {7, 8}


# Are all items in A also in B = NO = False
#print(setA.issubset(setB))


# Are all items in B also in A = Yes = True
#print(setB.issubset(setA))



# Do the first set have all the numbers from the second = YES = TRUE
#print(setA.issuperset(setB))


# No same elements in setA and setC
#print(setA.isdisjoint(setC))













## 33 - Imutable SET - forzenset
#a = forzenset([1, 2, 3, 4])

## Gives Errror its Imutable
##a.add(2)
#print(a)








#34 - Reverse String
#my_string = "Stefan"
##substring = my_string[::-1]
##substring = my_string[1:3]
#print(substring)







##35 - Remove whitespaces

#my_string = '         Hello      '
#print(my_string)
#my_string = my_string.strip()
#print(my_string)






#36 - String starts with
#my_string = 'Hello World'
#print(my_string.startswith('Hello'))
#print(my_string.endswith('Hello'))








# 36 - Find Index of string char
#my_string = 'Hello World'
#print(my_string.find('o'))






## 37 - Count specific char in string
#my_string = 'Hello World'
#print(my_string.count('o'))









## 38 - Replaces Chars in string
#my_string = 'Hello World'
#print(my_string.replace('o', 'a'))
#print(my_string.replace('World', 'Meee'))








## 39 - String to list
#my_string = 'Hello World'
##my_list = my_string.split()
##my_list = my_string.split(",")
#print(my_list)













# 40 - String to list
#my_string = 'Hello, World, Meee'
#my_list = my_string.split(",")
#print(my_list)




## From list to string
#new_string2 = ''.join(my_list)
#print(new_string2)













# 41 - From list to string #2  + Timer -- Time

## Timer 
#from timeit import default_timer as timer

## List
#my_list = ['a'] *6
#print(my_list)




## BAD -- Bad performance - Should use join instead
#start = timer()# Timer

#my_string = ''
#for i in my_list:
#    my_string +=i
#    stop = timer() # Timer
#print(my_string)

#print(stop-start)# Timer




## GOOD
#my_string = ''.join(my_list)
#print(my_string)









#42 - String with %s = string, %d = int, %f = float, %2f = float with 2 digits after the comma - variable

## 1
#var = "Tom"
#fl = 0.5
#my_string ="the variable is %s" % var
#my_string ="the variable is %.2f" % fl
#print(my_string)



##2 - ":.2f" = 2 digits after comma
#fl = 0.5343
#str = "Hello"
#my_string ="the variable is {:.2f} and {}".format(fl, str*2)
#print(my_string)




#3 - *2 multiply the float and make 2* string
#fl = 0.5343
#str = "Hello"
#my_string = f"the variable is {fl*2} and {str*2}"
#print(my_string)









# 43 - Collections
# Add String to Dictionary with the amount of same chars insde the string

#from collections import Counter
#a = "aaaaaabbbbbbccccc"
#my_counter = Counter(a)
##print(my_counter)
##print(my_counter.keys())
##print(my_counter.values())
##print(my_counter.most_common(2)) # 1 = most common , 2 = second most common
##print(my_counter.most_common(1)[0][0]) # [0] = the tuple at index zero than the element [0] in the tuple
#print(list(my_counter.elements())) # Get the elements as list 












# 44 - namedTuple - Point
 
# Easy to Create lightweight object type simillar to struct

#from collections import namedtuple
#Point = namedtuple('Point', 'x,y')
#pt = Point(1, -4)
#print(pt)










#45 - Ordered Dict - Remember the order of insertion
#from collections import OrderedDict
#ordered_dict = OrderedDict() 
#ordered_dict['a'] = 1
#ordered_dict['c'] = 3
#ordered_dict['b'] = 2
#ordered_dict['d'] = 4
#print(ordered_dict) 



## Normal Dictionary
#dictN = {'b':1, 'a':2, 'c':3}
#print(dictN)



## Dictionary 3
#from collections import defaultdict
#d = defaultdict(int) #int, float, string, list etc.
#d ['a'] = 1
#d ['b'] = 2
#d ['c'] = 3
#print(d['a'])





# Dictionary DEQUE
#from collections import deque
#d = deque() 
#d.append(1)
#d.append(2)

#d.appendleft(3) # Append to the left
#print(d)

##d.pop()# Pop = return and remove last element
##d.popleft()
##d.clear()# Remove all elements
##d.extend([4,5,6])
##d.extendleft([4,5,6])
#d.rotate(1)
##d.rotate(2) # rotate 2 places to the right
#d.rotate(-2) # rotate 2 places to the left
#print(d)









#46 - Product -IterTools - Combine all numbers to list

#from itertools import product
#a = [1,2]
#b = [3,4]
#prod = product(a,b)
##prod = product(a,b, repeat=2)
#print(list(prod))














#47 - Combine all numbers in all different ways - Ex. Password bot

#from itertools import permutations
#a = [1,2,3]
#perm = permutations(a)
##perm = permutations(a, 2) #Only different combinations with 2
#print(list(perm))













#48 - Combinations - All possible combinations with lenght 2
#from itertools import combinations
##a=[1,2,3]
##comb = combinations(a,2)
##print(list(comb))




# Combinations with replacement
#from itertools import combinations, combinations_with_replacement
#a=[1,2,3]
#comb = combinations(a,2)
#print(list(comb))
#comb_wr = combinations_with_replacement(a, 2)
#print(list(comb_wr))





# 49 - Acumulate - plus the numbers from the different lists in zigzac way

#from itertools import accumulate
#a = [1, 2, 3, 4]
#acc = accumulate(a)
#print(a)
#print(list(acc))







#50 - Multiply the numbers from the lists

#from itertools import accumulate
#import operator
#a = [1, 2, 3, 4]
#acc = accumulate(a, func=operator.mul)
 
#print(a)
#print(list(acc))







## Max
#from itertools import accumulate
#import operator
#a = [1, 2, 5, 3, 4]
#acc = accumulate(a, func=max)
#print(a)
#print(list(acc))





#Groupby

#from itertools import groupby

## Method
#def smaller_than_3(x):
#    return x <3

#a = [1, 2, 3, 4]
#group_obj = groupby(a, key=smaller_than_3)
#for key, value in group_obj:
#    print(key, list(value))






#51 -  Lambda
#add10 = lambda x: x +10
#print(add10(5))

## Func
#def add10_func(x):
#    return x + 10

## Lambda
#mult = lambda x,y: x*y
#print(mult(2,7))




# ---------------------------------
#points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]

#points2D_sorted = sorted(points2D, key =lambda x: x[1]) # Sort by key
#points2D_sorted2 = sorted(points2D, key =lambda x: x[0]) # Value // Not sure
#points2D_sorted3 = sorted(points2D, key =lambda x: x[0] + x[1]) # Sort acording to the sum of each Like (1, 2) = 3 etc.
#print(points2D)

#print(points2D_sorted)
#print(points2D_sorted2)



## Every next number is added to 2
#a = [1, 2, 3, 4, 5]
#b = map(lambda x: x*2, a)
#print(list(b)) # Convert to list


## Better = easier
## Same thing - # Every next number is added to 2
#c = [x*2 for x in a]
#print(c)




## Same thing
## Filter function
#a = [1, 2, 3, 4, 5, 6]
#b = filter(lambda x: x%2 == 0, a)
#print(list(b))

#c = [x for x in a if x%2== 0]
#print(c)





## Reduce Function
#from functools import reduce
#a = [1, 2, 3, 4]

#product_a = reduce(lambda x,y: x*y, a) # [1, 2, 3, 4] = 1*2 = 2 * (3*4) = 24
#print(product_a)














# 52 - Process
#from multiprocessing import Process
#import os
##import time # Like stopwatch - Used dor getting the time executing nothing to do with the threading
##time.sleep(0.1)

#def square_numbers():
#    for i in range(100):
#        i * i


#processes = []
#num_processes = os.cpu_count()


## Create processes
#for i in range(num_processes):
#    p = Process(target=square_numbers)
#    processes.append(p)


##Start
#for p in processes:
#    p.start()


## Join
#for p in processes:
#    p.join()

#print('End Main')












## Threading ------------------------------------------

## 52 - Process
#from threading import Thread
#import os

#def square_numbers():
#    for i in range(100):
#        i * i


#threads = []
#num_threads = 10


## Create processes
#for i in range(num_threads):
#    t = Thread(target=square_numbers)
#    threads.append(t)


##Start
#for t in threads:
#    t.start()


## Join
#for t in threads:
#    t.join()

#print('End Main')











## 53 - Multi Threading
# Threads share same memmory space, whilw Processes dont - One process can contain many threads
#Starting a process is much havier than starting a Thread - Starting a process reserves amount of memmory
# In C# Thread pool is much better because it dont start threads but having threads that are waiting to be assigned to work
#So thread Pool is much better than staring thread and use it

#from threading import Thread

#def square_numbers():
#    for i in range(100):
#        i*i

#if __name__ == "__main__":
#            threads = []
#            num_threads = 10

#            # Create Threads
#            for i in range(num_threads):
#                thread = Thread(target=square_numbers)
#                threads.append(thread)
          
#            # Start Threads
#            for thread in threads:
#                thread.start()
          
#            #Join Threads: Wait for them to complete
#            for thread in threads:
#                thread.join()
          
#            print('END MAIN')



















# 54 -  Multi Threading - Share Data between Threads
 
#from threading import Thread
#import time
#database_value = 0 # Simulate DB


#def increase():
#    global database_value

#    local_copy = database_value

#    # Rrocessing
#    local_copy +=1
#    time.sleep(0.1)


#    database_value = local_copy 



#if __name__ == "__main__":
#    print('Start value', database_value)

#    thread1 = Thread(target=increase)
#    thread2 = Thread(target=increase)

#    thread1.start()
#    thread2.start()

#    thread1.join()
#    thread2.join()

#    print('end value', database_value)
#    print('end main')












# 55.  Generators
# Generators are functions that return object that can be iterated over. It generates the items of the object later only when you ask for it. 
# Memmory efficient


#def mygenerator():
#    yield 1
#    yield 2
#    yield 3

#g = mygenerator()


#1 - Print All
#for i in g:
#    print(i)


#2 - Print Next
#value = next(g)
#print(value)



#value = next(g)
#print(value)





#3
#print(sum(g))




#4
#print(sorted(g))









#Generator 2 -------------------------------------------------------------------------------------


#def countdown(num):
#    print('Starting')
#    while num > 0:
#        yield num  #Stops here and waits for ex. next(cd)
#        num -=1

#cd = countdown(4)

#value = next(cd)
#print(value)


#print(next(cd))









#Generator 3 --------------------------------------------------------------------------------------
# No Generator
#def firstn(n):
#    nums = []
#    num = 0
#    while num < n:
#        nums.append(num)
#        num += 1
#    return nums

#print(sum(first(10)))




#Gen4---------------------------------------------------------

#import sys

## 1 No generator uses more memmory
#def firstn(n):
#    nums = []
#    num = 0
#    while num < n:
#        nums.append(num)
#        num += 1
#    return nums



## With Generator uses less memmory
#def firstn_generator(n):
#    num = 0
#    while num < n:
#        yield num
#        num += 1

##print(sum(firstn(10)))
##print(sum(firstn_generator(10)))

#print(sys.getsizeof(firstn(10000000)))
#print(sys.getsizeof(firstn_generator(10000000)))


















# Fibonachi with yield - Generqator --------------------------------------------------------------------------------

#def fibonachi(limit):
#    #011235813...
#    a, b = 0, 1
#    while a < limit:
#        yield a
#        a, b = b, a + b

#fib = fibonachi(30)
#for i in fib:
#    print(i)





#------Generator -- memmory Comparison------------------------------------------------------------

## Less Memorry
#import sys
#mygenerator = (i for i in range(100000) if i % 2 == 0)
#print(sys.getsizeof(mygenerator))


## More memmory
#mylist = [i for i in range(100000) if i % 2 == 0]
#print(sys.getsizeof(mylist))

















# 57 - Random Number
#import numpy as np
#np.random.seed(123)


#print(np.random.randint(2,5))












# 58 -- For loop ---------------------------------------------------------------
#for x in range(0, 10):
#    print(x)















# 59 - Decorators -------------------------------------------------------------
# Decorator allows you to add more funktionality to a method without modifying it


#@mydecorator
#def dosomething():
#    pass




##1 -----------------------------------------------------
##1 - Func 1
#def start_end_decorator(func):

#    def wrapper():
#        print('Start')
#        func()
#        print('End')
#    return wrapper



##2 - Func 2
#def print_name():
#    print('Stefan')



#print_name = start_end_decorator(print_name)

#print_name()





##2 -------------------------------------------------------------
##1 - Func 1
#def start_end_decorator(func):

#    def wrapper():
#        print('Start')
#        func()
#        print('End')
#    return wrapper



##2 - Func 2
#@start_end_decorator
#def print_name():
#    print('Stefan')

 

#print_name()











#3 ------------Decrators-------------------------------------------------
#import functools

##1 - Func 1
#def start_end_decorator(func):
#    @functools.wraps(func)
#    def wrapper(*args, **kwargs): # 11111111111
#        print('Start')
#        result = func(*args, **kwargs)
#        print('End')
#        return result
#    return wrapper # 2222222222



##2 - Func 2
#@start_end_decorator
#def add5(x):
#    return x + 5

 

#print(help(add5))
#print(add5.__name__)













# 60 - Random numbers -----------------------------------------------------------------------

import random

## Float Random
#a = random.random()
#print(a)



## Range
#b = random.uniform(1, 10)
#print(b)



## Range Int
#c = random.randint(1, 10)
#c = random.randrange(1, 10) # upper bound not included not picking the 10
#print(c)




## Normal Variate
#d = random.normalvariate(0, 1) 
#print(d)





# Random Pick from a List -------------------------------------------------------------
#mylist = list("ABCDEFGH")
#print(mylist)

#a = random.choice(mylist) # Picks random element from the list
#a = random.sample(mylist, 3) # Picks 3 unique elements No repeats of chars "Cant pick same char more than ones"
#a = random.choices(mylist, k=3) # Can pick same char more than ones  
#a = random.shuffle(mylist) # Mixing the elements "shuffles the element
#print(mylist)

#print(a)










#2 Random Pick from a List -------------------------------------------------------------
#import random

#random.seed(1) # SEED
#print(random.random())
#print(random.randint(1, 10))



#random.seed(2) # SEED
#print(random.random())
#print(random.randint(1, 10))



#random.seed(1) # SEED
#print(random.random())
#print(random.randint(1, 10))





#3 Random -------------------------------------------------------------------------------------

#import secrets

#a = secrets.randbelow(10) # int between 0 - 10
#a = secrets.randbits(4) #Max 4 bit- 1111 = 15    #Menas that tha max number is 15 so 0 -15 
#print(a)



#2 Random - Secret--------------------------------------------------------

#mylist = list("ABCDEFGH")
#a = secrets.choice(mylist)
#print(a)


#3 Random - Numpy--------------------------------------------------------

#import numpy as np

##a = np.random.rand(3) # Float Array 3 slots
##a = np.random.rand(3,3) # Float Array 3x3
##a = np.random.randint(0, 10, 3) # Range = 0-10 excluding 10 # Size 3
##a = np.random.randint(0, 10, (3,4)) # 3x4 Array
 
#print(a)



#4 Shuffle - Mix up the elements -------------------------------------------------------------------------

#import numpy as np


#arr = np.array([[1,2,3], [4, 5, 6], [7, 8, 9]])
#print(arr)
#np.random.shuffle(arr)
#print(arr)