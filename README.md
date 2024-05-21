# Historynicius

# Escopo do Projeto

## 1. Introdução

### Visão Geral do Projeto

O projeto consiste no desenvolvimento de um sistema web fullstack para registro e visualização de histórias ou textos. A aplicação permite que os usuários cadastrem novas histórias com informações como título, texto, data de publicação, imagem ilustrativa e categoria. Além disso, oferece funcionalidades de busca, filtragem por categoria e visualização detalhada das histórias.

### Objetivos e Propósito do Sistema

O objetivo principal do sistema é proporcionar uma plataforma intuitiva e eficiente para que os usuários possam registrar e compartilhar suas histórias de forma organizada. O sistema visa promover a criação e o compartilhamento de conteúdo entre os usuários, facilitando a busca e a leitura de histórias de interesse.

### Benefícios Esperados do Projeto

- Facilidade de registro e visualização de histórias.
- Promoção da interação e compartilhamento de conteúdo entre os usuários.
- Organização e categorização eficientes das histórias para uma melhor experiência do usuário.
- Possibilidade de filtragem e busca rápida de histórias por título ou categoria.

## 2. Visão Geral do Sistema

### Descrição do Sistema

O sistema é uma aplicação web desenvolvida utilizando o framework Django, que segue a arquitetura MVC (Model-View-Controller) adaptada para MTV (Model-Template-View). Ele permite que os usuários cadastrem novas histórias, visualizem uma lista de histórias em formato de cards, filtrem as histórias por categoria e acessem detalhes completos das histórias selecionadas.

### Público-Alvo do Sistema

O público-alvo do sistema são pessoas que desejam compartilhar suas histórias e também aquelas que buscam por conteúdo interessante para leitura. O sistema é voltado para uma ampla gama de usuários, desde escritores amadores até leitores ávidos por novas histórias.

### Requisitos Funcionais e Não Funcionais

#### Requisitos Funcionais

- Cadastro de novas histórias com título, texto, data de publicação, imagem ilustrativa e categoria.
- Visualização de lista de histórias em formato de cards.
- Filtragem de histórias por categoria.
- Busca de histórias por título ou categoria.
- Visualização detalhada de cada história.

#### Requisitos Não Funcionais

- Desempenho rápido e responsivo da aplicação.
- Segurança na autenticação de usuários e proteção de dados sensíveis.
- Facilidade de manutenção e escalabilidade do sistema.

## 3. Arquitetura do Sistema

### Explicação da Arquitetura MVT (Model-View-Template)

O sistema segue uma arquitetura MVT (Model-View-Template), onde:

- **Model:** Representa a camada de dados e lógica de negócios. Aqui são definidos os modelos de dados que representam as entidades do sistema, como História e Categoria.

- **View:** Controla a lógica de interação entre o modelo e o template. As views processam as requisições do usuário, interagem com o modelo para obter ou modificar dados e retornam respostas apropriadas ao navegador.

- **Template:** Responsável pela apresentação visual das páginas HTML. Os templates contêm a estrutura da página e inserções de dados dinâmicos utilizando a linguagem de template do Django.

### Papel de Cada Componente

- **Model:** Lida com a manipulação dos dados do sistema, incluindo operações de leitura, escrita, atualização e exclusão. Ele encapsula a lógica de negócios e fornece uma interface para acessar e modificar os dados.

- **View:** Recebe as requisições do navegador e chama os métodos adequados nos modelos para processar os dados. Elas são responsáveis por retornar uma resposta HTTP apropriada, geralmente renderizando um template com os dados necessários.

- **Template:** Define a estrutura visual das páginas HTML, incluindo a apresentação dos dados dinâmicos fornecidos pelas views. Os templates contêm marcações especiais que são substituídas pelos dados reais durante o processo de renderização.

### Uso do Padrão Repository para Acesso a Dados

Embora a arquitetura MVT seja predominante no Django, é comum utilizar o padrão Repository para encapsular a lógica de acesso a dados, especialmente em aplicações maiores ou mais complexas. O Repository atua como uma camada intermediária entre o Model e o banco de dados, facilitando a separação de preocupações e tornando o código mais modular e testável. Ele fornece métodos para recuperar, criar, atualizar e excluir objetos do banco de dados, abstraindo os detalhes de implementação específicos do modelo.


## 4. Requisitos Funcionais

### Lista Detalhada de Funcionalidades do Sistema

- Cadastro de novas histórias com título, texto, data de publicação, imagem ilustrativa e categoria.
- Visualização de lista de histórias em formato de cards.
- Filtragem de histórias por categoria.
- Busca de histórias por título ou categoria.
- Visualização detalhada de cada história.

### Casos de Uso Principais

- Um usuário deseja registrar uma nova história.
- Um usuário deseja visualizar a lista de histórias disponíveis.
- Um usuário deseja filtrar as histórias por categoria.
- Um usuário deseja buscar uma história específica por título ou categoria.
- Um usuário deseja visualizar detalhes completos de uma história selecionada.

### Fluxos de Trabalho do Usuário

1. Cadastro de Histórias:
   - Preenchimento do formulário de cadastro de nova história.
   - Envio dos dados do formulário para o sistema.
   - Confirmação do cadastro da história.

2. Visualização de Lista de Histórias:
   - Navegação para a página principal do sistema.
   - Visualização da lista de histórias em formato de cards.
   - Possibilidade de clicar em uma história para ver detalhes.

3. Filtragem de Histórias por Categoria:
   - Seleção da categoria desejada no filtro de categorias.
   - Atualização da lista de histórias para exibir apenas as histórias da categoria selecionada.

4. Busca de Histórias:
   - Digitação do termo de busca na barra de busca.
   - Submissão do termo de busca para o sistema.
   - Exibição dos resultados da busca na lista de histórias.

## 5. Requisitos Não Funcionais

### Desempenho Esperado do Sistema

Espera-se que o sistema apresente um desempenho rápido e responsivo, garantindo uma experiência de usuário satisfatória mesmo em condições de alta carga de acessos.

### Segurança e Autenticação

O sistema deve garantir a segurança dos dados dos usuários, incluindo mecanismos robustos de autenticação e autorização. As informações sensíveis devem ser protegidas contra acesso não autorizado.

### Escalabilidade e Manutenibilidade

O sistema deve ser facilmente escalável para acomodar um aumento no número de usuários e de histórias cadastradas. Além disso, deve ser de fácil manutenção, com código limpo e organizado para facilitar futuras atualizações e correções de bugs.

## 6. Tecnologias Utilizadas

### Linguagens de Programação

- Python
- HTML
- CSS

### Frameworks

- Django
- Django REST Framework

### Bancos de Dados

- SQLite (ambiente de desenvolvimento)
- PostgreSQL (ambiente de produção)

### Ferramentas de Desenvolvimento

- Git
- Visual Studio Code

## 7. Modelo de Dados

### Estrutura do Banco de Dados

O banco de dados do sistema possui as seguintes tabelas:

- História: Representa uma história cadastrada no sistema.
  - id: Identificador único da história.
  - título: Título da história.
  - texto: Conteúdo da história.
  - data_publicação: Data de publicação da história.
  - imagem_ilustrativa: Imagem ilustrativa da história.
  - categoria: Categoria da história.

- Categoria: Representa as categorias disponíveis para as histórias.
  - id: Identificador único da categoria.
  - nome: Nome da categoria.

### Relacionamentos entre Entidades

- Cada história pode pertencer a uma única categoria.
- Cada categoria pode ter várias histórias associadas.

### Esquema de Armazenamento

O esquema de armazenamento segue o modelo relacional, com as tabelas História e Categoria relacionadas através de chaves estrangeiras.

## 8. Interfaces do Usuário

### Layout e Design das Interfaces

As interfaces do usuário seguem um design intuitivo e responsivo, garantindo uma experiência agradável em dispositivos de diferentes tamanhos.

### Funcionalidades Específicas de Cada Tela

- Página Principal: Apresenta uma lista de histórias em formato de cards, permitindo filtrar por categoria e buscar histórias por título.
- Página de Detalhes: Exibe informações detalhadas de uma história selecionada, incluindo título, texto, data de publicação, imagem ilustrativa e categoria.

### Fluxos de Interação do Usuário

1. Visualização da Lista de Histórias:
   - O usuário pode navegar pela lista de histórias, visualizando os cards de cada história.
   - Ele pode clicar em uma história para ver mais detalhes.

2. Busca e Filtragem:
   - O usuário pode buscar histórias por título utilizando a barra de busca.
   - Ele também pode filtrar as histórias por categoria utilizando o menu de categorias.

## 9. Arquitetura de Implementação

### Organização do Código-Fonte

O código-fonte do sistema está organizado em diferentes diretórios de acordo com sua funcionalidade:

- `models/`: Contém os modelos de dados do sistema.
- `views/`: Contém as views responsáveis por processar as requisições do usuário.
- `templates/`: Contém os templates HTML utilizados para renderizar as páginas.
- `static/`: Contém arquivos estáticos como CSS, JavaScript e imagens.

### Divisão em Módulos e Componentes

O código-fonte está dividido em mód
