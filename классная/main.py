#Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении и на одну клетку по горизонтали,
# или наоборот. Даны две различные клетки шахматной доски, определи,
# может ли конь попасть с первой клетки на вторую одним ходом.
x=int(input())
y=int(input())
x1=int(input())
y1=int(input())

if abs(x-x1)==2 and abs(y-y1)==1 or abs(x-x1)==1 and abs(y-y1)==2:
    print("yes")
else:
    print("no")