<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}}</title>
    
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- CSS Customizado -->
    <link rel="stylesheet" href="/static/css/style.css">
    
    <!-- Favicon -->
    <link rel="icon" href="/static/images/favicon.ico" type="image/x-icon">
</head>
<body>
    <!-- Barra de Navegação -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="/">
                <i class="fas fa-futbol me-2"></i>
                Brasileirão 2025
            </a>
            
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <a class="nav-link {{'active' if request.path == '/campeonato' else ''}}" 
                           href="/campeonato">
                            <i class="fas fa-trophy"></i> Classificação
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link {{'active' if 'rodada' in request.path else ''}}" 
                           href="/campeonato/rodada/1">
                            <i class="fas fa-calendar-alt"></i> Rodadas
                        </a>
                    </li>
                </ul>
                
                <ul class="navbar-nav">
                    % if is_authenticated:
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" 
                           data-bs-toggle="dropdown">
                            <i class="fas fa-user-circle"></i> Minha Conta
                        </a>
                        <ul class="dropdown-menu dropdown-menu-end">
                            <li><a class="dropdown-item" href="/users/edit/{{current_user.id}}">
                                <i class="fas fa-user-edit"></i> Perfil
                            </a></li>
                            <li><hr class="dropdown-divider"></li>
                            <li><a class="dropdown-item" href="/logout">
                                <i class="fas fa-sign-out-alt"></i> Sair
                            </a></li>
                        </ul>
                    </li>
                    % else:
                    <li class="nav-item">
                        <a class="nav-link" href="/login">
                            <i class="fas fa-sign-in-alt"></i> Entrar
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/register">
                            <i class="fas fa-user-plus"></i> Cadastrar
                        </a>
                    </li>
                    % end
                </ul>
            </div>
        </div>
    </nav>

    <!-- Conteúdo Principal -->
    <main class="container my-4">
        {{!base}}
    </main>

    <!-- Rodapé -->
    <footer class="bg-dark text-white py-3 mt-4">
        <div class="container text-center">
            <p class="mb-0">Simulador do Brasileirão 2025 - Projeto Final de Orientação a Objetos</p>
        </div>
    </footer>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    
    <!-- JS Customizado -->
    <script src="/static/js/script.js"></script>
</body>
</html>