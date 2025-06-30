% rebase('layout', title='Gerenciamento de Usuários')

<div class="card mt-4">
    <div class="card-header bg-primary text-white d-flex justify-content-between align-items-center">
        <h3><i class="fas fa-users"></i> Usuários do Sistema</h3>
        <a href="/users/add" class="btn btn-light">
            <i class="fas fa-plus"></i> Novo Usuário
        </a>
    </div>
    <div class="card-body">
        <table class="table table-striped table-hover">
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
                    <td>{{user.id}}</td>
                    <td>{{user.name}}</td>
                    <td>{{user.email}}</td>
                    <td>
                        <div class="btn-group">
                            <a href="/users/edit/{{user.id}}" class="btn btn-sm btn-warning">
                                <i class="fas fa-edit"></i>
                            </a>
                            <form action="/users/delete/{{user.id}}" method="post" 
                                  onsubmit="return confirm('Tem certeza?')" style="display:inline">
                                <button type="submit" class="btn btn-sm btn-danger">
                                    <i class="fas fa-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                % end
            </tbody>
        </table>
    </div>
</div>