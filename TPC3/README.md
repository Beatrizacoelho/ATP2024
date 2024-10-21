# Trabalho de casa 3
O programa define um jogo onde o jogador e o computador alternam entre si para tirar fósforos de um total de 21, sendo o objetivo do computador forçar o jogador a retirar o último fósforo e perder o jogo.

Foi definida inicialmente a junção jogar que recebe o primeiro_jogador como variável. Esta função controla o fluxo principal do jogo, indicando quem começa o jogo (usuário ou computador). O jogador_atual é definido pelo parâmetro primeiro_jogador. 

Enquanto que o número total de fosforos que não for retirado for superior a 0, o jogo continua (utilização de um ciclo while). 

Se o jogador atual for o usuário (jogador_atual == 'usuario'), o usuário escolhe quantos fósforos deseja tirar (de 1 a 4). O programa valida a entrada. Assim, se o jogador escolher um número fora do intervalo ou maior que o número de fósforos restantes, é solicitada uma nova jogada até que ela seja válida. O número de fósforos retirados (entrada) é subtraído do total. Se o total de fósforos restantes chegar a 0, o jogo termina, e o jogador perde, pois retirou o último fósforo.

Se for a vez do computador (jogador_atual == 'computador'), é utilizada a função jogada_computador (explicada a seguir) para determinar quantos fósforos retirar. O número de fósforos retirados pelo computador é exibido, e os fósforos são subtraídos do total. Se o total de fósforos restantes chegar a 0, o jogador vence, porque o computador tirou o último fósforo.

Após cada jogada, o jogador atual alterna: se era o usuário, passa a ser o computador, e vice-versa.

De seeguida foi definida a função jogada_computador(fosforos). Esta função define a estratégia do computador. O objetivo do computador é tentar fazer com que o número de fósforos restantes seja um múltiplo de 5 após sua jogada, colocando o usuário em uma posição de desvantagem. Isto acontece porque a jogada do computador é calculada pela expressão (fosforos - 1) % 5. Se o número de fósforos não permitir que o computador mantenha um múltiplo de 5 (isto é, se a jogada calculada resultar em 0), o computador escolhe uma jogada aleatória entre 1 e 4, usando a função random.randint (tendo sido importado um random no inicio da função).

Por fim, foi definida a função main que é responsável por configurar o jogo, permitindo ao usuário escolher quem começa, podendo escolher entre o modo 1 ou o modo 2 (sendo a escolha validada pelo programa, de forma a garantir que o valor seja um destes dois). Se o usuário escolher a opção 1, o jogo começa com o jogador. Se a opção for 2, o jogo começa com o computador.