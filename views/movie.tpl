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
    
    <h2>Reviews</h2>
    % for review in reviews:
        <blockquote>{{review.comments}}</blockquote>
    % end
    <form method="POST" action="review">
    <h3>Submit a new review</h3>
    <input type="hidden" name="title" value="{{title}}">
    <textarea name="comments" cols="80" rows="6"></textarea>
    <input type="submit" value="Submit">
    </form>

  </body>

</html>

