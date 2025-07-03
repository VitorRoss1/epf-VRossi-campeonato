% rebase('layout', title='Tabela de Classificação')


% def tabela_row(time, posicao, current_user=None):
<tr class="{{'table-primary' if current_user and current_user['time_favorito'] == time.id else ''}}">
    <td>{{posicao}}</td>
    <td>
        <a href="/campeonato/time/{{time.id}}" class="text-decoration-none">
            <img src="/static/img/{{time.img_path}}" alt="{{time.nome}}" width="30" height="30" class="me-2">
            {{time.nome}}
        </a>
    </td>
    <td class="fw-bold">{{time.stats["Pontos"]}}</td>
    <td>{{time.stats["vitorias"]}}</td>
    <td>{{time.stats["empates"]}}</td>
    <td>{{time.stats["derrotas"]}}</td>
    <td>{{time.stats["gols_pro"]}}</td>
    <td>{{time.stats["gols_contra"]}}</td>
    <td class="{{'text-success' if time.Saldo_Gols() > 0 else 'text-danger' if time.Saldo_Gols() < 0 else ''}}">
        {{time.Saldo_Gols()}}
    </td>
</tr>
% end


% def login_required_alert(message="Faça login para acessar este recurso"):
<div class="alert alert-warning mt-3">
    <i class="fas fa-exclamation-circle me-2"></i>
    {{message}}
    <a href="/auth/login" class="alert-link ms-2">Clique aqui para fazer login</a>
</div>
% end

<div class="card">
    <div class="card-header bg-primary text-white">
        <h2><i class="fas fa-trophy me-2"></i>Classificação</h2>
    </div>
    
    <div class="card-body">
        <div class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th>#</th>
                        <th>Time</th>
                        <th>P</th>
                        <th>V</th>
                        <th>E</th>
                        <th>D</th>
                        <th>GP</th>
                        <th>GC</th>
                        <th>SG</th>
                    </tr>
                </thead>
                <tbody>
                    % current_user = user_service.get_current_user()
                    % for idx, time in enumerate(times, 1):
                        {{ tabela_row(time, idx, current_user) }} 
                    % end
                </tbody>
            </table>
        </div>
    </div>
</div>