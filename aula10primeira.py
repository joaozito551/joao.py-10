nb = ""
pa = float("inf")
sp = 0
for x in range(5):
    medicamneto = input(f"digite o nome do medicamento: ")
    preço = float(input(f"digite o preço: "))

    if preço < pa:
        pa = preço
        nb = medicamneto
    sp += preço
media = sp/5

print(f"""0 nome do medicamneto mais barato é {nb}
      o preço é {pa}
      a maedida aritimetica é: {media}""")
