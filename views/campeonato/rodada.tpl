% rebase('layout', title=f'Rodada {rodada}')

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
            <img src="/static/img/{{partida.casa.img_path}}" alt="{{partida.casa.nome}}" width="40" height="40"> 
            <strong>{{partida.fora.sigla}}</strong>
        </div>
    </div>
</div> 
% end

{# Definição da função login_required_alert diretamente neste template #}
% def login_required_alert(message="Faça login para acessar este recurso"):
<div class="alert alert-warning mt-3">
    <i class="fas fa-exclamation-circle me-2"></i>
    {{message}}
    <a href="/auth/login" class="alert-link ms-2">Clique aqui para fazer login</a>
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