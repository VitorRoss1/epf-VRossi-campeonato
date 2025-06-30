%# helper-final.tpl - Componentes reutilizáveis para o simulador do Brasileirão

%# Componente de card de partida
% def match_card(partida, editable=False):
<div class="match-card mb-3 p-3 border rounded">
    <div class="row align-items-center">
        <div class="col-md-5 text-end">
            <img src="/static/images/{{partida.casa.img_path}}" alt="{{partida.casa.nome}}" width="40" height="40">
            <strong>{{partida.casa.sigla}}</strong>
        </div>
        
        <div class="col-md-2 text-center">
            % if editable:
            <div class="d-flex justify-content-center align-items-center">
                <input type="number" name="casa_{{partida.id}}" class="form-control form-control-sm text-center" 
                       style="width: 60px;" min="0" 
                       value="{{partida.casa_placar if partida.casa_placar is not None else ''}}">
                <span class="mx-2">x</span>
                <input type="number" name="fora_{{partida.id}}" class="form-control form-control-sm text-center" 
                       style="width: 60px;" min="0"
                       value="{{partida.fora_placar if partida.fora_placar is not None else ''}}">
            </div>
            % else:
            <h5 class="mb-0">
                {{partida.casa_placar if partida.casa_placar is not None else '-'}} 
                x 
                {{partida.fora_placar if partida.fora_placar is not None else '-'}}
            </h5>
            % end
        </div>
        
        <div class="col-md-5">
            <img src="/static/images/{{partida.fora.img_path}}" alt="{{partida.fora.nome}}" width="40" height="40">
            <strong>{{partida.fora.sigla}}</strong>
        </div>
    </div>
</div>
% end

%# Componente de linha da tabela de classificação
% def tabela_row(time, posicao, current_user=None):
<tr class="{{'table-primary' if current_user and current_user['time_favorito'] == time.id else ''}}">
    <td>{{posicao}}</td>
    <td>
        <a href="/campeonato/time/{{time.id}}" class="text-decoration-none">
            <img src="/static/images/{{time.img_path}}" alt="{{time.nome}}" width="30" height="30" class="me-2">
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

%# Componente de card de jogador
% def jogador_card(jogador, show_details=False):
<div class="col-md-3 mb-3">
    <div class="card h-100">
        <div class="card-body">
            <div class="d-flex justify-content-between align-items-start">
                <h5 class="card-title mb-1">
                    <span class="badge bg-primary me-2">#{{jogador.numero}}</span>
                    {{jogador.nome}}
                </h5>
                <span class="badge {{'bg-success' if jogador.posicao == 'Goleiro' else 'bg-info'}}">
                    {{jogador.posicao}}
                </span>
            </div>
            % if show_details:
            <div class="mt-2">
                <small class="text-muted">Idade: {{jogador.idade if hasattr(jogador, 'idade') else 'N/A'}}</small><br>
                <small class="text-muted">Nacionalidade: {{jogador.nacionalidade if hasattr(jogador, 'nacionalidade') else 'N/A'}}</small>
            </div>
            % end
        </div>
    </div>
</div>
% end

%# Componente de alerta para login necessário
% def login_required_alert(message="Faça login para acessar este recurso"):
<div class="alert alert-warning mt-3">
    <i class="fas fa-exclamation-circle me-2"></i>
    {{message}}
    <a href="/auth/login" class="alert-link ms-2">Clique aqui para fazer login</a>
</div>
% end