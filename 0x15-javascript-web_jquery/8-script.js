$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, txtStat) {
  $('ul#list_movies').html(data.results.map(function(res){
	return `<li>${res.title}</li>`
	}));
});
