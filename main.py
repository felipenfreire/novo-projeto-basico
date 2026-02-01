print('------ INICIO ------')

pergunta1 = input('Estou com fome? (Digite s para sim ou n para não)')
if pergunta1 == 's':
    pergunta2 = input('Tenho comida em casa(Digite s para sim ou n para não)')
    if pergunta2 != 's':
        print('Ir ao mercado')
        print('Voltar para casa')
    print('Preparar a comida')
    print('Comer a comida')