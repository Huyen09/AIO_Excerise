import math
import random

def num_samples(x):
  return x.isnumeric()

def MAE_funtion(predict,target):
  return abs(target-predict)

def MSE_funtion(predict,target):
  return (target-predict)**2

def RMSE_funtion(predict,target):
  return math.sqrt((target-predict)**2)

x = input("samples: ")
if num_samples(x):
  x = int(x)
  loss_name = input("Loss_name= ")
  for i in range (x) :
    target = random.uniform(0,10)
    predict = random.uniform(0,10)
    if loss_name == "mae":
      ketqua = MAE_funtion(predict,target)
      print(f"sample {i+1}:{loss_name}({predict},{target}) = {ketqua}")
    if loss_name == "mse":
      ketqua = MSE_funtion(predict,target)
      print(f"sample {i+1}:{loss_name}({predict},{target}) = {ketqua}")
    if loss_name == "rmse":
      ketqua = RMSE_funtion(predict,target)
      print(f"sample {i+1}:{loss_name}({predict},{target}) = {ketqua}")
else:
  print("num_sample must be a number")

