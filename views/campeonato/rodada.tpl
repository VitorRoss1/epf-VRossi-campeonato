% rebase('layout', title=f'Rodada {rodada}')
% from 'helper-final.tpl' import match_card

<div class="card">
    <div class="card-header bg-primary text-white">
        <div class="d-flex justify-content-between align-items-center">
            <h2><i class="fas fa-calendar-alt"></i> Rodada {{rodada}}</h2>
            <a href="/campeonato" class="btn btn-light">
                <i class="fas fa-arrow-left"></i> Voltar para Tabela
            </a>
        </div>
    </div>
    
    <div class="card-body">
        <form action="/campeonato/enviar-placares" method="post">
            <input type="hidden" name="rodada" value="{{rodada}}">
            
            % for partida in partidas:
            <div class="mb-4">
                {{match_card(partida, editable=True)}}
            </div>
            % end
            
            <div class="d-grid gap-2">
                <button type="submit" class="btn btn-success btn-lg">
                    <i class="fas fa-calculator"></i> Calcular Tabela
                </button>
            </div>
        </form>
    </div>
</div>