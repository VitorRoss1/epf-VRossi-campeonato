% rebase('layout', title=('Editar' if user else 'Novo') + ' Usuário')

<div class="card">
    <div class="card-header">
        <h2>{{'Editar' if user else 'Novo'}} Usuário</h2>
    </div>
    <div class="card-body">
        % if 'error' in data:
        <div class="alert alert-danger">{{data['error']}}</div>
        % end
        
        <form action="{{action}}" method="post">
            <div class="mb-3">
                <label class="form-label">Nome:</label>
                <input type="text" name="name" class="form-control" 
                       value="{{user['name'] if user else ''}}" required>
            </div>
            
            <div class="mb-3">
                <label class="form-label">Email:</label>
                <input type="email" name="email" class="form-control" 
                       value="{{user['email'] if user else ''}}" required>
            </div>
            
            <div class="mb-3">
                <label class="form-label">Senha:</label>
                <input type="password" name="password" class="form-control" 
                       placeholder="{{'Deixe em branco para manter' if user else ''}}" 
                       {{'' if user else 'required'}}>
            </div>
            
            <button type="submit" class="btn btn-primary">Salvar</button>
            <a href="/users" class="btn btn-secondary">Cancelar</a>
        </form>
    </div>
</div>