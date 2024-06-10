import math

def is_number(x):
  try:
    float(x)
  except ValueError :
   return False
  return True

def Sigmoid_Function(x):
 return 1/(1+math.exp(x))

def ReLu_Funtion(x):
  if x <= 0:
    return 0
  if x > 0:
    return x

def ELU_Funtion(x,alpha=0.01):
  if x <= 0:
    return alpha*(math.exp(x)-1)
  if x > 0:
    return x


x = input("Nhập giá trị x: ")
if is_number(x):
  x = float(x)  # Convert x to float
  ten_ham = input("activation_function: ")
  if ten_ham =="sigmoid":
    ketqua=Sigmoid_Function(x);
    print(f"{ten_ham}({x}) = {ketqua}")
  elif ten_ham =="relu":
    ketqua = ReLu_Funtion(x)
    print(f"{ten_ham}({x}) = {ketqua}")
  elif ten_ham =="elu":
    ketqua = ELU_Funtion(x)
    print(f"{ten_ham}({x}) = {ketqua}")
  else:
    print(f"{ten_ham} is not supported")
    
else:
  print("x must be a number")