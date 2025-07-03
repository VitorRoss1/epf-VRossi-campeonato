% rebase('layout', title=('Editar' if user else 'Novo') + ' Usuário')

{# Definição da função login_required_alert diretamente neste template #}
% def login_required_alert(message="Faça login para acessar este recurso"):
<div class="alert alert-warning mt-3">
    <i class="fas fa-exclamation-circle me-2"></i>
    {{message}}
    <a href="/auth/login" class="alert-link ms-2">Clique aqui para fazer login</a>
</div>
% end

<div class="card">
    <div class="card-header">
        <h2>{{'Editar' if user else 'Novo'}} Usuário</h2>
    </div>
    <div class="card-body">
        % if error: {# <--- Acessa 'error' diretamente #}
        <div class="alert alert-danger">{{error}}</div> {# <--- Acessa 'error' diretamente #}
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