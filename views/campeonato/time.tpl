% rebase('layout', title=time.nome)


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
            </div>
            % end
        </div>
    </div>
</div>
% end


% def login_required_alert(message="Faça login para acessar este recurso"):
<div class="alert alert-warning mt-3">
    </i>
    {{message}}
    <a href="/auth/login" class="alert-link ms-2">Clique aqui para fazer login</a>
</div>
% end

        </i> Craques Do Time </h3>
        
        % if user_service.get_current_user():
            <div class="row">
                % for jogador in time.getJogadores:
                    {{ jogador_card(jogador, show_details=False) }} 
                % end
            </div>
        % else:
            {{ login_required_alert("Faça login para visualizar o elenco completo e detalhes dos jogadores.") }} 
    </div>
</div>