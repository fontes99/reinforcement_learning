# 8 Puzzle solver
O arquivo `Puzzle.py` contém uma implementação de agente autônomo para resolver o quebra-cabeça conhecido como *8 puzzle*. A seguir, segue as descrições dessa implementação.

## Estado
O estado é uma classe que implementa a interface `State`, contendo nela uma matriz 3x3 que representa o *8 puzzle* atual e a operação que foi realizada para chegar nessa matriz. 

```
# Exemplo de matriz utilizada no problema

[
    [8, 1, 3],
    [0, 7, 2],
    [6, 5, 4]
]
```

O `0` na matrix representa o espaço em braco do *8 puzzle*, e é nele que são aplicadas as operações.

A operação inicial é vazia, e vai mudando conforme novos estados forem gerados. Os valores admitidos são: `"UP"`, `"DOWN"`, `"LEFT"` e `"RIGHT"`. Essas operações ditam para qual direção o 0 deve ir.

## Sucessores
Para gerarmos os sucessores, primeiro checamos em que posição está o espaço em branco e, a partir daí, geramos todos os próximos estado possíveis. 

Existem 4 sucessores possíveis, sendo um para cada operação. 

### Podagens
Não é gerado nenhum sucessor que fugiria do escopo da matriz 3x3. Por exemplo, se o espaço em branco estiver enconstado na parede da esquerda (coluna 0), não é gerado o sucessor de operação `"LEFT"`, e assim por diante.

Além disso, também não é gerado nenhum sucessor cuja operação é a complementar do gerador. Por exemplo, se o estado atual deu-se pela operação `"DOWN"`, o sucessor de operação `"UP"` não é gerado, para evitar voltas desnecessárias.

## Heurística
A heurística escolhida é uma somatória da distâcia de manhattan de todos as casas entre o estado atual e o estado meta. 

Essa heurística é admissível porque ela pode ser tanto igual ao valor real, sendo que nenhuma peça pode fazer menos que os movimentos da distância de manhattan entre sua posição e sua meta, quanto maior, quando se é necessário fazer um 'desvio' no seu caminho mais curto para acomodar a movimentação de outras peças.

## Checagem da possibilidade de resolução do *puzzle*
Para checar se uma matriz consegue, atravéz dos movimentos préviamente descritos, se transformar em outra, é utilizado o conceito de *paridade*. Uma matriz pode ter um de dois graus de paridade: impar ou par. Uma matriz só pode ser transformada em outra atravéz desses movimentos se tiverem o mesmo grau de paridade.

Para checar o grau de paridade de uma matriz, primeiro transformamos ela em um vetor unidimencional e depois ordenamos o vetor com o algoritmo `bubble sort`. O número de inversões realizadas pelo algoritmo de ordenação nos diz o grau de paridade da matriz.

Se o estado inicial tiver grau de paridade diferente do estado meta, o agente não irá gerar sucessores, imprimindo a mensagem de `"Nao achou solucao"`

## Arquivo de testes
No arquivo `test_8_puzzle.py` existem 5 testes. Um fácil, três difíceis e um impossível de ser resolvido.