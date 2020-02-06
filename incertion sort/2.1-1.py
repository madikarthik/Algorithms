# chapter 2 (pg 22)
# problem no 2.1-1
def insertionSort(n):
   for index in range(1, len(n)):
     currentvalue = n[index]
     position = index
     while position>0 and n[position-1]>currentvalue:
         n[position]=n[position-1]
         position = position-1
     n[position]=currentvalue

n = [31, 41, 59, 26, 41, 58]
insertionSort(n)
print(n)
