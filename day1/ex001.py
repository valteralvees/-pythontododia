print('Hello world')

#unpacking - desestruturação
nome,idade,curso,signo = 'valter',20,'ADS', 'aquário'

#Sistema online de redirecionamento e chatbot com o aluno UNIT - Magister
nome = input('Qual o seu nome?')
curso = input('Qual o seu curso?')
msg1 = print('Oi,' + nome + "! " + "Seja bem vindo ao MAGISTER da Unit. É um prazer tê-lo conosco." + " Seu curso de " + curso + " Está disponível para consulta no sistema online. O que você deseja fazer? ")

deseja= input("""se deseja emitir uma declaração de matrícula ou
fazer qualquer serviço de sercretaria online, digite SIM:""")
  #aspas triplas permitem quebra de linha

nome2 = nome.upper()

print(f'Então,{nome2}, ao verificar o seu curso de {curso} percebemos que você não tem vínculo ativo para o semestre atual. Deseja renovar sua matrícula? Estamos com ótimos descontos para alunos do signo de {signo}')

print(msg1.split('.'))

# extraindo partes da string
primeiraletra = print(nome[0])

