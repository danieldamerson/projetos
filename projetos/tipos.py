descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip().upper()

if cupom == "DESCONTO10":
  preco = preco - preco*0.10 
  
elif cupom == "DESCONTO20":
  preco = preco - preco*0.20 
  
elif cupom == "SEM_DESCONTO":
  preco = preco - preco*0.00
  
else:
  print("Operação inválida")
# TODO: Aplique o desconto se o cupom for vá