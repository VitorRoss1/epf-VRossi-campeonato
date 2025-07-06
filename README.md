# Projeto Template: POO com Python + Bottle + JSON CAMPEONATO BRASILEIRO 25

Este é um projeto de template educacional voltado para o ensino de **Programação Orientada a Objetos (POO)** do Prof. Lucas Boaventura, Universidade de Brasília (UnB).

Utiliza o microframework **Bottle**. Ideal para uso em disciplinas introdutórias de Engenharia de Software ou Ciência da Computação.

## 💡 Objetivo

Fornecer uma base simples, extensível e didática para construção de aplicações web orientadas a objetos com aplicações WEB em Python, ideal para trabalhos finais ou exercícios práticos.

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

### `controllers/`
Contém as classes responsáveis por lidar com as rotas da aplicação. Exemplos:
- `user_controller.py`: rotas para listagem, adição, edição e remoção de usuários.
- `base_controller.py`: classe base com utilitários comuns.

### `models/`
Define as classes que representam os dados da aplicação. Exemplo:
- `user.py`: classe `User`, com atributos como `id`, `name`, `email`, etc.

### `services/`
Responsável por salvar, carregar e manipular dados usando arquivos JSON. Exemplo:
- `user_service.py`: contém métodos como `get_all`, `add_user`, `delete_user`.

### `views/`
Contém os arquivos `.tpl` utilizados pelo Bottle como páginas HTML:
- `layout.tpl`: estrutura base com navegação e bloco `content`.
- `users.tpl`: lista os usuários.
- `user_form.tpl`: formulário para adicionar/editar usuário.

### `static/`
Arquivos estáticos como:
- `css/style.css`: estilos básicos.
- `js/main.js`: scripts JS opcionais.
- `img/BottleLogo.png`: exemplo de imagem.

### `data/`
Armazena os arquivos `.json` que simulam o banco de dados:
- `users.json`: onde os dados dos usuários são persistidos.

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

## ✍️ Personalização
Para adicionar novos modelos (ex: Atividades):

1. Crie a classe no diretório **models/**.

2. Crie o service correspondente para manipulação do JSON.

3. Crie o controller com as rotas.

4. Crie as views .tpl associadas.

---

## 🧠 Autor e Licença
vítor da costa rossi de oliveira - 242015352
Projeto desenvolvido como template didático para disciplinas de Programação Orientada a Objetos, baseado no [BMVC](https://github.com/hgmachine/bmvc_start_from_this).
Você pode reutilizar, modificar e compartilhar livremente.
