userinput = int(input())
vetor = []
comprimento = 0
item = 0

while comprimento < 1000:
  vetor.append(item)
  print('N[{}] = {}'.format(comprimento,item))
  if item < (userinput - 1):
    item = item + 1
  else:
      item = userinput - 1
      item = 0
  comprimento = comprimento + 1