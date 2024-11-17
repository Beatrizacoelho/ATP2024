# Trabalho de casa 5 - Gestor de um cinema

O programa implementa uma aplicação para a gestão de um conjunto de uma sala de cinemas, permitindo o gerenciamento de filmes, lugares disponíveis e vendas de bilhetes. Utilizando uma estrutura onde cada sala é representada como uma lista contendo a capacidade máxima de lugares, uma lisda dos lugares ocupados, estando esta inicialmente vazia, e o nome do filme em exibição na respetiva sala. Todas as salas adicionadas pelo utilizador são armazenadas em uma lista principal que representa o cinema.

As principais funcionalidades da aplicação são as seguintes: 

1. listar(cinema): recebe a lista cinema e permite visualizar os nomes dos filmes em exibição nas salas.
2. disponível(cinema,filme,lugar): recebe a lista cinema, qual o filme e qual o lugar que é pretendido e verifica se este se encontra disponível.
3. vendebilhete(cinema,filme,lugar): recebe a lista cinema, qual o filme e qual o lugar que é pretendido e marca esse lugar como ocupado em na sala caso esteja disponível para o filme desejado.
4. listardisponivel(cinema): recebe a lista cinema e mostra a quantidade de lugares disponíveis para cada filme em exibição.
5. inserirsala(cinema,sala): recebe a lista cinema e a nova sala que pretendemos acrescentar e adiciona-a, especificando o número de lugares, os lugares ocupados inicialmente e o filme em exibição.

Para que o programa possa interagir com o utilizador foi desenvolvido um menu que permite ao usuário escolher entre as operações disponíveis, garantindo interação dinâmica e facilidade de uso.