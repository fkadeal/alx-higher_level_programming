ON( "https://swapi-api.hbtn.io/api/people/5/?format=json", function( json ) {
	    $('#character').html(json.name);
});