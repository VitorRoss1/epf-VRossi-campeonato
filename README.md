# Projeto Template: POO com Python + Bottle + JSON CAMPEONATO BRASILEIRO 25

Este é um projeto de vitor da costa rossi de oliveira baseado no template educacional voltado para o ensino de **Programação Orientada a Objetos (POO)** do Prof. Lucas Boaventura, Universidade de Brasília (UnB).

Utiliza o microframework **Bottle**. Ideal para uso em disciplinas introdutórias de Engenharia de Software ou Ciência da Computação.

## 💡 Objetivo

Simular o Campeonato Brasileiro de 2025, permitindo que você insira os placares das partidas, veja as estatísticas dos times acumularem , acompanhe a tabela de classificação e acesse os dois craques de cada um dos 20 times (usuários cadastrados).

---

## 🗂 Estrutura de Pastas

```bash
campeonato/
├── app.py
├── config.py
├── main.py
├── requirements.txt
├── README.md
├── controllers/
│   ├── __init__.py
│   ├── campeonato_controller.py
│   ├── simular_controller.py
│   └── user_controller.py
├── models/
│   ├── __init__.py
│   ├── jogador.py
│   ├── partida.py
│   ├── time.py
│   └── user.py
├── services/
│   ├── __init__.py
│   ├── campeonato_service.py
│   └── user_service.py
├── views/
│   ├── auth/
│   │   ├── login.tpl
│   │   └── register.tpl
│   ├── campeonato/
│   │   ├── rodada.tpl
│   │   ├── tabela.tpl
│   │   └── time.tpl
│   ├── layout.tpl
│   └── protected.tpl
├── static/
│   ├── css/
│   │   └── style.css
│   ├── img/
│   │   ├── bah.png
│   │   ├── bot.png
│   │   └── ... (outros escudos)
│   └── js/
│       └── main.js
├── data/
│   ├── partidas.json
│   ├── times.json
│   └── users.json
└── .vscode/
    └── settings.json
```

OO-EPF-CAMPEONATO

‘->’ : no meu projeto..
 
1. Aplicação Web em Python com Bottle
    * Estrutura MVC (Model-View-Controller)
    * Persistência de dados (JSON, SQLite ou outro banco simples)
    * ->JSON
2. Modelagem de Dados
    * Pelo menos duas classes principais (models) além de uma classe Usuário
    * Implementação dos 4 pilares de OO: Abstração, Encapsulamento, Herança e Polimorfismo

-> Abstração (ocultar detalhes de implementação complexos e exibir apenas as funcionalidades essenciais de um sistema)

Classes model/time e model/partida e model/jogador focam apenas o que é relevante para o propósito de um campeonato virtual e nao nas complexidades reais desses conceitos. 


->Encapsulamento
`_stats` em model/time


->Herança
` jogadorGoleiro/linha de jogador` em model/jogador


->Polimorfismo
A classe `JogadorGoleiro` sobrescreve `JogadorLinha `(subclasses de jogador em model/jogador) 


1. Autenticação de Usuários
    * A aplicação deverá gerenciar o cadastro de usuários com acesso à funções exclusivas, além das funcionalidades públicas da aplicação.
    * Sistema de cadastro/login
2. Interface Web
    * Layout customizado além do básico (usando CSS/Bootstrap/Materialize)
    * -> Bootstrap 5.3.3 e CSS customizado (style.css)
3. Documentação
    * README.md contendo:
        * Descrição da solução e funcionalidades
        * Diagrama de classes (Sugestão: draw.io)
        * ->
        * ￼<img width="532" alt="Captura de Tela 2025-07-06 às 20 01 51" src="https://github.com/user-attachments/assets/b6fda394-8b4d-4d93-bb0e-a22853e8d2e0" />

        * Instruções de instalação/execução
    * 
Requisitos para Pontuação Extra

1. Relações entre Models
    * Associações entre models (1-1, 1-N, N-N)
    * Implementação de composição/agregação nas models
    * -> 1-n (time->jogadores, partida->times)
2. Sistema de Permissões
    * Gerência de níveis de permissão por tipo de usuário (usuário, regular, usuário admin, etc) 
    * -> X
3. Bibliotecas Adicionais
    * Uso de libs adicionais além do bottle
    * -> Json ,bootstrap 5.3.3
4. Qualidade do Projeto
    * Relevância do tema
    * Criatividade na solução
    * Código bem organizado e documentado
    * Tratamento de erros

---

## 📁 Descrição das Pastas

controllers/

Essa pasta tem as classes que cuidam das rotas do seu site. Elas recebem o que o usuário faz, conversam com a lógica do programa e decidem qual página mostrar.

campeonato_controller.py: Gerencia as páginas da tabela, das rodadas e dos detalhes dos times.

simular_controller.py: É onde você registra os placares das rodadas. Ele salva tudo no campeonato de verdade, mostrando o placar acumulado.

user_controller.py: Cuida das rotas de login, cadastro e, se você mantiver, do gerenciamento de usuários.

models/

Aqui ficam as classes que representam os dados do seu aplicativo e a lógica por trás deles. Elas são a "essência" do que seu programa entende.

time.py: Define o Time, com nome, escudo e estatísticas acumuladas.

partida.py: Representa uma Partida de futebol, com os times e os placares.

jogador.py: Define os Jogadores, incluindo suas posições (atacante, goleiro, etc.).

user.py: Define o Usuário que acessa o sistema.

item_campeonato_base.py: Contém a classe abstrata para itens do campeonato, garantindo que tenham um ID.

services/

Essa pasta tem a lógica pra salvar, carregar e trabalhar com seus dados, que ficam em arquivos JSON. É o lugar onde as regras do jogo e do sistema são aplicadas.

campeonato_service.py: É o coração do campeonato. Ele carrega e salva os times e partidas, e calcula todas as estatísticas acumuladas.

user_service.py: Cuida do login, cadastro e autenticação dos usuários.

views/

Nessa pasta, você encontra todos os arquivos .tpl. São os templates HTML que o Bottle usa pra montar as páginas que o usuário vê.

layout.tpl: É a base de todas as páginas, com o menu de navegação e o cabeçalho.

campeonato/: Tem as páginas específicas do campeonato, como a tabela (tabela.tpl) e os detalhes das rodadas (rodada.tpl) e dos times (time.tpl).

simular/: Tem a página pra registrar os placares (simular_rodada.tpl).

auth/: Tem as páginas de login (login.tpl) e cadastro (register.tpl).

static/

Essa é a pasta pra arquivos que o navegador consegue usar diretamente, como estilos CSS, códigos JavaScript e imagens.

css/: Guarda seus arquivos CSS, como style.css.

img/: Tem as imagens dos escudos dos times (ex: fla.png, pal.png).

js/: Onde você pode adicionar scripts JS.

data/

Aqui ficam os arquivos .json que funcionam como o banco de dados do seu projeto. É onde todas as informações do campeonato são guardadas de forma persistente.

times.json: Guarda os dados dos times e suas estatísticas.

partidas.json: Guarda todos os jogos e seus placares.

users.json: Guarda os dados dos usuários cadastrados.

---

## ▶️ Como Executar

1. Crie o ambiente virtual na pasta fora do seu projeto:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate     # Windows
```

2. Entre dentro do seu projeto criado a partir do template e instale as dependências:
```bash
pip install -r requirements.txt
```

3. Rode a aplicação:
```bash
python3 main.py
```

4. Accese sua aplicação no navegador em: [http://localhost:8080](http://localhost:8080)


---

## 🧠 Autor e Licença
vítor da costa rossi de oliveira - 242015352

Projeto desenvolvido como template didático para disciplinas de Programação Orientada a Objetos, baseado no [BMVC](https://github.com/hgmachine/bmvc_start_from_this).
