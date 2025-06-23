% rebase('layout', title=f'Rodada {Rodada}')

<div class="card shadow">
    <div class="card-header bg-primary text-white">
        <h2 class="h4 mb-0">
            <i class="fas fa-calendar-alt me-2"></i>Rodada {{Rodada}}
        </h2>
    </div>
    
    <div class="card-body">
        <form action="/submit-scores" method="post">
            <input type="hidden" name="Rodada" value="{{Rodada}}">
            
            % for match in matches:
            <div class="match-card mb-4 p-3 border rounded">
                <div class="row align-items-center">
                    <div class="col-md-5 text-end">
                        <div class="d-flex align-items-center justify-content-end">
                            <img src="/static/images/{{match.home_team.img_path}}" 
                                 alt="{{match.home_team.name}}" 
                                 class="team-logo me-2">
                            <span class="fw-bold">{{match.home_team.acronym}}</span>
                        </div>
                    </div>
                    
                    <div class="col-md-2">
                        <div class="d-flex justify-content-center">
                            <input type="number" name="home_{{match.id}}" 
                                   class="form-control score-input" 
                                   min="0" required>
                            <span class="mx-2">x</span>
                            <input type="number" name="away_{{match.id}}" 
                                   class="form-control score-input" 
                                   min="0" required>
                        </div>
                    </div>
                    
                    <div class="col-md-5">
                        <div class="d-flex align-items-center">
                            <img src="/static/images/{{match.away_team.img_path}}" 
                                 alt="{{match.away_team.name}}" 
                                 class="team-logo me-2">
                            <span class="fw-bold">{{match.away_team.acronym}}</span>
                        </div>
                    </div>
                </div>
            </div>
            % end
            
            <div class="text-center mt-4">
                <button type="submit" class="btn btn-primary btn-lg">
                    <i class="fas fa-calculator me-2"></i>Calcular Classificação
                </button>
            </div>
        </form>
    </div>
</div>