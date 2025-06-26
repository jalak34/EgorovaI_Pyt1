
def fizz_buzz(n):
    
    if (n % 3 == 0) and (n % 5 != 0):
      return("Fizz")
      
    if (n % 5 == 0) and (n % 3 != 0):
      return("Buzz")

    elif (n % 3 == 0) and (n % 5 == 0):
      return("FizzBuzz")

    else:
     return("Не делится на 3 и 5")

print(fizz_buzz(15))




    

  
  

