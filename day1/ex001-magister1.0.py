#Operadores Lógicos e condicionais
print('Welcome to Magister. The system need some informations before we continue. Please, be true about your informations, or your acess wil be NOT granted. ')
print('In this moment, the system is only accepting users that have the letter "V" in their names. Please put attention in this requirement.')
name = input("Insert your name, without accent, if have:")
if name[0] == "V":
  print(f'{name}, your name is eligble for MAGISTER acess. Welcome!')
  course = input("What's your graduation?")
  if course == "ADS" or "Análise e Desenvolvimento de Sistemas":
    print('Your acess is being watched by the Security Sistems Crew. Be attenction to your njavegation in our site. Any attacks to our system can be and will be punished.')

  elif course == "psicologia":
    print('My dear, please go out our site. You are nuts...')
else:
  print('Acess denied')

