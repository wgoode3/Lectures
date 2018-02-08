$(document).ready(function(){
	console.log("jquery is ready");
	var uri = "https://newsapi.org/v2/top-headlines";
	var src = "?sources=google-news";
	var key = "&apiKey=1d7cea5143fc43838ed03210bc5ee950";

	$.get(uri + src + key, function(data){
		console.log(data);

		for(var i=0; i < data.articles.length; i++){
			$("#container").append(
			`<div class= "NewsStory">
				<h3>${data.articles[i].title}</h3>
				<img src="${data.articles[i].urlToImage}" alt="" width="500px">
				<a href="${data.articles[i].url}"><button>Show Article</button></a>
			</div>`
			);
			console.log(data.articles[i]);
		}
	});
});