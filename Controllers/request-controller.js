const fs = require('fs');
var S3FS = require('s3fs');

module.exports.request = function(request, response){
		var image = request.image;
		//Parse base64 image and store in root folder with filename 'currentImg'
		fs.open('currentImg.txt', image, function(err, fd){
			if(err){
				throw 'error opening file: ' + err;
			}

			fs.write(fd, )
		})

		//Doesn't work
		fs.writeFile('currentImg.txt', image, function(err) {
			if(err){
				var mes = 'Error while writing file to server' + err;
				response.json({
					status: 0,
					message: mes
				});
				return console.log(err);
			}
			console.log('File saved!');
		});

		//Works
		var sf3sImpl = new S3FS('trash-cam', {
			accessKeyId: "AKIAI7GICYUEB2SRSQUA",
			secretAccessKey: "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"
		});

		sf3sImpl.create();
		var stream = fs.createReadStream('currentImg.txt');
		sf3sImpl.writeFile('toProcess.txt', stream).then(function(){
			fs.unlink('currentImg.txt', function(err){
				if(err){
					console.error(err);
				}
			});
		});
	}