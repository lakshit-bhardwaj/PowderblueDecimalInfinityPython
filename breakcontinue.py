for i in range(1,100):
  for j in range(2,int(i//2)+1):
    if (i%j==0):
      break
  else:
    print(i)
#This else would print line6 if the inner loop completes without break 
