# To calculate slope, put in the x and y values.
x1=int(input("What is the first X value? "))
x2=int(input("What is the second X value "))
y1=int(input("What is the first Y value? "))
y2=int(input("What is the second Y value? "))
# Inputs are needed so the user can put in any numbers they want
mY=int(y2-y1)
mX=int(x2-x1)
m=int(mY/mX)
b=int(m*(-1)*x2+y2)
print(b)
#B Inverter
b==int
mY=str(mY)
mX=str(mX)
if(b<0):
 b=str(b)
 print("y ="+" "+mY +"/"+mX+ "x " +  b )
else:
  b=str(b)
  print("y ="+" "+mY +"/"+mX+ "x" + " + " + b )