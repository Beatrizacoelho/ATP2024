# Trabalho de casa 8

A relização deste trabalho de casa foi feita e três partes:
- TPC1: realização de funções que fazem recurso listas em compreensão.
- TPC2: criação de algumas funções com objetivos especificos.
- TPC3: criação de uma funções de manipulação  e consulta dos dados contidos no dicionário rede social.

Para ser mais fácil a exploração destes trabalhos de caso, vamos especificar o que cada função faz:
1. **TPC1 (a)**: esta função juntar numa nova lista os elementos que não são comuns as duas listas que esta recebe. A lista em compreensão ncomuns, combina a soma de duas lista em compreensão para incluir dois casos: os elementos de lista1 que não estão em lista2 e os elementos de lista2 que não estão em lista1.

2. **TPC2 (b)**: esta função retorna uma lista de palavras com mais de três letras presentes num texto. Esta lista em compreensão faz recurso a funcionalidade split para dividir o texto em palavras e retorna as palavras que têm um comprimento superior a 3 letras. 

3. **TPC3 (c)**: esta função permite retornar uma lista de tuplos com o indice e os elementos da lista fornecida. A lista em compreensão recebe assim as palavras de uma lista e retorna uma lista nofva onde são inseridos tuplos com o seu index+1 da palavra, de forma a evitar o 0, e a própia da palavra. 

4. **TPC2 (a)**: esta função recebe uma string e uma substring e retorna o número de vezes que a substring aparece na string.

5. **TPC2 (b)**: esta função pretende calcular o menor produto que for possível multiplicando os 3 menores inteiros da lista. Assim, esta recebe uma lista de números e organiza-a de menor para maior(sort), calculando de seguida o produto entre os 3 menores números (os números de indice 0, 1 e 2), retornando o resultado.

6. **TPC2 (c)**: esta função reduz um número inteiro positivo a um único dígito, somando repetidamente os dígitos do número até que reste apenas um dígito. Para isso é definida a variável soma, para cada etapa é calculada a soma dos dígitos do número, sendo este atualizado para o valor dessa soma.

7. **TPC2 (d)**: esta função procura a posição de uma substring (s2) dentro de uma string (s1). Para isso, se s2 estiver presente em s1, é utilizado o método index para retornar a posição da primeira ocorrência de s2 em s1. Caso contrário, a função retorna -1, indicando que a substring não foi encontrada. 

8. **TPC3 (a)**: esta função verifica quantos post existem, iniciando a contagem n em 0, adicionando 1 por cada post existem no dicionário redeSocial.

9. **TPC3 (b)**: esta função verifica quantos posts de certo autor existem pesquisando pelo seu nome. Se para um determinado post o autor for o autor que é procurado (post['autor'] == autor), o post é adicionado a uma nova lista. No fim, é retornada a lista de todos os posts daquele autor.

10. **TPC3 (c)**: esta função retorna uma lista de autores de posts ordenada alfabeticamente. Assim, esta lê a lista redeSocial, adicionando uma nava lista autores de posts que ainda não estão incluidos nessa mesma lista, o que evita a existência de nomes duplicados. No fim, antes da lista ser retornada os nomes dos autores são organizados alfabeticamente utilizando a funcionalidade sort.

11. **TPC3 (d)**: esta função acrescenta um novo post a lista redeSocial. Esta recebe como parâmetros: redeSocial e o conteudo, autor, dataCriacao e comentarios do novo post. Criada a lista nova_postagem com as informações fornecidas para o novo post, acrescentando apenas o ID, no formato 'pX', onde X é o número total de posts incrementado em 1 (assumindo que a função quantosPost retorna o total de posts atuais). O novo post é adicionado à lista redeSocial com o método .append(). No fim, a função retorna a lista redeSocial atualizada. 

12. **TPC3 (e)**: esta função recebe um ID e remove da lista redeSocial o post com esse ID. Esta recebe como parâmetros: redeSocial e o id do post que deve ser removido. A função percorre cada elemento (post) em redeSocial, comparando a chave 'id' do post atual com o valor fornecido em id. Se o 'id' do post corresponder ao valor especificado, o post é removido da lista usando a funcionalidade remove. A função retorna a lista atualizada com o post removido. 

13. **TPC3 (f)**: esta função retorna uma lista de tuplos em que o primeiro elemento corresponde ao nome do autor e o segundo a um post desse mesmo autor (autor, post). Para isso, esta função recebe como parâmetros apenas a lista redeSocial. Inicialmente é criada uma lista vazia. De seguida é percorrido cada post na lista redeSocial. Para cada post é adicionado a nova lista o respetivo tuplo. No fim, a função retorna a lista de tuplos. 

14. **TPC3 (g)**: esta função recebe um autor e retorna uma lista de posts comentados por esse mesmo autor. Para isso, a função recebe como parâmetros: redeSocial e o autor. Inicialmente é criada uma nova lista vazia. De seguida, é percorrido cada post da lista redeSocial. Dentro de cada post, a lista de comentários é percorrida (post['comentarios']), verificando se se o autor do comentário corresponde ao autor fornecido (comentario['autor'] == autor). Se for encontrado um comentário do autor especificado, o post desse comentário é adicionado à nova lista. No fim, a função retorna a nova lista, contendo os posts nos quais o autor especificado fez comentários.