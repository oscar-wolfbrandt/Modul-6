#1#
def function1(number1, number2):
  print(number1 + number2)
function1(3, 3)

#2#
def namn(oscar):
  print("mitt namn är " + oscar)
namn("oscar")

#3#
sak = 10 
while sak > 0: 
  def namn(oscar):
    print("mitt namn är " + oscar)
  namn("oscar")
  sak = sak - 1 

#4#
def add():
  tilläg = input("vadd vill du läga till:")
  lista.append(tilläg)

  
def reomve():
  bort = int(input("vad vill du ta bort "))
  lista.pop(bort)

  
def ändra():
  change = int(input("vilken vill du ändra:"))
  new = input("vad vill du ha istälet")
  lista.pop(change)
  lista.append(new)

  
lista = []
loop = True 

while loop == True:
  do = input("vad vill du göra till/bort/ändra/ut:")

  if do == "till":
    add()
    print(lista)
  
  elif do =="bort":
    reomve()
    print(lista)
  
  elif do =="ändra":
    ändra()
    print(lista)
  elif do == "ut":
    break


#5#
def addition():
  try:
    tal_1 = input("skriv första talet: ")
    tal_2 = input("skriv andra talet : ")
    svar = float(tal_1) + float(tal_2)
    print(svar)
  except:
     print("skriv ett tal tack")


def subtraktion():
    tal_1 = input("skriv första talet: ")
    tal_2 = input("skriv andra talet : ")  
    svar = float(tal_1 )- float(tal_2)
    print(svar)


def multiplication():
    tal_1 = input("skriv första talet: ")
    tal_2 = input("skriv andra talet : ")  
    svar = float(tal_1 )* float(tal_2)
    print(svar)


def divition():
    tal_1 = input("skriv första talet: ")
    tal_2 = input("skriv andra talet : ")  
    svar = float(tal_1 )- float(tal_2)
    print(svar)

way = input("vilket räknesät vill du anvenda + - / elletr *:")

if way == "+":
    addition()

elif way == "-":
   subtraktion()

elif way == "*":
   multiplication()

elif way == "/":
   divition()