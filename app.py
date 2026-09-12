#desconto progressivo para loja online
#gabriely cezario

# entrada de dados
valor_compra = float(input("Digite o valor total da compra: R$ "))

#processamento de dados:
#verifica qual desconto deve ser aplicado
if valor_compra < 200:
    desconto = 0.05
elif valor_compra < 300:
    desconto = 0.10
else:
    desconto = 0.15

#calcula o valor do desconto
valor_desconto = valor_compra * desconto

#calcula o valor final da compra
valor_final = valor_compra - valor_desconto

#saida de danos: 
print(f"\nValor da compra: R$ {valor_compra:.2f}\nDesconto aplicado: R$ {valor_desconto:.2f}\nValor total a pagar: R$ {valor_final:.2f}")