#preco_alimentos = {
    "uva":10,
    "banana": 20,
    "batatinha":30
}
#data = {nome: 
        preco for nome,
        preco in preco_alimentos.items()
        if preco > 20}

#print(data)


#precos = [10,20,30,40]

#novo_preco = [preco*2 for preco in precos if preco*2 >20]
#print(novo_preco)
#data = "disponivel"

#podemos_ofertar = True if data == "disponivel" else False
#print(podemos_ofertar)

lista_tuplas = [("uva", 10), ("banana", 20), {"batatinha": 30}]
novo_dict = {key: value for key, value in lista_tuplas}
print(novo_dict)