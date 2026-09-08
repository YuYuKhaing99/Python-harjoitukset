def summa(list):
  sum = 0
  for num in list:
    sum += num
  return sum
    
list = [1,2,3,4,5,6]
tulos = summa(list)
print("Tulos on : ",tulos)
