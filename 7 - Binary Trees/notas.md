# Binary Trees — Notas

## Progresso

- [x] Árvore binária (`binary_tree.py`): inserção, busca, percursos DFS/BFS
- [ ] BFS em profundidade — parei no P42

## Conceitos

### DFS — Depth First Search (Busca em Profundidade)

Percorre a árvore descendo o máximo possível em um ramo antes de voltar
(backtracking). Usa **pilha** (ou recursão, que é uma pilha implícita).

- **Pré-ordem (preorder):** visita o nó → esquerda → direita
- **Em ordem (inorder):** esquerda → visita o nó → direita
- **Pós-ordem (postorder):** esquerda → direita → visita o nó

### BFS — Breadth First Search (Busca em Largura/Amplitude)

Percorre a árvore por **níveis**: primeiro a raiz, depois os filhos, depois os
netos, e assim por diante. Usa uma **fila (queue)**.

> Ideia-chave: BFS visita os vizinhos mais próximos primeiro. É útil para
> encontrar o caminho mais curto em grafos não-ponderados.
