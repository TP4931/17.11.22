#Шоколадка имеет вид прямоугольника, разделенного на n×m долек.
# Шоколадку можно один раз разломить по прямой на две части.
# Определи, можно ли таким образом отломить от шоколадки часть, состоящую ровно из k долек.
# Программа получает на вход три числа: n, m, k и должна вывести YES или NO.
n=int(input("введите n"))
m=int(input("введите m"))
k=int(input("введите k"))
if m%k==0 or n%k==0:
  print("yes")
else:
 print("no")
