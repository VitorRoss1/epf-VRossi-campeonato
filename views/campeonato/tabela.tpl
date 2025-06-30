% rebase('layout', title='Tabela de Classificação')
% from 'helper-final.tpl' import tabela_row

<div class="card">
    <div class="card-header bg-primary text-white">
        <div class="d-flex justify-content-between align-items-center">
            <h2><i class="fas fa-trophy"></i> Classificação do Brasileirão 2025</h2>
            <div class="btn-group">
                % for r in range(1, 39):
                <a href="/campeonato/rodada/{{r}}" class="btn btn-sm btn-outline-light {{'active' if r == rodada else ''}}">
                    {{r}}
                </a>
                % end
            </div>
        </div>
    </div>
    
    <div class="card-body">
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
                    % for idx, time in enumerate(sorted(times, key=lambda t: (-t.stats['Pontos'], -t.Saldo_Gols(), -t.stats['vitorias'], t.stats['gols_contra'])), 1):
                        {{tabela_row(time, idx)}}
                    % end
                </tbody>
            </table>
        </div>
        
        <div class="mt-3">
            <div class="row">
                <div class="col-md-4">
                    <div class="card text-white bg-success">
                        <div class="card-body text-center">
                            <h5 class="card-title">Libertadores</h5>
                            <p class="card-text">1º a 6º colocados</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card text-white bg-info">
                        <div class="card-body text-center">
                            <h5 class="card-title">Pré-Libertadores</h5>
                            <p class="card-text">7º e 8º colocados</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card text-white bg-danger">
                        <div class="card-body text-center">
                            <h5 class="card-title">Rebaixamento</h5>
                            <p class="card-text">17º a 20º colocados</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>