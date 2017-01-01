console.log("LOADED: base_main.js");
requirejs.config({
	paths: {
		jQuery: '/static/bower_components/jquery/dist/jquery.min',
		bootstrap: '/static/bower_components/bootstrap/dist/js/bootstrap.min',
		underscore: '/static/bower_components/underscore/underscore-min'
	},
	"shim": {
		"bootstrap": ["jQuery"]
	}
});

define([], function() {
});
