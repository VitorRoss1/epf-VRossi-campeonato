<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="/">Brasileirão 2025</a>
            
            <div class="collapse navbar-collapse">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="/campeonato">Campeonato</a>
                    </li>
                </ul>
                
                <ul class="navbar-nav">
                    % if user_service.get_current_user():
                        <li class="nav-item">
                            <a class="nav-link" href="/users/protected">Protegido</a>
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

    <div class="container mt-4">
        {{!base}}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>