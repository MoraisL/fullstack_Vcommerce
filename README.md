# V-Commerce



author - Vinícius de Morais Lino


# Escopo do Projeto

## 1. Introdução

### Visão Geral do Projeto

O projeto consiste no desenvolvimento de um sistema web fullstack para um E-commerce. A aplicação permite que os usuários adicionem produtos ao carrinho, removam produtos do carrinho, pesquisem produtos e filtrem produtos por categorias e outros critérios. Além disso, oferece funcionalidades de autenticação e autorização para garantir a segurança dos dados dos usuários.

### Objetivos e Propósito do Sistema

O objetivo principal do sistema é proporcionar uma plataforma intuitiva e eficiente para que os usuários possam realizar compras online de forma organizada. O sistema visa facilitar a navegação, a busca de produtos, proporcionando uma experiência de usuário agradável e segura.

### Benefícios Esperados do Projeto

- Facilidade de adicionar e remover produtos do carrinho de compras.
- Promoção de uma experiência de compra segura e eficiente.
- Organização e categorização eficientes dos produtos para uma melhor experiência do usuário.
- Possibilidade de busca e filtragem rápida de produtos por diversos critérios.

## 2. Visão Geral do Sistema

### Descrição do Sistema

O sistema é uma aplicação web desenvolvida utilizando o framework Django, que segue a arquitetura MVC (Model-View-Controller) adaptada para MTV (Model-Template-View). Ele permite que os usuários adicionem produtos ao carrinho, removam produtos do carrinho, visualizem uma lista de produtos, filtrem os produtos por categoria e acessem detalhes completos dos produtos selecionados.

### Público-Alvo do Sistema

O público-alvo do sistema são consumidores que desejam realizar compras online. O sistema é voltado para uma ampla gama de usuários, desde compradores ocasionais até consumidores frequentes de lojas virtuais.


## 3. Arquitetura do Sistema

### Explicação da Arquitetura MVT (Model-View-Template)

O sistema segue uma arquitetura MVT (Model-View-Template), onde:

- **Model:** Representa a camada de dados e lógica de negócios. Aqui são definidos os modelos de dados que representam as entidades do sistema, como Produto e Categoria.
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

- Cadastro de novos produtos com nome, descrição, preço, imagem e categoria.
- Visualização de lista de produtos.
- Filtragem de produtos por categoria.
- Busca de produtos por nome ou categoria.
- Visualização detalhada de cada produto.
- Adicionar produtos ao carrinho de compras.
- Remover produtos do carrinho de compras.


### Casos de Uso Principais

- Um usuário deseja adicionar um produto ao carrinho.
- Um usuário deseja remover um produto do carrinho.
- Um usuário deseja visualizar a lista de produtos disponíveis.
- Um usuário deseja filtrar os produtos por categoria.
- Um usuário deseja buscar um produto específico por nome ou categoria.
- Um usuário deseja visualizar detalhes completos de um produto selecionado.

### Fluxos de Trabalho do Usuário

1. **Adicionar Produto ao Carrinho:**
    - Seleção do produto desejado.
    - Adição do produto ao carrinho de compras.
    - Confirmação da adição do produto ao carrinho.
2. **Remover Produto do Carrinho:**
    - Visualização do carrinho de compras.
    - Seleção do produto a ser removido.
    - Remoção do produto do carrinho.
3. **Visualização de Lista de Produtos:**
    - Navegação para a página principal do sistema.
    - Visualização da lista de produtos em formato de cards.
    - Possibilidade de clicar em um produto para ver detalhes.
4. **Filtragem de Produtos por Categoria:**
    - Seleção da categoria desejada no filtro de categorias.
    - Atualização da lista de produtos para exibir apenas os produtos da categoria selecionada.
5. **Busca de Produtos:**
    - Digitação do termo de busca na barra de busca.
    - Submissão do termo de busca para o sistema.
    - Exibição dos resultados da busca na lista de produtos.
6. **Finalização de Compra:**
    - Navegação para a página de finalização de compra.
    - Preenchimento das informações de pagamento e envio.
    - Confirmação da compra e processamento do pagamento.

## 5. Requisitos Não Funcionais

### Desempenho Esperado do Sistema

Espera-se que o sistema apresente um desempenho rápido e responsivo, garantindo uma experiência de usuário satisfatória mesmo em condições de alta carga de acessos.

### Segurança e Autenticação

O sistema deve garantir a segurança dos dados dos usuários, incluindo mecanismos robustos de autenticação e autorização. As informações sensíveis devem ser protegidas contra acesso não autorizado.

### Escalabilidade e Manutenibilidade

O sistema deve ser facilmente escalável para acomodar um aumento no número de usuários e de produtos cadastrados. Além disso, deve ser de fácil manutenção, com código limpo e organizado para facilitar futuras atualizações e correções de bugs.

## 6. Tecnologias Utilizadas

### Linguagens de Programação

- Python
- HTML
- CSS
- JavaScript

### Frameworks e Bibliotecas

- Django
- Django Rest Framework
- Bootstrap
- jQuery

### Ferramentas de Desenvolvimento

- Visual Studio Code
- Git

## 7. Implementação e Configuração do Sistema

### Instruções para Configuração do Sistema Localmente

Para configurar a aplicação localmente, siga os seguintes passos:

1. Clone o repositório para sua máquina local:

git clone https://github.com/MoraisL/fullstack_Vcommerce

2. Navegue até o diretório do projeto:

cd ecommerce-hoodie-app

3. Crie um ambiente virtual e ative-o:

python -m venv env
source env/bin/activate

4. Instale as dependências a partir do arquivo requirements.txt:

pip install -r requirements.txt

5. Aplique as migrações para criar o esquema do banco de dados:

python manage.py migrate

6. Execute o servidor de desenvolvimento:

python manage.py runserver


Acesse a aplicação no navegador em {http://127.0.0.1:8080/}.


### Navegação e Funcionalidades do Sistema

- Navegue pelos produtos na página principal.
- Utilize a barra de busca para encontrar produtos específicos.
- Veja informações detalhadas dos produtos na página de detalhes do produto.
- Adicione produtos ao carrinho e gerencie os itens selecionados.
- Prossiga para a finalização de compra para concluir suas compras.
- Registre-se e faça login para acessar funcionalidades personalizadas.
- Atualize os detalhes do usuário na página de perfil.
- Explore diferentes categorias de produtos e veja os produtos relacionados.

## 8. Endpoints e Descrições

- Homepage URL: / Método: GET Descrição: Exibe a página inicial com produtos de moletom.
- About Section URL: /about/ Método: GET Descrição: Exibe informações sobre o aplicativo.
- Login Page URL: /login/ Método: GET, POST Descrição: Permite que os usuários façam login em suas contas.
- Logout Page URL: /logout/ Método: GET Descrição: Permite que os usuários façam logout de suas contas.
- Register Page URL: /register/ Método: GET, POST Descrição: Permite que novos usuários se registrem.
- Profile Page URL: /update_user/ Método: GET, POST Descrição: Permite que os usuários visualizem e atualizem seus dados.
- User Info Page URL: /update_info/ Método: GET, POST Descrição: Permite que os usuários adicionem detalhes adicionais sobre si mesmos.
- Product Categories Page URL: /category/str/  Método: GET Descrição: Exibe produtos de moletom pertencentes a uma categoria específica.
- Product Details Page URL: /product/int/ Método: GET Descrição: Exibe informações detalhadas sobre um produto de moletom específico.
- Cart Page URL: /cart/ Método: GET Descrição: Exibe todos os produtos de moletom adicionados ao carrinho de compras.
- Search Page URL: /search/ Método: GET, POST Descrição: Permite que os usuários procurem produtos de moletom específicos.

## 9. Autenticação e Segurança

### Métodos de Autenticação Utilizados

A autenticação dos usuários é realizada utilizando o sistema de autenticação padrão do Django. Os usuários podem fazer login com seu nome de usuário e senha, e novos usuários podem se registrar para criar uma conta e acessar funcionalidades adicionais.

### Exemplos de Uso

#### Exemplo 1: Registro de Conta

1. Navegue para a página de registro (/register/}).
2. Preencha o formulário de registro com seu nome de usuário e senha desejados.
3. Clique no botão "Registrar" para enviar o formulário.
4. Após o registro bem-sucedido, você será redirecionado para a página de perfil (update_info/}) para adicionar detalhes adicionais.

#### Exemplo 2: Login na Conta

1. Navegue para a página de login (/login/}).
2. Insira seu nome de usuário e senha.
3. Clique no botão "Login" para acessar sua conta.
4. Após o login bem-sucedido, você será redirecionado para a página principal (/) para começar a navegar pelos produtos.

#### Exemplo 3: Atualização de Detalhes do Usuário

1. Navegue para a página de perfil (\texttt{/update_user/}).
2. Visualize seus detalhes atuais.
3. Atualize os detalhes conforme necessário.
4. Clique no botão "Salvar" para salvar as mudanças.

#### Exemplo 4: Adição de Informações Adicionais do Usuário

1. Navegue para a página de informações adicionais (\texttt{/update_info/}).
2. Preencha o formulário com detalhes adicionais, como endereço e informações de contato.
3. Clique no botão "Salvar" para salvar as mudanças.

