# Projeto Galáxias

## Descrição
Imagine uma plataforma online onde você pode explorar e gerenciar informações sobre diferentes galáxias. Esse é o Projeto Galáxias! Aqui, você pode adicionar, visualizar, editar e até mesmo deletar informações sobre galáxias, como nome, estrela principal, distância da Terra e até mesmo uma imagem representativa.

Para facilitar a interação do usuário, desenvolvemos uma aplicação com uma arquitetura moderna. Utilizamos Flask para o backend, que é a parte que cuida da lógica por trás da aplicação, e HTML com Bootstrap para o frontend, que é a parte visual e interativa que você vê ao acessar o projeto.

## Funcionalidades
Vamos dar uma olhada nas principais funcionalidades do Projeto Galáxias:
- **Cadastro de Galáxias:**
  - Interface Intuitiva: Adicionar uma nova galáxia é fácil e direto. Basta preencher um formulário com informações como o nome da galáxia, sua estrela principal, a distância da Terra em anos-luz e até mesmo adicionar uma imagem representativa.
  - Upload de Imagens: Além de inserir um link para uma imagem, você também pode fazer upload de arquivos de imagem, o que permite uma personalização maior da entrada de dados e enriquece o catálogo visual da aplicação.
- **Listagem de Galáxias:** Todas as galáxias cadastradas são organizadas em uma lista para que você possa visualizá-las facilmente.
- **Edição de Galáxias:** Se alguma informação sobre uma galáxia mudar, você pode atualizá-la facilmente através da nossa interface intuitiva que conta com um botão editar em sua interface.
- **Remoção de Galáxias:** Caso queira remover uma galáxia do nosso catálogo, você pode fazer isso de forma simples e rápida utilizando o botão excluir.

## Tecnologias e Ferramentas
Para criar essa aplicação incrível, utilizamos as seguintes tecnologias:
- **Frontend:** Utilizamos HTML e Bootstrap para criar uma interface bonita e responsiva, que se adapta a diferentes dispositivos, como celulares e computadores.
- **Backend:** Utilizamos Flask, que é um framework em Python, para cuidar da parte lógica da aplicação. O Flask como framework oferece flexibilidade e poder para criar uma aplicação robusta e escalável.
- **Database:** Utilizamos SQLite como sistema de gerenciamento de banco de dados, o que facilita a manipulação e persistência das informações.

## Rotas da Aplicação
Aqui estão as principais rotas da nossa aplicação:
- **GET /:** Essa é a rota principal, onde você pode ver todas as galáxias cadastradas.
- **POST /criar:** Utilize essa rota para adicionar uma nova galáxia ao nosso catálogo. Basta preencher um formulário com os dados necessários.
- **GET /editar/:** Se você quiser editar alguma informação de uma galáxia específica, utilize essa rota para carregar o formulário de edição.
- **PUT /atualizar/:** Utilize essa rota para atualizar os dados de uma galáxia específica. Basta preencher um formulário com as novas informações.
- **DELETE /deletar/:** Se quiser remover uma galáxia do nosso catálogo, utilize essa rota. Basta especificar o ID da galáxia que deseja deletar.

## Equipe de Desenvolvimento
Por trás desse projeto incrível, temos uma equipe dedicada e talentosa:
- **Equipe: Hubble**
  - Erick Soares
  - Gi (preenche aqui)
  - Jéssica Rodrigues
  - Marco Murched
  - Rafael Fidalgo
  - Sáphira Mendes
  - Suellen Costa
