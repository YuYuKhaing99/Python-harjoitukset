def odd_pois(list):
   list2 = []
   for i in list:
    if i % 2 == 0:
      list2.append(i)
   return list2

list = [1,2,3,4,5,6]
list_new = odd_pois(list)
print(list)
print(list_new)


    