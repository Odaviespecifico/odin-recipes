def limpa(a):
    lista = a.split('\n')
    lista_nova = []
    for i in lista:
        if i == '':
            lista.pop(lista.index(i))
        try:
            int(eval(i))
            lista.pop(lista.index(i))
        except:
            pass
        if i != '':
            lista_nova.append(i)

    for i in lista_nova:
        print(f'<li>{i}</li>')

limpa("""1 kg de carne moída (de preferência patinho)
creme de cebola
1 sachê de creme de cebola
cebola
1 cebola media picada
alho
4 dentes de alho picado
cebolinha
cebolinha a gosto
sal
sal a gosto
orégano seco
orégano a gosto
pimenta-do-reino
pimenta a gosto""")