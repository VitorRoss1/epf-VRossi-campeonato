% rebase('layout', title=f'Elenco - {time.nome}')

<div class="card">
    <div class="card-header">
        <h2>
            <img src="/static/images/{{time.img_path}}" alt="{{time.nome}}" width="40">
            {{time.nome}} ({{time.sigla}})
        </h2>
    </div>
    <div class="card-body">
        <h3>Elenco Titular</h3>
        <div class="row">
            % for jogador in time.getJogadores:
            <div class="col-md-4 jogador-card">
                <div class="card mb-3">
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
