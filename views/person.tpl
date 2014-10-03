<!doctype html>
<html>

  <head>
    <title>{{name}} - Hackathon Movie Wiki</title>
    <link rel="stylesheet" href="/css/wiki.css">
  </head>

  <body>

    <nav><a href="/">Hackathon Movie Wiki</a> / <a href="/person/">People</a> / <strong>{{name}}</strong></nav>

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

