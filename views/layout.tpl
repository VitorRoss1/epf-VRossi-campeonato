<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Brasileirão 2025 - {{title}}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">    
        <div class="container-fluid">
            <a class="navbar-brand" href="/campeonato">
                </i> Brasileirão 2025 
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link" href="/campeonato">Tabela</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/simular">Simular Rodada</a> 
                    </li>
                </ul>
                <ul class="navbar-nav ms-auto">
                    % current_user = user_service.get_current_user()
                    % if current_user:
                    <li class="nav-item">
                       
                    
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/auth/logout">Sair</a>
                    </li>
                    % else:
                    <li class="nav-item">
                        <a class="nav-link" href="/auth/login">Entrar</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/auth/register">Registrar</a>
                    </li>
                    % end
                </ul>
            </div>
        </div>
    </nav>

    <div class="container">
        {{!base}} 
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>