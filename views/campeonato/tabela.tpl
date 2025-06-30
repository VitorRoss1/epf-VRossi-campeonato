% rebase('layout', title='Tabela de Classificação')

<div class="card">
    <div class="card-header">
        <h2>Tabela de Classificação</h2>
    </div>
    <div class="card-body">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Pos</th>
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
                % for idx, time in enumerate(times, 1):
                <tr>
                    <td>{{idx}}</td>
                    <td>
                        <a href="/campeonato/time/{{time.id}}">
                            <img src="/static/images/{{time.img_path}}" width="30">
                            {{time.sigla}}
                        </a>
                    </td>
                    <td>{{time.stats["Pontos"]}}</td>
                    <td>{{time.stats["vitorias"]}}</td>
                    <td>{{time.stats["empates"]}}</td>
                    <td>{{time.stats["derrotas"]}}</td>
                    <td>{{time.stats["gols_pro"]}}</td>
                    <td>{{time.stats["gols_contra"]}}</td>
                    <td>{{time.Saldo_Gols()}}</td>
                </tr>
                % end
            </tbody>
        </table>
    </div>
</div>