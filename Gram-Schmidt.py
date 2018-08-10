#This is a Gram-Schmidt Orthogonalization Python program.

def dot(x,y):
    'Inner/dot product of vectors A and B.'
    z = 0
    for a,b in zip(x,y):
    z += a*b
    return z

def mag(x):
    'Magnitude of a vector.'
    z = 0
    for ele in x:
      z += ele**2
    return z**(0.5)

def unit(x):
    'Normalizes a vector.'
    z = []
    for a in x:
      z.append((1/mag(x))*a)
    return z

def scam(a,b):
    'Scalar multiplication'
    z = []
    for x in b:
      z.append(a*x)
    return z

def sub(a,b):
  'Vector subtraction'
  z = []
  for x,y in zip(a,b):
    z.append(x-y)
  return z

while True:

    x = eval(input("Please enter the linearly independent vectors in any iterable format (list or tuple).\nUser input:"))

    n = 0

    for ele in x:
      n += 1
      print("u_{} = {}".format(n, ele))

    conf= input("\nAre the inputs correct? Y/N")

    if conf.lower() == 'y':
      break

    else:
      print()
      continue

Ans = []
Int = []

for j in range(1,len(x)):
  w = scam(dot(Ans[j-1],x[j]), Ans[j-1])
  Int.append(w)
  for number in range():
    Ans.append(unit(sub(x[j]-w)))
