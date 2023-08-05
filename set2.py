import math
# problem 1
def printpat():
    a=[]
   
    for i in range(1,6):
       a.append(i)
    print(" ".join(map(str,a)))
printpat()    

#problem 2
def conditions(a):
    for char in a:
        if char >500:
            break;
        elif char %5==0 and char<=150:
           print(char)
conditions([12, 75, 150, 180, 145, 525, 50])

#problem 3
def appendstr():
    str1="hello"
    str2="world"
    str3=""
    sl=math.floor(len(str1)/2)
    for i in range(0,sl):
       str3+=str1[i]
    str3+=str2 
    
    for i in range(math.ceil(sl),len(str1)):
        str3+=str1[i] 
       
    return str3
print(appendstr())     

# problem 4

def reaarangestr(s):
    str="" 
    str1=""
    for char in s:
        
        if char.lower()==char:
            str+=char  
        else:
            str1+=char  
    return print(str+str1)

reaarangestr("AaDi")           
# probblem 5

def indexlist():
   
    l1 = ["M", "na", "i", "Ke"]
    l2 = ["y", "me", "s", "lly"]
    ln=max(len(l1),len(l2))
    res=[]
    for i in range(0,ln):
       
           res.append(l1[i]+l2[i])
       

    return res    
print(indexlist())

# problem 6

def concatstr():
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
    print(list1+list2)
    res=[]
    res.append(list1[0]+list2[0])
    res.append(list1[0]+list2[len(list2)-1])
    res.append(list1[1]+list2[0])
    res.append(list1[1]+list2[1])
    return print(res)
concatstr()
# problem 7
def printlist():
    list1 = [10, 20, 30, 40]
    list2 = [100, 200, 300, 400]
    j=len(list2)-1
    for i in range(0,len(list1)):
        print(str(list1[i])+" "+str(list2[j]))
        j=j-1
printlist()        

# problem 8
def fun():
   employees = ['Kelly', 'Emma']
   defaults = {"designation": 'Developer', "salary": 8000}
   res={}
   for char in employees:
     res[char]=defaults
   return print(res)

# problem 9

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
    }
keys = ["name", "salary"]
res={}
for char in keys:
   res[char]=sample_dict[char]
#print(res)   
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0]=222
print(tuple1)        