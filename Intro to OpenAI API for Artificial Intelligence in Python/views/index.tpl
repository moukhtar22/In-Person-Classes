<h1>Web App</h1>
<form action="/" method="post">
    Create an Image: <input type="text" name="query">
    <br>
    <input type="submit">
</form>

<p><strong>Query:</strong> {{query}}</p>
<p><strong>Revised Prompt:</strong> {{revised_prompt}}</p>

% for item in gallery:
    <div style="display:inline-block;width:200px; height:auto; vertical-align:top;">
        <img style="width:100%; height:auto;" src="/static/{{item[0]}}">
        <p>{{item[1]}}</p>
    </div>
% end