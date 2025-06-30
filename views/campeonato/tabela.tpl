% rebase('layout', title='Tabela de Classificação')
% from 'helper_final.tpl' import tabela_row

<div class="card">
    <div class="card-header bg-primary text-white">
        <h2><i class="fas fa-trophy me-2"></i>Classificação</h2>
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
                    % current_user = user_service.get_current_user()
                    % for idx, time in enumerate(times, 1):
                        {{ tabela_row(time, idx, current_user) }}
                    % end
                </tbody>
            </table>
        </div>
    </div>
</div>