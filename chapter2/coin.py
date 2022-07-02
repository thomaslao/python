num=int(input("enter a number:"))
num100=(num//100)
num50=(num%100)//50
num10=(num%100)%50//10

print("百元的數字為 %d" %num100)
print("五十元的數字為 %d" %num50)
print("十元的數字為 %d" %num10)
