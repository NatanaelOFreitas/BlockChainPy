# ⛓️ BlockChainPy

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Uma implementação robusta e didática de uma estrutura de **Blockchain** desenvolvida em Python. Este projeto desmistifica o funcionamento por trás das criptomoedas, focando em integridade de dados e algoritmos de consenso.

---

## 🧐 O que é este projeto?

O **BlockChainPy** é um laboratório de estudos sobre registros distribuídos. Ele simula como blocos de informações são encadeados de forma que qualquer alteração em um bloco anterior invalide toda a estrutura subsequente, garantindo a segurança da informação através de criptografia SHA-256.



## 🚀 Funcionalidades Atuais

- [x] **Gênesis Block:** Geração automática do bloco inicial da rede.
- [x] **Mineração (Proof of Work):** Sistema de dificuldade ajustável para minerar novos blocos.
- [x] **Imutabilidade:** Qualquer alteração nos dados altera o Hash, quebrando a corrente.
- [x] **Cadeia de Custódia:** Cada bloco armazena o hash do bloco anterior (`previous_hash`).

## 🛠️ Tecnologias e Conceitos

| Tecnologia/Conceito | Aplicação |
| :--- | :--- |
| **Python 3.8+** | Core do desenvolvimento e lógica do sistema. |
| **SHA-256** | Algoritmo de espalhamento para garantir unicidade. |
| **Nonce** | Número arbitrário usado para encontrar o Hash válido na mineração. |
| **JSON** | Formatação dos dados do bloco para persistência/exibição. |

## 📦 Como Instalar e Usar

### Pré-requisitos
* Python 3.8 ou superior instalado.

### Instalação
```bash
# Clone o repositório
git clone [https://github.com/NatanaelOFreitas/BlockChainPy.git](https://github.com/NatanaelOFreitas/BlockChainPy.git)