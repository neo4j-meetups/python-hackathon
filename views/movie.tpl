<!doctype html>
<html>

  <head>
    <title>{{title}} [{{released}}] - Hackathon Movie Wiki</title>
    <link rel="stylesheet" href="/css/wiki.css">
  </head>

  <body>

    <nav><a href="/">Hackathon Movie Wiki</a> / <a href="/movies/">Movies</a> / <strong>{{title}}</strong></nav>

    <h1>{{title}}</h1>

    <h2>Movie Details</h2>
    <dl>
        <dt>Title:</dt>
          <dd>{{title}}</dd>
        <dt>Released:</dt>
          <dd>{{released}}</dd>
        <dt>Director:</dt>
          <dd><a href="/person/{{director}}">{{director}}</a></dd>
    </dl>

    <h2>Cast</h2>
    <ul>
    % for name in sorted(actors):
        <li><a href="/person/{{name}}">{{name}}</a></li>
    % end
    </ul>

    <div class="footer">
      <code>(graphs)-[:ARE]->(everywhere)</code>
      <p>With &hearts; from Sweden &amp; the <a href="http://neo4j.com/community/">Neo4j Community</a></p>
    </div>

  </body>

</html>

