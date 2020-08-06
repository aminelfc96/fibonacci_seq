
import os
from time import time
fibo_cache = []
def fibo(n):
#  file = open('fibo_seq.txt','w') -- Uncomment this line to save the result on file
   if n == 1:
      fibo_cache.append(1)
#     print(1) -- Uncomment to print the sequence / You need to comment the progress bar section 
    
#     file.write('1\n') -- Uncomment this line to save the result on file
  elif n == 2:
      fibo_cache.append(2)
 #    print(2) -- Uncomment to print the sequence / You need to comment the progress bar section 
    
 #    file.write('2\n') -- Uncomment this line to save the result on file
  else:
      x = fibo_cache[-1] + fibo_cache[-2]
      fibo_cache.append(x)
 #    print(x) -- Uncomment to print the sequence / You need to comment the progress bar section 

 #    file.write(str(x)+'\n') -- Uncomment this line to save the result on file
  
 # Uncomment this section if you want to see the golden ration
 # try:
 #    ratio = float(fibo_cache[-1] / fibo_cache[-2])
 #    print(ratio)
 # except IndexError:
 #    pass
  del fibo_cache[:-2]
numbers = int(input('enter number '))
start = time()
for n in range(1,numbers+1):
  fibo(n)
  #Progress Bar 
  progress = int(n * 100 / numbers)
  if progress >= 1:
    os.system('cls')
    print(progress*'█',f'{progress}%')

 # to calculate the process time in seconds
print('process took',time()-start)
