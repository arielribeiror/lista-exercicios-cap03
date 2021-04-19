is_fibonacci = int(input("Qual número você quer saber se está na sequência Fibonnaci? "))

find = False
prev1 = 0
prev2 = 1
actual = 1

while is_fibonacci > actual:
  actual = prev1 + prev2
  prev1 = prev2
  prev2 = actual
  
  if is_fibonacci == actual:
    find = True
    print("Ação bem sucedida!")
    
if not find:
  print("A ação falhou...")