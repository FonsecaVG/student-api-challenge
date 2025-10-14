# Student API Challenge - Flask/Python

## ✨ Endpoints Funcionais

* **POST /students:** Cadastra estudantes com validação obrigatória da nota (entre 0 e 10).
* **GET /students:** Retorna a lista completa de todos os estudantes.
* **GET /students/:id:** Retorna os dados de um estudante específico (ou 404 Not Found).

## 🧠 Justificativa das Decisões (Decisions Made)


Justificativa decisões:

**Armazenamento de Dados e Estrutura:**
- Justificativa: Armazenamento feito por lista Python global para manter o código em único arquivo (app.py).

**Lógica do Caractere Único (get_unique_char):**
- Justificativa: A função utiliza o método Python string.count() dentro do loop para contar e validar o nº de ocorrência de cada letra.

**JSON e Validação:**
- Justificativa: O Flask é usado para retornar o formato JSON e aplicar a validação da nota.
O uso do jsonify garante que a API siga o padrão RESTful. A validação numérica da nota com (try/except) permite lidar com entradas inválidas do cliente de forma controlada, retornando mensagens de erro (400 Bad Request).

**Verificação de Qualidade**
- Teste: Por fim, a funcionalidade da API foi validada usando a extensão Thunder Client no VS Code, para simular todas as requisições POST e GET, garantindo a precisão da lógica de retorno do caractere único e a correta aplicação dos códigos HTTP (201, 200, 400, 404).


## 🚀 Run Locally
1. Clone o repositório:
    ```bash
    git clone [SEU_LINK]
    cd student-api-challenge
    ```
2. Crie o ambiente virtual e instale:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows
    pip install -r requirements.txt
    ```
3. Inicie a API:
    ```bash
    python app.py
    ```
