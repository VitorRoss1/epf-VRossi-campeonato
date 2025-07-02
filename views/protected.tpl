% rebase('layout', title='Área Protegida')

<div class="card mt-4">
    <div class="card-header bg-success text-white">
        <h2>Acesso Permitido</h2>
    </div>
    <div class="card-body">
        <p class="lead">{{data['message']}}</p>
        <p>Esta é uma área que só pode ser acessada por usuários logados.</p>
        <a href="/auth/logout" class="btn btn-danger mt-3">
            <i class="fas fa-sign-out-alt me-2"></i>Sair
        </a>
    </div>
</div>