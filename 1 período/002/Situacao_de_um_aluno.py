nota_01=float(input())
nota_02=float(input())
nota_03=float(input())

media= (nota_01+nota_02+nota_03)/3

#A media do aluno foi (media) e ele foi (situaçao)

if media>=70:
    print("A media do aluno foi {:.2f} e ele foi APROVADO".format(media))
elif media>0 and media<40:
    print("A media do aluno foi {:.2f} e ele foi REPROVADO".format(media))
elif media>40 and media<70:
    print("A media do aluno foi {:.2f} e ele foi FINAL".format(media))
else:
    print("Media invalida")