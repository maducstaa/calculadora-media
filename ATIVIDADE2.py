# naruto style

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = (nota1 + nota2 + nota3) / 3

if media < 2:
    print("Estudante da academia ninja!")
elif media >= 2 and media <= 4:
    print("Você é um(a) Genin!")
elif media > 4 and media <=6:
    print("Você é um(a) Chounin!")
elif media > 6 and media <= 8:
    print("Você é um(a) Jounin!")
elif media > 8 and media <=10:
    print("Você é o(a) mestre Hokage!")
else:
    print("Média fora dos parâmetros permitidos (entre 0 e 10)")
    
print(r"""
      Entre 0 e 1,9 pontos de média: Estudante da academia
      Entre 2 e 3,9 pontos de média: Genin
      Entre 4 e 5,9 pontos de média: Chounin
      Entre 6 e 7,9 pontos de média: Jounin
      Entre 8 e 10 pontos de média: mestre Hokage""")
