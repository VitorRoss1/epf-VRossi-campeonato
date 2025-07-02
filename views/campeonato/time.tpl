% rebase('layout', title=time.nome)
% from 'helper_final.tpl' import jogador_card, login_required_alert

<div class="card">
    <div class="card-header bg-primary text-white">
        <div class="d-flex justify-content-between align-items-center">
            <h2 class="mb-0">
                <img src="/static/images/{{time.img_path}}" alt="{{time.nome}}" width="50" height="50" class="me-3">
                {{time.nome}} ({{time.sigla}})
            </h2>
            <a href="/campeonato" class="btn btn-light btn-sm">
                <i class="fas fa-arrow-left me-1"></i> Voltar
            </a>
        </div>
    </div>
    
    <div class="card-body">
        <div class="row mb-4">
            <div class="col-md-6">
                <div class="card h-100">
                    <div class="card-header bg-secondary text-white">
                        <i class="fas fa-chart-line me-2"></i>Estatísticas
                    </div>
                    <div class="card-body">
                        <div class="row">
                            <div class="col-6">
                                <p><strong>Pontos:</strong> {{time.stats["Pontos"]}}</p>
                                <p><strong>Vitórias:</strong> {{time.stats["vitorias"]}}</p>
                                <p><strong>Empates:</strong> {{time.stats["empates"]}}</p>
                            </div>
                            <div class="col-6">
                                <p><strong>Derrotas:</strong> {{time.stats["derrotas"]}}</p>
                                <p><strong>Gols Pró:</strong> {{time.stats["gols_pro"]}}</p>
                                <p><strong>Gols Contra:</strong> {{time.stats["gols_contra"]}}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-6">
                <div class="card h-100">
                    <div class="card-header bg-secondary text-white">
                        <i class="fas fa-info-circle me-2"></i>Informações
                    </div>
                    <div class="card-body">
                        <p><strong>Saldo de Gols:</strong> 
                            <span class="{{'text-success' if time.Saldo_Gols() > 0 else 'text-danger' if time.Saldo_Gols() < 0 else ''}}">
                                {{time.Saldo_Gols()}}
                            </span>
                        </p>
                        <p><strong>Aproveitamento:</strong> 
                            {{'%.1f' % (time.stats["Pontos"] / (rodada * 3) * 100) if rodada > 0 else 0}}%
                        </p>
                    </div>
                </div>
            </div>
        </div>
        
        <h3 class="mb-3"><i class="fas fa-users me-2"></i>Elenco</h3>
        
        % if user_service.get_current_user():
            <div class="row">
                % for jogador in time.getJogadores:
                    {{ jogador_card(jogador, show_details=False) }}
                % end
            </div>
        % else:
            {{ login_required_alert("Faça login para visualizar o elenco completo e detalhes dos jogadores.") }}
        % end
    </div>
</div>
