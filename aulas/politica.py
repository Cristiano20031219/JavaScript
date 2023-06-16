array = ["presidente","governador","senador","deputado_federal","deputado_estadual"]
print(array)
entrada = str(input("digite qual categoria voce quer "))
if entrada == "0":
    print("O nome do atual predidente é Luiz inacio lula da Silva ")

elif entrada == "1":
    print("governador")
    estado = str(input("informe o estado que quer saber "))

elif entrada == "2":
    print("senador")

elif entrada == "3":
    print("deputado_federal")
    
elif entrada == "4":
    print("deputado_estadual")
#print(len(test))
#print(array[0])