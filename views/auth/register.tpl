% rebase('layout', title='Registro')

<div class="row justify-content-center">
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">Criar Nova Conta</div>
            <div class="card-body">
                % if 'error' in data:
                <div class="alert alert-danger">{{data['error']}}</div>
                % end
                
                <form action="/auth/register" method="post">
                    <div class="mb-3">
                        <label class="form-label">Nome:</label>
                        <input type="text" name="name" class="form-control" required>
                    </div>
                    
                    <div class="mb-3">
                        <label class="form-label">Email:</label>
                        <input type="email" name="email" class="form-control" required>
                    </div>
                    
                    <div class="mb-3">
                        <label class="form-label">Senha:</label>
                        <input type="password" name="password" class="form-control" required>
                    </div>
                    
                    <button type="submit" class="btn btn-primary">Registrar</button>
                </form>
            </div>
        </div>
    </div>
</div>