import math

def MD_nRE(y,y_hat,n,p):
    y_root = y**(1/n)
    y_hat_root = y_hat**(1/n)
    loss = (y_root - y_hat_root)**p
    return loss

y = float(input("Gia tri y: "))
y_hat = float(input("Gia tri y_hat: "))   
n = int(input("gia tri cua n: "))
p = int(input("gia tri bac p: "))
loss = MD_nRE(y,y_hat,n,p)
print(f"y = {y},y_hat {y_hat},n = {n},p = {p}, loss = {loss}")