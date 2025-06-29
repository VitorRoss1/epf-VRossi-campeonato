% rebase('layout', title=f'Rodada {rodada}')

<div class="card">
  <div class="card-header bg-primary text-white">
    <h2>Rodada {{rodada}}</h2>
  </div>
  <div class="card-body">
    <form action="/campeonato/enviar-placares" method="post">
      <input type="hidden" name="rodada" value="{{rodada}}">
      
      % for partida in partidas:
      <div class="match-card mb-4 p-3 border rounded">
        <div class="row align-items-center">
          <div class="col-md-5 text-end">
            <img src="/static/images/{{partida.casa.img_path}}" width="40">
            <strong>{{partida.casa.sigla}}</strong>
          </div>
          
          <div class="col-md-2 text-center">
            <input type="number" name="casa_{{partida.id}}" class="form-control" min="0">
            <span class="mx-2">x</span>
            <input type="number" name="fora_{{partida.id}}" class="form-control" min="0">
          </div>
          
          <div class="col-md-5">
            <img src="/static/images/{{partida.fora.img_path}}" width="40">
            <strong>{{partida.fora.sigla}}</strong>
          </div>
        </div>
      </div>
      % end
      
      <button type="submit" class="btn btn-primary">Calcular Tabela</button>
    </form>
  </div>
</div>