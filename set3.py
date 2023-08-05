from queue import Queue

# two sum problem
def twosum(a,t):
   res=[]
   for i in range(0,len(a)-1):
      for j in range(i+1,len(a)):
         if a[i]+a[j]==t:
          res.append(i)
          res.append(j)
   return print(res)    
# palindrome check   
 
def palicheck(s):
   rev=""
   for i in range(len(s)-1,-1,-1):
      rev+=s[i]
     
   if rev==s:
      return print(True)   
   else:
      return print(False)

# selection sort 

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

class StackUsingQueue:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, item):
        self.queue2.put(item)
        while not self.queue1.empty():
            self.queue2.put(self.queue1.get())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        if self.queue1.empty():
            raise IndexError("pop from empty stack")
        return self.queue1.get()

    def top(self):
        if self.queue1.empty():
            raise IndexError("top from empty stack")
        return self.queue1.queue[0]

    def empty(self):
        return self.queue1.empty()

#fizz buzz

def fizzbuzz():
    for i in range(0,101):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)
                       
def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
        return word_count
    except FileNotFoundError:
        print("File not found.")
        return 0

def write_count_to_file(count, output_file_path):
    with open(output_file_path, 'w') as output_file:
        output_file.write(str(count))

input_file_path = 'input.txt'        
output_file_path = 'word_count.txt'   

word_count = count_words(input_file_path)
write_count_to_file(word_count, output_file_path)

print(f"Total words: {word_count} (written to {output_file_path})")

#exception handeling

def divideno(a,b):
    if b==0:
        return print("cannot divide by 0")
    else:   return print(a/b)

#tuple unpacking

def tupleunpack(a):
    for i in range(0,len(a)):
       
            print(str(a[i][0])+" "+"is" +" "+str(a[i][1])+" "+"years old")
tupleunpack([("John", 25), ("Jane", 30)])           
        
