# linha 01
opcao = False
# A variável opcao é definida como False.

# linha 02
numero = 1
# A variável numero é definida como 1.

# linha 03
texto = "1"
# A variável texto é definida como a string "1".

# linha 04
resultado = (opcao and not opcao)
# A expressão (opcao and not opcao) será False and True, que resultará em False. Então, resultado será False.

# linha 05
numero = numero + 2
# numero agora será 1 + 2, resultando em 3.

# linha 06
resultado = (numero >= 2) or resultado
# A expressão (numero >= 2) é verdadeira (3 >= 2), então o resultado é True. Como True or False é True, resultado agora é True.

# linha 07
numero = 1
# numero é redefinido como 1.

# linha 08
resultado = (numero == texto) and resultado
# Em Python, a comparação entre "numero" (int) e "texto" (str) é sempre False, pois são de tipos diferentes.
# Portanto, mesmo que o valor de 'numero' e 'texto' seja o mesmo, a expressão (numero == texto) é False.
# Como False and True é False, resultado agora é False.

# linha 09
print(resultado)
# A função print() é chamada para imprimir o valor de resultado.
