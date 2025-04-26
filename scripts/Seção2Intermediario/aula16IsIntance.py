#Exemplos de IsIntance

exemplo = [
    1, 2, 3, 4, "Derek,"
    
    ]
def mostrar_ints():
    for items in exemplo:
        if isinstance(items, int):
            print(items)

print(mostrar_ints())