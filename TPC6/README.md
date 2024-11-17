# Trabalho de casa 6- Sistema de gestão de alunos

Com este trabalho de casa pretende-se a criação de uma aplicação de gestão de alunos que permite criar turmas, adicionar alunos as turmas, listar informações de turmas e alunos, e salvar e recuperar turmas de um arquivo.

Esta aplicação recebe dois dados princpais:
- Escola: uma lista de turmas, onde cada turma é um tuplo que contém o nome da turma e uma lista de alunos.
- Aluno: representado por um tuplo contendo o nome, o ID, e uma lista de três notas do aluno.

Foram criadas as seguintes funções para o desenvolvimento desta aplicação:

1. MostrarMenu(): Exibe as opções do menu para o usuário. Este menu permite navegar pelas principais funcionalidades da aplicação, como criar turmas, listar alunos, consultar alunos por ID, entre outros.
   Esta função recorre a utilização da função `Menu()`, que é responsável por controlar o fluxo principal da aplicação, chamando as funções apropriadas de acordo com a escolha do usuário.
2. existeturma(nome_turma, escola): Verifica se uma turma já existe na lista de turmas.
3. CriarTurma(nome_turma, escola): Adiciona uma nova turma à escola, caso a turma não exista.
4. inserir_aluno(nome_turma, aluno): Insere um aluno numa turma específica. Isto acontece caso o ID do aluno não exista na turma, ou seja, se  o ID for único, ele adiciona o aluno à lista.
5. listar(nome_turma): Lista todos os alunos de uma turma específica, exibindo o nome, ID e notas de cada aluno. 
6. consultar_aluno(id_aluno, nome_turma): Procura um aluno pelo seu ID em uma turma específica. Se o aluno for encontrado, exibe suas informações, caso contrário, informa que o aluno não foi encontrado.
7. guardar_turma(nome_turma, fnome): Salva os dados de uma turma em um arquivo de texto.
8. recuperar_turma(fnome): Recupera os dados de uma turma de um arquivo de texto e retorna uma lista de alunos com seus respectivos dados.

NOTA: O arquivo em que as turmas são salvas armazena as informações de cada aluno em uma linha com o formato `Nome,ID#NotaTPC,NotaProj,NotaTeste`. Esse formato é usado tanto para gravar quanto para ler as informações.

Para a utilização de determinadas opções (escolhidas pelo usuário na utilização da aplicação) deverão ser seguidos os seguintes passos:
- Criar Turma: Escrever o nome de uma nova turma para adicioná-la à escola.
- Inserir Aluno: Escolher uma turma e insirir os dados do novo aluno (nome, ID e notas).
- Consultar Aluno por ID: Inserir o ID do aluno em uma turma específica, cujas informações pretendemos consultar.