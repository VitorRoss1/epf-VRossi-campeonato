% rebase('layout', title=f'{time.nome}')

<div class="card">
    <div class="card-header">
        <h2>
            <img src="/static/images/{{time.img_path}}" width="50">
            {{time.nome}} ({{time.sigla}})
        </h2>
    </div>
    <div class="card-body">
        <h3>Estatísticas</h3>
        <ul>
            <li>Pontos: {{time.stats["Pontos"]}}</li>
            <li>Vitórias: {{time.stats["vitorias"]}}</li>
            <li>Empates: {{time.stats["empates"]}}</li>
            <li>Derrotas: {{time.stats["derrotas"]}}</li>
            <li>Gols Pró: {{time.stats["gols_pro"]}}</li>
            <li>Gols Contra: {{time.stats["gols_contra"]}}</li>
            <li>Saldo de Gols: {{time.Saldo_Gols()}}</li>
        </ul>
        
        <h3>Elenco</h3>
        <div class="row">
            % for jogador in time.getJogadores:
            <div class="col-md-4 mb-3">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">#{{jogador.numero}} {{jogador.nome}}</h5>
                        <p class="card-text">{{jogador.posicao}}</p>
                    </div>
                </div>
            </div>
            % end
        </div>
    </div>
</div>
