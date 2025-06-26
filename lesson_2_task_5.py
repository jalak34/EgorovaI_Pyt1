def month_to_season(m):
  if 1 <=m <=2 or m == 12:
    return "зима"
  
  elif 3 <= m <= 5:
    return("весна")
    
  elif 6 <= m <= 8:
    return "лето"
 
  elif 9 <= m <= 11:
    return "осень"
    
  else:
     return("Число должно быть от 1 до 12")
  
print(month_to_season(4))


            




    

  
  

