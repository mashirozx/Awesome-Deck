from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("""

    <!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<title>Awesome Deck</title>

	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/normalize.css@8.0.1/normalize.min.css">


	<link rel="stylesheet" href="/static/page/css/style.css">


</head>

<body>

	<div class="cover-logo">
		Awesome Deck
	</div>
	<div class="text-input">
		<input type="text" id="deck-code-input" placeholder="Paste your deck code here!">
		<label for="input1">Deck Code</label>
		<button id="commit" onclick="javascript:commit()">Button</button>
	</div>
	<div class="menu">
		<table>
			<tr>
				<th>API</th>
				<th>Blog</th>
				<th>Share</th>
			</tr>
		</table>
	</div>

	<script>
		console.log("0");
		(function() {

			var input = document.getElementById("deck-code-input");
			input.addEventListener("keyup", function(event) {
				event.preventDefault();
				if (event.keyCode === 13) {
					document.getElementById("commit").click();
				}
			});
		})();

		function commit() {
			var deckCodeInputEl = document.getElementById("deck-code-input");
			var newDeck = deckCodeInputEl.value;
			var deckCode = encodeURIComponent((newDeck || "").trim());
			window.location.href =
				window.location.protocol + "//" + window.location.host +
				"/deck/?name=&code=" + deckCode;
				//"http://123.207.63.52:8000/deck/?name=&code=" + deckCode;
		}

	</script>

</body>

</html>


    """)
