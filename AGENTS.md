# AGENTS.md — Instruções do projeto

## Sobre o projeto

Estudos do curso **Estruturas de Dados e Algoritmos + LeetCode** (Augusto Galego), em Python.
Cada módulo do curso corresponde a uma pasta numerada:

- `2 - Overview das estruturas de dados/`
- `3 - Arrays/`
- `4 - Linked List/`
- `5 - Sorting/`
- `6 - Binarios/`
- `7 - Binary Trees/`
- `8 - Grafos/`
- `9 - Stack/`
- `10 - Heap/`
- `11 - LeetCode/`

Cada pasta pode ter arquivos `.py` (implementações), `notas.md` (anotações do aluno) e arquivos `.docx`.

## Criando arquivos Explicação.md

### Regra de escopo

- Criar ou atualizar `Explicação.md` **somente em pastas que contenham arquivos `.py`**.
- Pastas que só têm `notas.md`/`.docx` **não** recebem `Explicação.md`.
- Um `Explicação.md` cobre **todos** os algoritmos `.py` da pasta. Quando um novo `.py` for adicionado, atualizar o `Explicação.md` existente com a nova seção.
- **Não modificar** os arquivos `.py` — apenas ler e documentar.

### Corrigindo bugs nos `.py` (pedido explícito do aluno)

- A regra acima vale para o fluxo de **documentação**. Quando o aluno **pedir explicitamente** para corrigir um `.py`, o fluxo é: reproduzir o bug com um teste (RED) → corrigir → ver testes passarem (GREEN) → **atualizar** o `Explicação.md` correspondente (referências de linha e trechos que citem o bug).
- Testes automatizados ficam em `tests/test_algorithms.py` (biblioteca padrão `unittest`). Rode com: `python -m unittest tests/test_algorithms.py`.
- Depois de corrigir, rodar o `.py` diretamente para confirmar a saída real.

### Idioma e tom

- Sempre em **português**.
- Tom didático, como um professor explicando para um programador júnior, com calma.
- Explicar o conceito antes de mostrar código; usar exemplos concretos.

### Estrutura padrão de cada seção de algoritmo

Para cada algoritmo encontrado nos `.py`:

1. **O que é** — conceito em linguagem simples, sem jargão desnecessário.
2. **Passo a passo** — traçar um exemplo numérico curto à mão, mostrando como os dados mudam a cada iteração/recursão.
3. **Ilustração Mermaid** — diagrama embutido em bloco ```mermaid (fluxogramas, árvores de recursão, diagramas de ponteiros). Renderiza nativamente no GitHub e no Obsidian.
4. **Complexidade** — Big O de tempo e espaço.
5. **Referência ao arquivo** — função + número das linhas, no formato `arquivo.py:linha`.
6. **Para saber mais** — links para conteúdo externo sobre o algoritmo (Wikipédia em português, artigos, visualizadores animados como o VisuAlgo). O aluno prefere **links de estudo** em vez de apontar erros no código.

### Checklist ao finalizar

- Reler o `.md` conferindo:
  - referências de linha corretas (bater com o arquivo `.py` real);
  - exemplos numéricos corretos;
  - sintaxe Mermaid válida;
  - formatação markdown (títulos, tabelas, blocos de código).
- Confirmar que nenhum `.py` foi alterado.
