<p align="center">
	<h1 align="center">Algoritmo de Inserção em Python</h1>
</p>

<p align="center">
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-requisitos-obrigatórios">Requisitos Obrigatórios</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-pontos-de-melhoria">Pontos de Melhoria</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-complexidade-do-algoritmo">Complexidade do Algoritmo</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-requisitos">Requisitos</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-rodar">Como rodar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-rodar">Como visualizar a documentação do pydoc</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-contribuir">Como contribuir</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-licença">Licença</a>
</p>

<p align="center">
 <img src="https://img.shields.io/static/v1?label=PRs&message=welcome&color=7159c1&labelColor=000000" alt="PRs welcome!" />

  <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=7159c1&labelColor=000000">
</p>

<br>

## 💻 Projeto
O Algoritmo de inserção utiliza **Python** e **Matplotlib**. O algoritmo cria uma *árvore AVL* e irá inserir e mostrar o tempo de execução da inserção em relação da Complexidade Teórica de **Big O(log n)**.

## ✅ Requisitos Obrigatórios
✔️ Linguagem de programação:  a solução deve ser desenvolvida obrigatoriamente em Java ou Python. É proibida a utilização de bibliotecas ou frameworks externos, exceto para interfaces gráficas (GUI) ou desenvolvimento web básico. Qualquer outra exceção deve ser bem justificada na documentação;\
✔️ Orientação a Objetos: é obrigatório que o código respeite as boas práticas de programação orientada a objetos (OOP);\
✔️ Estrutura de Dados: o sistema deve implementar as estruturas de dados adequadas que atendam aos requisitos de performance;\
✔️ Interface com o Usuário: a solução pode ser demonstrada por meio de Prompt de comando;\
✔️ Performance: esses requisitos visam garantir que o sistema não apenas funcione corretamente, mas também o faça de maneira eficiente, mesmo sob alta carga de trabalho:\
        ✔️ 1.000 usuários;\
        ✔️ 10.000 usuários;\
        ✔️ 100.000 usuários.;\
✔️ Buscas devem ser otimizadas, operando em tempo logarítmico;\
✔️ O Tempo médio de busca não deve exceder log2(N);\
✔️ Operações de inserção devem ser otimizadas para garantir um rápido cadastramento;\
✔️ O tempo médio de inserção não deve exceder log2(N);\
✔️ A documentação deve ser clara, objetiva e incluir descrição das funções, métodos e classes implementados (usando javadoc, Pydoc ou equivalentes) e um README.txt detalhando a execução da solução e a justificativa para escolhas técnicas utilizadas.

## 💪 Pontos de Melhoria
- Implementar a boa prática de encapsulamento;
- Adcionar tratamento de exceções.

## 📐 Complexidade do Algoritmo
A complexidade que obtemos com esse algoritmo é de **O(log n)**

<p align="center">1.000 usuários</p>
<h1 align="center">
    <img alt="Output" src="./assets/1k-users.png">
</h1>

<p align="center">10.000 usuários</p>
<h1 align="center">
    <img alt="Output" src="./assets/10k-users.png">
</h1>

<p align="center">100.000 usuários</p>
<h1 align="center">
    <img alt="Output" src="./assets/100k-users.png">
</h1>

## 🚀 Tecnologias
Esse projeto foi desenvolvido com as seguintes tecnologias:

- [**Python**](https://www.python.org/)
- [**Matplotlib**](https://matplotlib.org/)
- [**timeit**](https://docs.python.org/3/library/timeit.html)
- [**pydoc**](https://docs.python.org/3/library/pydoc.html)

## 🔧 Requisitos
Para rodar essa aplicação Python, você apenas irá precisar instalar Python em seu computador.

[**Pyhton**](https://www.python.org/downloads/) é uma linguagem de programação que permite que você trabalhe de maneira rápida e integre sistemas de forma mais eficiente.

## 🏃 Como rodar

1. Faça o clone do projeto;
2. Abra o projeto no seu terminal;
3. Rode `python AVLTree.py` para rodar o código

## 📃 Como visualizar a documentação do pydoc

1. Faça o clone do projeto;
2. Abra o projeto no seu terminal;
3. Rode `pip install matplotlib` para instalar a dependência necessária para visualização do gráfico;
3. Rode `python -m pydoc AVLTree` ou abra o arquivo HTML para visualizar a documentação.

## 🤔 Como contribuir

- Faça um fork;
- Crie uma branch com a sua funcionalidade: `git checkout -b my-feature`;
- Faça um commit com suas alterações: `git commit -m 'feat: My new feature'`;
- Faça o push para sua branch: `git push origin my-feature`.

Depois que o merge do seu pull request for feito, você pode excluir sua branch.

## 📝 Licença

Esse projeto está utilizando a Licença MIT. Olhe a [**LICENÇA**](LICENSE) para mais detalhes.

---

<p align="center">Developed byMedina IT :copyright:</p>
