% rebase('layout', title='Login - Brasileirão 2025')

<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header bg-primary text-white">
                    <h3 class="text-center"><i class="fas fa-sign-in-alt"></i> Acesso ao Simulador</h3>
                </div>
                <div class="card-body">
                    % if error:
                    <div class="alert alert-danger">{{error}}</div>
                    % end
                    
                    <form action="/login" method="post">
                        <div class="mb-3">
                            <label for="email" class="form-label">Email:</label>
                            <input type="email" class="form-control" id="email" name="email" required>
                        </div>
                        
                        <div class="mb-3">
                            <label for="password" class="form-label">Senha:</label>
                            <input type="password" class="form-control" id="password" name="password" required>
                        </div>
                        
                        <div class="d-grid gap-2">
                            <button type="submit" class="btn btn-primary">
                                <i class="fas fa-sign-in-alt"></i> Entrar
                            </button>
                        </div>
                    </form>
                    
                    <div class="mt-3 text-center">
                        <p>Não tem uma conta? <a href="/register">Cadastre-se</a></p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>