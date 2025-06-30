% rebase('layout', title='Usuários')

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