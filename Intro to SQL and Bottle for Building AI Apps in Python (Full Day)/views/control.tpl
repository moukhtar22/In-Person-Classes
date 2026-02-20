% for x in roster:
    {{x}} <br>
% end

% for x in roster:
    {{x['name']}} -- {{x['age']}} <br>
% end

% for x in roster:
    % if x['age'] >= 18:
        % status = 'adult'
    % elif x['age'] >= 13 and x['age'] < 18:
        % status = 'teenager'
    % else:
        % status = 'child'
    % end
    {{x['name']}} -- {{x['age']}} -- {{ status }}<br>
% end