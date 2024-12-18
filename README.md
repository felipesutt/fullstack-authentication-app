# Projeto de Controle de Acesso a Dados Ambientais

Este projeto tem como objetivo implementar um sistema de controle de acesso a informações estratégicas sobre propriedades rurais que utilizam agrotóxicos proibidos, com foco em proteger os lençóis freáticos e ecossistemas aquáticos. O sistema possui diferentes níveis de acesso, permitindo que usuários consultem informações com base em suas permissões.

## Estrutura do Projeto

O projeto é dividido em duas partes principais:

### 1. Backend

O backend é desenvolvido em Django e utiliza um banco de dados PostgreSQL hospedado no Neon. O sistema de autenticação é personalizado, permitindo níveis de acesso variados para os usuários.

#### Tecnologias Utilizadas

- Django
- Django Rest Framework
- PostgreSQL
- Python

#### Configuração do Backend

Antes de iniciar a configuração do backend, verifique se o python 3.10 está instalado corretamente no sistema
OBS: A chave do banco de dados não está contida nesse repositório

1. **Clone o repositório:**

```bash
git clone https://github.com/felipesutt/fullstack-authentication-app
cd seu_repositorio/backend
```

2. **Execute o seguinte comando para instalar as dependencias:**

```bash
pip install -r ./requirements.txt
```

3. **Popule o banco de dados (somente caso não haja dados):**

```bash
python manage.py seed_data
```

4. **Inicie o servidor:**

```bash
python manage.py runserver
```

### 2. Frontend

O frontend é desenvolvido usando Electron, React e Vite, proporcionando uma interface de usuário responsiva e dinâmica.

#### Tecnologias Utilizadas

- Electron
- React
- Vite
- Tailwind CSS
- Axios

#### Configuração do Frontend

1. **Navegue até o diretório do frontend:**

```bash
cd seu_repositorio/frontend
```

2. **Instale as dependências:**

```bash
npm install
```

3. **Inicie o aplicativo Electron:**

```bash
npm run dev
```
