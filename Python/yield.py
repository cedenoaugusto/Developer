def contador(max):
    print("\tDentro de contador - empezando")
    n=0
    while n < max:
        print(f"\tDentro de contador - viene yield con n={n}")
        yield n # pseudoequivalente a un return
        print("\tDentro de contador - retomando después de yield")
        n=n+1
    print("\tDentro de contador - terminando")

print("Instanciando contador") 
mycont = contador(3)
print("Contador instanciado") 

for i in mycont:
    print(f"valor leido del iterador={i}") 
print("Fin") 