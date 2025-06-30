% rebase('layout', title=f'Rodada {rodada}')
% from 'helper_final.tpl' import match_card

<div class="card">
    <div class="card-header bg-primary text-white">
        <div class="d-flex justify-content-between align-items-center">
            <h2 class="mb-0">
                <i class="fas fa-calendar-alt me-2"></i>
                Rodada {{rodada}}
            </h2>
            <a href="/campeonato" class="btn btn-light btn-sm">
                <i class="fas fa-arrow-left me-1"></i> Voltar
            </a>
        </div>
    </div>
    
    <div class="card-body">
        <form action="/campeonato/enviar-placares" method="post">
            <input type="hidden" name="rodada" value="{{rodada}}">
            
            % for partida in partidas:
            <div class="mb-4">
                {{ match_card(partida, editable=user_service.get_current_user()) }}
            </div>
            % end
            
            % if user_service.get_current_user():
            <div class="d-grid">
                <button type="submit" class="btn btn-success btn-lg">
                    <i class="fas fa-save me-2"></i> Salvar Placar
                </button>
            </div>
            % else:
            {{ login_required_alert("Faça login para editar os placares") }}
            % end
        </form>
    </div>
</div>