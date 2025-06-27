# Entrada do usuário
email = input().strip()
lista= ["@","gmail",".","com"]
listad= ["@","outlook",".","com"]

# TODO: Verifique as regras do e-mail:
if (lista or listad) and "@" in email:
  if "@" == email[0] and email[-1]:
    print("Email inválido")
  else:
    print("Email válido")
else: 
  print("E-mail inválido")

