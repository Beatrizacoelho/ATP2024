sala1 = (150, [], "Twilight")
sala2 = (200, [], "Hannibal")
cinema1 = []

def listar(cinema):
    lista=[]
    for sala in cinema:
        lista.append(sala[2]) #Adiciona o nome do filme a lista
    return sala #retorna a lista de filmes

def disponível(cinema,filme,lugar):
    res = False
    for sala in cinema:
        if filme==sala[2]:
            if lugar not in sala[1]:
                res=True
    return res 

def vendebilhete(cinema,filme,lugar):
    if disponível(cinema,filme,lugar):
        for sala in cinema:
            if filme==sala[2]:
                sala[1].append(lugar)
    return cinema

def listardisponivel(cinema):
    lista2=[]
    for sala in lista:
        info=(sala[2],sala[0]- len(sala[1]))
        lista2.append(info)
    return lista2

def inserirsala(cinema,sala):
    if sala not in cinema:
        cinema.append(sala)
    return cinema

def menu():
    print('''(1) listar(cinema)
          (2) disponível(cinema,filme,lugar)
          (3) vendebilhete(cinema,filme,lugar)
          (4) listardisponível(cinema)
          (5) inserirlista(cinema,sala)'''
          )

num=int(input("Escreva a sua opção"))

if num==1:
    filmes = listar(cinema1)
    for filme in filmes:
        print(filme)

if num==2:
    cinema=str("Escolha o cinema")
    filme=input("Qual é o filme que quer ver?")
    lugar=int(input("Escolha o lugar"))
    cond=disponível(cinema1,filme,lugar)
    if cond:
        print("O seu lugar está disponível")
    else:
        print("Não está")

if num==3:
    cinema=str("Escolha o cinema")
    filme=input("Qual é o filme que quer ver?")
    lugar=int(input("Escolha o lugar"))
    
    vendebilhete(cinema,filme,lugar)
    print("Bilhete vendido para o filme " + str(filme) + ", lugar " + str(lugar))

if num==4:
    print(listardisponivel(str(input("Escolha o cinema"))))

if num==5:
    cinema=str(input("Escolha o cinema"))
    num_lugares=int(input("Insira o número de lugares"))

    n=int(input("Quantos lugares ocupados queres adicionar?"))
    lista=[]
    for num in range(n):
        num=int(input("Qual o número do lugar?"))
        lista.append(num)
    
    filme=str(input("Insira o filme: "))
    sala=(num_lugares,lista,filme)
    inserirsala(cinema,sala)

