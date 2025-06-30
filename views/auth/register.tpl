% rebase('layout', title='Registro - Brasileirão 2025')

<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header bg-primary text-white">
                    <h3 class="text-center"><i class="fas fa-user-plus"></i> Criar Nova Conta</h3>
                </div>
                <div class="card-body">
                    % if error:
                    <div class="alert alert-danger">{{error}}</div>
                    % end
                    
                    <form action="/register" method="post">
                        <div class="mb-3">
                            <label for="name" class="form-label">Nome Completo:</label>
                            <input type="text" class="form-control" id="name" name="name" required>
                        </div>
                        
                        <div class="mb-3">
                            <label for="email" class="form-label">Email:</label>
                            <input type="email" class="form-control" id="email" name="email" required>
                        </div>
                        
                        <div class="mb-3">
                            <label for="password" class="form-label">Senha:</label>
                            <input type="password" class="form-control" id="password" name="password" required>
                        </div>
                        
                        <div class="mb-3">
                            <label for="confirm_password" class="form-label">Confirmar Senha:</label>
                            <input type="password" class="form-control" id="confirm_password" name="confirm_password" required>
                        </div>
                        
                        <div class="d-grid gap-2">
                            <button type="submit" class="btn btn-primary">
                                <i class="fas fa-user-plus"></i> Cadastrar
                            </button>
                        </div>
                    </form>
                    
                    <div class="mt-3 text-center">
                        <p>Já tem uma conta? <a href="/login">Faça login</a></p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>