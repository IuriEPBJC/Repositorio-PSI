# Sistema de Gestão de Builds - League of Iuri

Este projeto organiza e gere informações relacionadas a builds, campeões e posições num universo inspirado no jogo League of Legends. Utiliza SQLite para criar uma base de dados chamada `leagueofiuri.db`.

---

## Estrutura Geral

A base de dados contém as seguintes tabelas principais:

### 1. Tabela `build`
Armazena informações sobre builds, associando-as a campeões e funções.

| Coluna  | Tipo      | Descrição                                                |
|---------|-----------|----------------------------------------------------------|
| `id`    | INTEGER   | Identificador único da build (chave primária).           |
| `build` | TEXT      | Tipo de build (ex.: "attack speed", "tank").             |
| `champ` | INTEGER   | Referência ao ID do campeão (chave estrangeira para `champions`). |
| `roles` | INTEGER   | Referência ao ID da função (chave estrangeira para `posicao`).   |

---

### 2. Tabela `champions`
Armazena informações sobre os campeões e os seus reinos de origem.

| Coluna  | Tipo      | Descrição                                                |
|---------|-----------|----------------------------------------------------------|
| `id`    | INTEGER   | Identificador único do campeão (chave primária).         |
| `nome`  | TEXT      | Nome do campeão (ex.: "Aatrox", "Ahri").                 |
| `reino` | TEXT      | Reino de origem do campeão (ex.: "Runeterra", "Ionia").  |

---

### 3. Tabela `posicao`
Regista as posições ou funções associadas aos campeões.

| Coluna  | Tipo      | Descrição                                                |
|---------|-----------|----------------------------------------------------------|
| `id`    | INTEGER   | Identificador único da posição (chave primária).         |
| `roles` | TEXT      | Tipo de posição (ex.: "mid", "top").                     |
| `champ` | INTEGER   | Referência ao ID do campeão (chave estrangeira para `champions`). |

---

## Scripts Disponíveis

### 1. Criação de Tabelas e Dados
Os seguintes scripts criam as tabelas e populam a base de dados com dados iniciais:

- **`build_create.py`**: Cria a tabela `build` e insere 20 registos de builds associadas a campeões e funções.
- **`champions_create.py`**: Cria a tabela `champions` e insere uma lista de campeões e os seus reinos.
- **`posicao_create.py`**: Cria a tabela `posicao` e insere dados de posições associadas aos campeões.

### 2. Consulta de Dados
Os seguintes scripts permitem consultar os dados da base de dados:

- **`build_read.py`**: Lê e imprime todos os registos da tabela `build`.
- **`champions_read.py`**: Lê e imprime todos os registos da tabela `champions`.
- **`posicao_read.py`**: Lê e imprime todos os registos da tabela `posicao`.

---

## Passo a Passo

### Passo 1: Configurar e Popular a Base de Dados
1. **Certifique-se de que tem o Python 3.x instalado.**
   - Verifique a instalação com o comando:  
     ```bash
     python --version
     ```

2. **Execute os scripts de criação para configurar as tabelas e inserir os dados iniciais.**  
   Execute os seguintes comandos no terminal ou ambiente de desenvolvimento:
   ```bash
   python champions_create.py
   python posicao_create.py
   python build_create.py
