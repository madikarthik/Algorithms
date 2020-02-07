def insertionsort(n):
     for index in range (len(n)-2, -1, -1):
          currentvalue = n[index]
          position = index
          print position
          while position < len(n)-1 and n[position+1] > currentvalue:
               n[position] = n[position+1]
               position += 1
          n[position] = currentvalue

n = [31, 41, 59, 26, 41, 58]
insertionsort(n)
print(n)
          
    
          
