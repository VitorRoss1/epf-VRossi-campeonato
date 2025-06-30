% rebase('layout', title=f'{"Editar" if user else "Criar"} Usuário')

<div class="card mt-4">
    <div class="card-header bg-primary text-white">
        <h3><i class="fas fa-user-edit"></i> {{"Editar" if user else "Criar"}} Usuário</h3>
    </div>
    <div class="card-body">
        <form action="{{action}}" method="post">
            <div class="mb-3">
                <label class="form-label">Nome:</label>
                <input type="text" name="name" class="form-control" 
                       value="{{user.name if user else ''}}" required>
            </div>
            
            <div class="mb-3">
                <label class="form-label">Email:</label>
                <input type="email" name="email" class="form-control"
                       value="{{user.email if user else ''}}" required>
            </div>
            
            % if not user:
            <div class="mb-3">
                <label class="form-label">Senha:</label>
                <input type="password" name="password" class="form-control" required>
            </div>
            % end
            
            <div class="d-flex justify-content-between">
                <a href="/users" class="btn btn-secondary">
                    <i class="fas fa-arrow-left"></i> Voltar
                </a>
                <button type="submit" class="btn btn-primary">
                    <i class="fas fa-save"></i> Salvar
                </button>
            </div>
        </form>
    </div>
</div>