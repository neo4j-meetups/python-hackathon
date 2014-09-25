<!doctype html>
<html>

  <head>
    <title>Movie List - Hackathon Movie Wiki</title>
    <link rel="stylesheet" href="/css/wiki.css">
  </head>

  <body>

    <nav><a href="/">Hackathon Movie Wiki</a> / <strong>Movies</strong></nav>

    <h1>Movies</h1>
    <ul>
    % for title, released in movies:
        <li><a href="/movie/{{title}}">{{title}} [{{released}}]</a></li>
    % end
    </ul>

  </body>

</html>

