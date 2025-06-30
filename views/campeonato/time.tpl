% rebase('layout', title=f'{time.nome} - Elenco')
% from 'helper-final.tpl' import jogador_card

<div class="card">
    <div class="card-header bg-primary text-white">
        <div class="d-flex justify-content-between align-items-center">
            <h2>
                <img src="/static/images/{{time.img_path}}" alt="{{time.nome}}" width="50">
                {{time.nome}} ({{time.sigla}})
            </h2>
            <a href="/campeonato" class="btn btn-light">
                <i class="fas fa-arrow-left"></i> Voltar
            </a>
        </div>
    </div>
    
    <div class="card-body">
        <div class="row mb-4">
            <div class="col-md-6">
                <div class="card">
                    <div class="card-header bg-secondary text-white">
                        <h5 class="mb-0"><i class="fas fa-chart-line"></i> Estatísticas</h5>
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
                        <h5 class="mb-0"><i class="fas fa-info-circle"></i> Informações</h5>
                    </div>
                    <div class="card-body">
                        <p><strong>Saldo de Gols:</strong> {{time.Saldo_Gols()}}</p>
                        <p><strong>Aproveitamento:</strong> 
                            {{'%.1f' % (time.stats["Pontos"] / (38 * 3) * 100 if rodada > 0 else 0}}%
                        </p>
                    </div>
                </div>
            </div>
        </div>
        
        <h3 class="mb-3"><i class="fas fa-users"></i> Elenco Titular</h3>
        <div class="row">
            % for jogador in time.getJogadores:
                {{jogador_card(jogador)}}
            % end
        </div>
    </div>
</div>
