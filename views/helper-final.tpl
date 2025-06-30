%# helper-final.tpl - Componentes reutilizáveis para o simulador do Brasileirão

%# Componente de card de partida
% def match_card(partida, editable=False):
<div class="match-card mb-3 p-3 border rounded">
    <div class="row align-items-center">
        <div class="col-md-5 text-end">
            <img src="/static/images/{{partida.casa.img_path}}" width="40">
            <strong>{{partida.casa.sigla}}</strong>
        </div>
        
        <div class="col-md-2 text-center">
            % if editable:
            <input type="number" name="casa_{{partida.id}}" class="form-control" min="0" 
                   value="{{partida.casa_placar if partida.casa_placar is not None else ''}}">
            <span class="mx-2">x</span>
            <input type="number" name="fora_{{partida.id}}" class="form-control" min="0"
                   value="{{partida.fora_placar if partida.fora_placar is not None else ''}}">
            % else:
            <h4>{{partida.casa_placar if partida.casa_placar is not None else '-'}} x 
                {{partida.fora_placar if partida.fora_placar is not None else '-'}}</h4>
            % end
        </div>
        
        <div class="col-md-5">
            <img src="/static/images/{{partida.fora.img_path}}" width="40">
            <strong>{{partida.fora.sigla}}</strong>
        </div>
    </div>
</div>
% end

%# Componente de linha da tabela de classificação
% def tabela_row(time, posicao):
<tr>
    <td>{{posicao}}</td>
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

%# Componente de card de jogador
% def jogador_card(jogador):
<div class="col-md-4 mb-3">
    <div class="card h-100">
        <div class="card-body">
            <h5 class="card-title">
                <span class="badge bg-primary">#{{jogador.numero}}</span>
                {{jogador.nome}}
            </h5>
            <p class="card-text">
                <span class="badge bg-secondary">{{jogador.posicao}}</span>
            </p>
        </div>
    </div>
</div>
% end