% rebase('layout', title=f'Simular Rodada {rodada_atual}')

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

<div class="card">
    <div class="card-header bg-primary text-white">
        <div class="d-flex justify-content-between align-items-center">
            <h2 class="mb-0"><i class="fas fa-calculator me-2"></i>Simular Rodada</h2>
            <select class="form-select w-auto" onchange="window.location.href='/simular/' + this.value">
                % for r in range(1, max_rodada + 1):
                <option value="{{r}}" {{'selected' if r == rodada_atual else ''}}>Rodada {{r}}</option>
                % end
            </select>
        </div>
    </div>
    <div class="card-body">
        <form action="/simular/enviar_placares_simulacao" method="post">
            <input type="hidden" name="rodada_atual" value="{{rodada_atual}}">
            
            % if not partidas:
            <div class="alert alert-info">Não há partidas cadastradas para esta rodada.</div>
            % else:
                % for partida in partidas:
                <div class="mb-4">
                    {{ match_card(partida, editable=True) }}
                </div>
                % end
            % end
            
            <div class="d-grid mt-4">
                <button type="submit" class="btn btn-success btn-lg">
                    <i class="fas fa-play me-2"></i> Simular Rodada
                </button>
            </div>
        </form>
    </div>
</div>