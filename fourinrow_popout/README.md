# Agente de *Connect 4*

Nesse projeto, foi implementado um agente competitivo para o jogo de *Connect 4* - Pop out utilizando o algoritmo *Min-Max*.

Para implementar esse agente, foi escolhido o algoritmo de *Min-Max* com poda alpha-beta para que possamos ter um tempo de resposta reduzido. Com isso, a jogabilidade do agente passa a ser mais fluida. O tempo de resposta é reduzido pelas podas que o algorítmo faz e pela profundidade da busca. A função de utilidade é definida manualmente.

Esse agente não utiliza de aprendizado de máquina.

A expectativa para o desempenho do agente é que tenha uma classificação mediana. Depois de realizados alguns testes contra outro agente parecido mas com algumas mudanças, ganhou-se quase 55% das vezes.

As principais referências para a implementação do agent são:

- O Código demonstrado em aula
- [Vídeo sobre implementação sobre *Connect 4*](https://www.youtube.com/watch?v=42bkrj19swo)

A principal diferença entre este agente e um de *Connect 4* padrão é a implementação do método `pop()`. Nela, é adicionado aos sucessores as possíveis retiradas de peça do jogador atual de alguma base da coluna e a atualização do novo tabuleiro.

Este agente se adaptaria bem com poucas mudanças para jogar em um contexto de *Connect 4* padrão.

