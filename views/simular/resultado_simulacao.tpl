% rebase('layout', title=f'Resultado da Simulação - Rodada {rodada_simulada}')

% def tabela_row(time, posicao, current_user=None):
<tr class=""> 
    <td>{{posicao}}</td> 
    <td>
        <a href="/campeonato/time/{{time.id}}" class="text-decoration-none">
            <img src="/static/img/{{time.img_path}}" alt="{{time.nome}}" width="30" height="30" class="me-2">
            {{time.nome}}
        </a>
    </td>
    <td class="fw-bold">{{time._stats["Pontos"]}}</td>
    <td>{{time._stats["vitorias"]}}</td>
    <td>{{time._stats["empates"]}}</td>
    <td>{{time._stats["derrotas"]}}</td>
    <td>{{time._stats["gols_pro"]}}</td>
    <td>{{time._stats["gols_contra"]}}</td>
    <td class="{{'text-success' if time.Saldo_Gols() > 0 else 'text-danger' if time.Saldo_Gols() < 0 else ''}}">
        {{time.Saldo_Gols()}}
    </td>
</tr>
% end

% def match_card(partida, editable=False):
<div class="match-card mb-3 p-3 border rounded">
    <div class="row align-items-center">
        <div class="col-md-5 text-end">
            <img src="/static/img/{{partida.casa.img_path}}" alt="{{partida.casa.nome}}" width="40" height="40">
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
            <img src="/static/img/{{partida.fora.img_path}}" alt="{{partida.fora.nome}}" width="40" height="40">
            <strong>{{partida.fora.sigla}}</strong>
        </div>
    </div>
</div>
% end


<div class="card mb-4">
    <div class="card-header bg-primary text-white">
        <h2></i>Resultados da Simulação - Rodada {{rodada_simulada}}</h2>
    </div>
    <div class="card-body">
        <h3 class="mb-3">Partidas Simuladas:</h3>
        % for partida in simulated_partidas:
        <div class="mb-3">
            {{ match_card(partida, editable=False) }}
        </div>
        % end

        <h3 class="mb-3 mt-4">Tabela de Classificação Simulada:</h3>
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
                    % for idx, time in enumerate(simulated_tabela, 1):
                        {{ tabela_row(time, idx) }}
                    % end
                </tbody>
            </table>
        </div>
        <div class="d-grid mt-4">
            <a href="/simular/{{rodada_simulada + 1 if rodada_simulada < campeonato_service.get_current_rodada() else rodada_simulada}}" class="btn btn-primary btn-lg">
                </i> Próxima Rodada
            </a>
            <a href="/simular" class="btn btn-secondary btn-lg mt-2">
                </i> Nova Simulação
            </a>
        </div>
    </div>
</div>