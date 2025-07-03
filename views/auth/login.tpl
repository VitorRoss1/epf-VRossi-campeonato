% rebase('layout', title='Login')

<div class="row justify-content-center">
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">Login</div>
            <div class="card-body">
                % if error: 
                <div class="alert alert-danger">{{error}}</div> 
                % end
                
                <form action="/auth/login" method="post">
                    <div class="mb-3">
                        <label class="form-label">Email:</label>
                        <input type="email" name="email" class="form-control" required>
                    </div>
                    
                    <div class="mb-3">
                        <label class="form-label">Senha:</label>
                        <input type="password" name="password" class="form-control" required>
                    </div>
                    
                    <button type="submit" class="btn btn-primary">Entrar</button>
                </form>
                
                <div class="mt-3">
                    <p>Não tem conta? <a href="/auth/register">Registre-se aqui</a></p>
                </div>
            </div>
        </div>
    </div>
</div>