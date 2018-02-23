# Python program to illustrate
# Iterating over a list
print("python")
l = ["param", "jeet", "singh"]
for i in l:
    print(i)
      
# Iterating over a tuple (immutable)
print("\nTuple python")
t = ("param", "jeet", "singh")
for i in t:
    print(i)
      
# Iterating over a String
print("\nString python")    
s = "param"
for i in s :
    print(i)
      
# Iterating over dictionary
print("\nDictionary Iteration")   
d = dict() 
d['xyz'] = 123
d['abc'] = 345
for i in d :
    print("%s  %d" %(i, d[i]))
