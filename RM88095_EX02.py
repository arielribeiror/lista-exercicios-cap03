transactions = int(input("Quantas transações você fez hoje? "))
total = 0
average = 0

for i in range(0, transactions):
  msg = "Qual o valor da {}ª transação? ".format(i + 1)
  transactionValue = float(input(msg))
  total = total + transactionValue
  average = total / transactions
  i+=1
  
print("Você gastou um total de R${} com uma média do dia de R${}".format(total, average))