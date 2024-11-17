# Trabalho de Casa 7 - Análise Meteorológica

Neste trabalho de casaé pretendida a criação de uma aplicação em Python que permita analisar dados meteorológicos diários, como temperaturas mínima e máxima, amplitude térmica, precipitação, entre outros, oferecendo também funcionalidades para calcular estatísticas meteorológicas e gerar gráficos de temperatura e precipitação com base em uma tabela de dados meteorológicos.

A aplicação possui um menu que nos permite selecionar, dentro das seguintes opções, o que pretendemos fazer:

1. Temperatura média: permite calcular a temperatura média diária partindo das temperaturas mínima e máxima registradas.
2. Guardar tabela: Guarda a tabela de dados meteorológicos em um arquivo de texto.
3. Carregar a tabela: Carrega uma tabela de dados meteorológicos a partir de um arquivo de texto.
4. Temperatura mínima mais baixa: Exibe a menor temperatura mínima registrada.
5. Amplitude média térmica: Calcula a amplitude térmica diária.
6. Precipitação máxima: Identifica o dia e o valor da maior precipitação registrada.
7. Dias com precipitação superior a um valor `p`: Exibe os dias onde a precipitação foi maior que um valor fornecido (`p`).
8. Maior número consecutivo de dias com precipitação abaixo de `p`: Calcula o maior período consecutivo de dias com precipitação abaixo de um valor fornecido (`p`).
9. Gráficos de temperatura máxima, mínima e precipitação: Gera gráficos de linhas e de barras para a temperatura e precipitação, respetivamente.
0. Sair: Encerra a aplicação.

Para a utilização de determinadas opções o usuário terá que fornecer determinadas informações, por exemplo, para as opções 7 e 8, o usuário deverá fornecer um valor de precipitação (`p`).

Para a criação de cada uma destas opções foram geradas as seguintes operações:

- mostrar_menu: Exibe o menu de opções.
- medias(tabMeteo): Recebe uma tabela e calcula a média diária da temperatura.
- guardatabMeteo(t, fnome): Recebe uma tabela e o nome do ficheiro, e salva a tabela meteorológica em um arquivo de texto.
- carregatabMeteo(fnome): Recebe o nome do ficheiro (arquivo de texto), carregando as informações nele presentes.
- minMin(tabMeteo): Recebe uma tabela e encontra a temperatura mínima mais baixa.
- amplTerm(tabMeteo): Recebe uma tabela e calcula a amplitude térmica diária.
- maxChuva(tabMeteo): Recebe uma tabela e identifica o dia e o valor da precipitação máxima.
- diasChuvosos(tabMeteo, p): Recebe uma tabela e um valor para a precipitação e lista os dias com precipitação superior ao valor `p`.
- maxPeriodoCalor(tabMeteo, p): Recebe uma tabela e um valor para a precipitação e calcula o maior número consecutivo de dias com precipitação abaixo do valor `p`.
- grafTabMeteo(t): Recebe uma tabela e gera gráficos de temperatura mínima e máxima e de precipitação.

Para serem fornecidas as informações para as funções acima listadas podem ser criadas tabelas de meteriologia (listas de tuplos) com a seguinte estrutura:


```python
tabMeteo1 = [
    ((2022, 1, 20), 2, 16, 0),
    ((2022, 1, 21), 1, 13, 0.2),
    ((2022, 1, 22), 7, 17, 0.01)]
```

NOTA: cada tuplo recebe as informações na seguinte ordem:`((ano, mês, dia), temperatura mínima, temperatura máxima, precipitação)`
