% rebase('layout', title='Usuários')

{# Definição da função tabela_row (se precisar aqui, adaptada para usuários) - REMOVIDO PARA EVITAR CONFUSAO, list.tpl NAO DEVE USAR TABELA_ROW DE TIMES #}
{# Definição da função login_required_alert diretamente neste template #}
% def login_required_alert(message="Faça login para acessar este recurso"):
<div class="alert alert-warning mt-3">
    <i class="fas fa-exclamation-circle me-2"></i>
    {{message}}
    <a href="/auth/login" class="alert-link ms-2">Clique aqui para fazer login</a>
</div>
% end

<div class="card">
    <div class="card-header d-flex justify-content-between align-items-center">
        <h2>Usuários</h2>
        <a href="/users/add" class="btn btn-primary">Novo Usuário</a>
    </div>
    <div class="card-body">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Email</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                % for user in users:
                <tr>
                    <td>{{user['id']}}</td>
                    <td>{{user['name']}}</td>
                    <td>{{user['email']}}</td>
                    <td>
                        <a href="/users/edit/{{user['id']}}" class="btn btn-sm btn-warning">Editar</a>
                        <form action="/users/delete/{{user['id']}}" method="post" style="display:inline">
                            <button type="submit" class="btn btn-sm btn-danger">Excluir</button>
                        </form>
                    </td>
                </tr>
                % end
            </tbody>
        </table>
    </div>
</div>