final = 8
cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
votoNulo = 0
votoBranco = 0
qtdVotos = 0
porceNulo = 0
proceBranco = 0
vencedor = ''

while (final != 0):
    print('-- Eleições presidenciais: -- ')
    print('|        1- José  42anos      | ')
    print('|        2- Pedro 55anos      | ')
    print('|        3- Maria 50anos      | ')
    print('|        4- João  70anos      | ')
    print('|        5- Voto Nulo         | ')
    print('|        6- Voto Branco       | ')

    final = int(input(
        'De acordo com a tabela acima. Digite um numero para votar ou 0 para encerrar: '))

    if final == 0:
        break

    if final == 1:
        cand1 += 1
    elif final == 2:
        cand2 += 1
    elif final == 3:
        cand3 += 1
    elif final == 4:
        cand4 += 1
    elif final == 5:
        votoNulo += 1
    elif final == 6:
        votoBranco += 1

    qtdVotos += 1
    porceNulo = (votoNulo / qtdVotos) * 100
    proceBranco = (votoBranco / qtdVotos) * 100

    if cand4 >= cand1 and cand4 >= cand2 and cand4 >= cand3:
        vencedor = 'João'
    elif cand3 >= cand1 and cand3 > cand2 and cand3 > cand4:
        vencedor = 'Maria'
    elif cand2 >= cand3 and cand2 >= cand1 and cand2 > cand4:
        vencedor = 'Pedro'
    else:
        vencedor = 'José'


print('-- Tivemos um total de votos:{}'.format(qtdVotos))
print('Candidato José -- {} votos'.format(cand1))
print('Candidato Pedro -- {} votos'.format(cand2))
print('Candidata Maria -- {} votos'.format(cand3))
print('Candidato João -- {} votos'.format(cand4))
print('\nVotos Nulos -- {} votos'.format(votoNulo))
print('Votos Brancos -- {} votos'.format(votoBranco))
print('Porcentagem de votos nulos {:.2f}% '.format(porceNulo))
print('Porcentagem de votos brancos {:.2f}% '.format(proceBranco))
print('\n\n  --- Candidato Vencedor:  {} ----'.format(vencedor))
