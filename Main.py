def solve():
  d = a1*b2-b1*a2
  dx = c1*b2-b1*c2
  dy = a1*c2-a2*c1
  x = dx/d
  y = dy/d
  return x, y

while True:
  print("Standard form of linear equation \n ax+by=c")
  a1 = int(input("Write a value of a:\n")) 
  b1 = int(input("Write a value of b:\n")) 
  c1 = int(input("Write a value of c:\n")) 
  print("Standard form of linear equation \n ax+by=c")
  a2 = int(input("Write a value of a:\n")) 
  b2 = int(input("Write a value of b:\n")) 
  c2 = int(input("Write a value of c:\n")) 
  print("Solution set is", solve())
  print("\n")