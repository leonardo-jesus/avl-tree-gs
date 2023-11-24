"""
Este módulo implementa uma árvore AVL para armazenamento e recuperação eficiente de dados.

Classes:
    AVLNode: Representa um nó em uma árvore AVL.
    AVLTree: Implementa a estrutura da árvore AVL.

Módulos externos necessários:
    - json: Manipulação de dados JSON.
    - timeit: Medição do tempo de execução.
    - matplotlib.pyplot: Geração de gráficos.

Uso:
    1. Crie uma instância da classe AVLTree.
    2. Insira dados na árvore usando o método insert.
    3. Execute test_avl_tree para testar o desempenho da inserção e gerar um gráfico.

Exemplo:
    data_size = 1000
    data = [
        {
            "name": f"Influencer_{i}",
            "age": 25 + i,
            "Works At": f"Company_{i % 5}"
        } for i in range(data_size)
    ]

    test_avl_tree(data)
"""

import json
import timeit
import matplotlib.pyplot as plt

class AVLNode:
    def __init__(self, key, value):
        """
        Inicializa um nó AVL com uma chave e um valor associado.

        Parâmetros:
            key (int): Chave do nó.
            value: Valor associado à chave.
        """
        self.key = key
        self.value = value
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        """Inicializa uma árvore AVL vazia."""
        self.root = None

    def height(self, node):
        """
        Retorna a altura de um nó na árvore.

        Parâmetros:
            node (AVLNode): Nó cuja altura será calculada.

        Retorna:
            int: Altura do nó.
        """
        return node.height if node else 0

    def update_height(self, node):
        """
        Atualiza a altura de um nó com base nas alturas de seus filhos.

        Parâmetros:
            node (AVLNode): Nó cuja altura será atualizada.
        """
        if node:
            node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        """
        Calcula o fator de balanceamento de um nó.

        Parâmetros:
            node (AVLNode): Nó cujo fator de balanceamento será calculado.

        Retorna:
            int: Fator de balanceamento do nó.
        """
        return self.height(node.left) - self.height(node.right) if node else 0

    def rotate_right(self, y):
        """
        Realiza uma rotação para a direita em torno do nó 'y'.

        Parâmetros:
            y (AVLNode): Nó em torno do qual a rotação será realizada.

        Retorna:
            AVLNode: Novo nó raiz após a rotação.
        """
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        """
        Realiza uma rotação para a esquerda em torno do nó 'x'.

        Parâmetros:
            x (AVLNode): Nó em torno do qual a rotação será realizada.

        Retorna:
            AVLNode: Novo nó raiz após a rotação.
        """
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, key, value):
        """
        Insere um novo nó na árvore AVL.

        Parâmetros:
            key (int): Chave do novo nó.
            value: Valor associado à chave.
        """
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        """
        Função auxiliar para realizar a inserção recursiva de um nó na árvore AVL.

        Parâmetros:
            node (AVLNode): Nó atual sendo considerado.
            key (int): Chave do novo nó.
            value: Valor associado à chave.

        Retorna:
            AVLNode: Novo nó raiz após a inserção.
        """
        if node is None:
            return AVLNode(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value
            return node

        self.update_height(node)

        balance = self.balance_factor(node)

        if balance > 1:
            if key < node.left.key:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

        if balance < -1:
            if key > node.right.key:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        return node

def test_avl_tree(data):
    """
    Testa o desempenho da inserção de dados em uma árvore AVL e gera um gráfico.

    Parâmetros:
        data: Dados a serem inseridos na árvore.
    """
    avl_tree = AVLTree()

    def insert_data():
        for i, entry in enumerate(data):
            avl_tree.insert(i, entry)
            print(f"Dados inseridos: {entry}")

    execution_time = timeit.timeit(insert_data, number=2)

    print(f"\033[1;32mInserção de {len(data)} dados em uma árvore AVL: {execution_time:.5f} segundos\033[0m")

    # Plotar a complexidade O(log n)
    sizes = [2**i for i in range(2, 20)]  # Criar tamanhos de entrada exponenciais
    times = []

    for size in sizes:
        sample_data = [
            {
                "name": f"Influencer_{i}",
                "age": 25 + i,
                "Works At": f"Company_{i % 5}"
            } for i in range(size)
        ]

        time_taken = timeit.timeit(lambda: avl_tree._insert(None, size // 2, json.dumps(sample_data[0])), number=100)
        times.append(time_taken)

    plt.plot(sizes, times, label="Real Time Complexity")
    plt.plot(sizes, [times[0] * (size / sizes[0]) * (1 / 100) for size in sizes], label="Theoretical O(log n)")
    plt.xscale("log", base=2)
    plt.yscale("log", base=10)
    plt.xlabel("Size of Input (n)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.show()
    plt.savefig('plot.png')

if __name__ == "__main__":
    data_size = 1000

    data = [
        {
            "name": f"Influencer_{i}",
            "age": 25 + i,
            "Works At": f"Company_{i % 5}"
        } for i in range(data_size)
    ]

    test_avl_tree(data)
