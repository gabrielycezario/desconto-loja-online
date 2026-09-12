# 🛍️ Desconto Progressivo

Código desenvolvido em **Python** para calcular descontos progressivos em uma loja online de acordo com o valor total da compra.

Solicita ao usuário o valor total da compra e verifica qual desconto deve ser aplicado:

| Valor da compra                      | Desconto |
| ------------------------------------ | -------: |
| Menor que R$ 200,00                  |       5% |
| De R$ 200,00 até menor que R$ 300,00 |      10% |
| R$ 300,00 ou mais                    |      15% |

Depois de identificar o desconto, o programa calcula o valor descontado e o **valor final da compra**.

## 🧮 Fórmulas utilizadas

### Valor do desconto

```text
valor_desconto = valor_compra × desconto
```

### Valor final

```text
valor_final = valor_compra - valor_desconto
```

## ▶️ Como executar

1. Tenha o **Python** instalado no computador.
2. Abra o projeto no **VS Code**.
3. Abra o arquivo `.py`.
4. Execute o programa pelo terminal:

```bash
python nome_do_arquivo.py
```

Ou:

```bash
py nome_do_arquivo.py
```

5. Digite o valor total da compra quando solicitado.

## 💻 Exemplo de execução

```text
Digite o valor total da compra: R$ 250

Valor da compra: R$ 250.00
Desconto aplicado: R$ 25.00
Valor total a pagar: R$ 225.00
```

---

👩‍💻 **Desenvolvido por Gabriely Cezario**