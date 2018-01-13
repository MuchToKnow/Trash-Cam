var fs = require('fs');

module.exports.request = function(request, response){
	var image = request.image;
	//Parse base64 image and store in root folder with filename 'currentImg'
		var file = image;
		fs.writeFile('currentImg.txt', image, (err) => {
			if(err) throw err;	
			console.log('File saved!');
		});
	}
}