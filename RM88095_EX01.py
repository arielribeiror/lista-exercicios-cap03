eatTimes = int(input("Quantos alimentos você ingeriu hoje? "))
total = 0

for i in range(0, eatTimes):
  msg = "Quantas calorias o {}º alimento possui? ".format(i + 1)
  calories = int(input(msg))
  total = total + calories
  i+=1
  
print("Você ingeriu {} calorias hoje".format(total))