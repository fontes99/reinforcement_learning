# Taxi Driver
O agente criando no arquivo `Taxi.py` consegue, recebendo dados do ambiente, nos dizer qual sequencia de ações o taxi tem q executar para que se consigo levar um passageiro de um ponto qualquer até outro.

## Estado
O estado é um objeto de uma classe que implementa a interface `State`. Nele encontramos a descrição do ambiente, seu mapa, as coordenadas das posições possíveis e a operação que gerou esse estado.

A descrição do ambiente são quatro variáveis: coordenadas *x* e *y* do taxi, índice do passageiro e índice do destino. Os índices servem para que o agente saiba em que posições estão o passageiro e o destino.

Existem 4 posíveis posições: R, G, Y e B, cada um contento índice 0, 1, 2, 3 respectivamente. Quando o passageiro está dentro do Taxi, seu índice é 4.

O mapa é uma matrix quadrada que descreve por onde o Taxi pode passar ou não passar (representado por `:` e `|` respectivamente) e onde estão os pontos R, G, Y e B.

## Sucessores

Os sucessores são gerados a partir de 6 possíveis ações que o taxi pode realizar: 0 = south, 1 = north, 2 = east, 3 = west, 4 = pickup e 5 = dropoff. Para as 4 primeiras, checa-se se o Taxi não está nas bordas do mapa e se não existe uma parede que impediria o movimento desejado. Para as duas últimas, checa-se a posição do taxi com a posição do passageiro para *pickup* e, para *dropoff*, a posição do taxi com o destino mais o índice do passageiro, que tem que ser 4 para indicar que ele já está no taxi.

## Heurística

A heurística escolhida foi a distância euclidiana. Ela nos diz a distância mais curta entre o taxi e seu destino, portanto ela será sempre menor ou igual ao valor real.

Para calcular a heurística nesse problema, primeiro checamos se o passageiro está ou não no taxi. Se estiver, retornamos a distância euclidiana do taxi até o destino. Se o passageiro não estiver no taxi, retorna-se a distância euclidiana do taxi até ele.

## Arquivo de testes

O arquivo de testes contem 5 testes com 4 *seeds* diferentes. Cria-se o estado com essa *seed* e olhamos se o metodo `path()` está de acordo com o esperado.