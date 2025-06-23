% rebase('layout', title=f'Tabela - Rodada {rodada}')

<div class="card">
    <div class="card-header">
        <h2>Tabela de Classificação - Rodada {{rodada}}</h2>
    </div>
    <div class="card-body">
        <table class="table">
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
                % for i, time in enumerate(tabela):
                <tr>
                    <td>{{i+1}}</td>
                    <td>
                        <a href="/time/{{time.id}}">
                            <img src="/static/images/{{time.img_path}}" alt="{{time.nome}}" width="30">
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