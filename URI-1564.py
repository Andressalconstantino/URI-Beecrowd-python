while True:
  try:
    number= int(input())
    if number!=0:
      print("vai ter duas!")
      continue
    elif number==0:
      print("vai ter copa!")
      continue
  except EOFError:
     break