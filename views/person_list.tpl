<!doctype html>
<html>

  <head>
    <title>Person List - Hackathon Movie Wiki</title>
    <link rel="stylesheet" href="/css/wiki.css">
  </head>

  <body>

    <nav><a href="/">Hackathon Movie Wiki</a> / <strong>People</strong></nav>

    <h1>People</h1>
    <ul>
    % for name, in people:
        <li><a href="/person/{{name}}">{{name}}</a></li>
    % end
    </ul>

  </body>

</html>

