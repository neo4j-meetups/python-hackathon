<!doctype html>
<html>

  <head>
    <title>{{name}} - Hackathon Movie Guide</title>
    <link rel="stylesheet" href="/css/main.css">
  </head>

  <body>

    <div class="header">
      <nav><a href="/">Hackathon Movie Guide</a> / <a href="/person/">People</a> / <strong>{{name}}</strong></nav>
    </div>

    <h1>{{name}}</h1>

    <h2>Personal Details</h2>
    <dl>
        <dt>Name:</dt>
          <dd>{{name}}</dd>
        <dt>Born:</dt>
          <dd>{{born}}</dd>
    </dl>

    <h2>Movies</h2>
    <ul>
    % for movie, role in sorted(movies):
        <li class="{{role}}"><a href="/movie/{{movie}}">{{movie}}</a> [{{role}}]</li>
    % end
    </ul>

    <div class="footer">
      <code>(graphs)-[:ARE]->(everywhere)</code>
      <p>With &hearts; from Sweden &amp; the <a href="http://neo4j.com/community/">Neo4j Community</a></p>
    </div>

  </body>

</html>

