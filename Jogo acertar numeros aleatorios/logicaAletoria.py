import random
import math
 
lower = int(input("Qual o limite minimo? :- "))
 
upper = int(input("Qual o limite maximo? :- "))
 
x = random.randint(lower, upper)
print("\n\tVocê têm somente ", round(math.log(upper - lower + 1, 2))," chances de acertar!\n")
 
 
count = 0
 
while count < math.log(upper - lower + 1, 2):
    count += 1
     
     
    guess = int(input("O número escolhido foi :- "))
     
    
    if x == guess:  
       print("Parabéns você conseguiu fazer isso em apenas", count, " tentativas!")
       
       break
    elif x > guess:
       print("Tente novamente! Você chutou muito baixo!")
    elif x < guess:
       print("Tente novamente! Você chutou muito alto!")
 
if count >= math.log(upper - lower + 1, 2):
   print("\nO número é %d !" % x," Que pena :( Não foi dessa vez!")
  
