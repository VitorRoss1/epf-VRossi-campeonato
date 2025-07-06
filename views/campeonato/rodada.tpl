% rebase('layout', title=f'Rodada {rodada}')

% def match_card(partida, editable=False):
<div class="match-card mb-3 p-3 border rounded">
    <div class="row align-items-center">
        <div class="col-md-5 text-end">
            <img src="/static/img/{{partida.casa.img_path}}" alt="{{partida.casa.nome}}" width="40" height="40"> 
            <strong>{{partida.casa.sigla}}</strong>
        </div>
        
        <div class="col-md-2 text-center">
            {# Placar exibido, sem campos editáveis #}
            <h5 class="mb-0">
                {{partida.casa_placar if partida.casa_placar is not None else '-'}} 
                x 
                {{partida.fora_placar if partida.fora_placar is not None else '-'}}
            </h5>
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
            <h2 class="mb-0">
                <i class="fas fa-calendar-alt me-2"></i>
                Rodada {{rodada}}
            </h2>
            <a href="/campeonato" class="btn btn-light btn-sm">
                <i class="fas fa-arrow-left me-1"></i> Voltar à Tabela
            </a>
        </div>
    </div>
    
    <div class="card-body">
        {# NÃO HÁ MAIS FORMULÁRIO DE SALVAR PLACARES AQUI #}
        % for partida in partidas:
        <div class="mb-4">
            {{ match_card(partida, editable=False) }} {# Sempre false, pois não edita aqui #}
        </div>
        % end
    </div>
</div>