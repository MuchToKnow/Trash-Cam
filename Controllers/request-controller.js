const fs = require('fs');
var S3FS = require('s3fs');
const AWS = require('aws-sdk');
var PythonShell = require('python-shell');
var rekog = require('./js-rekognition');
var match = require('./matching');
var server = require('~/server.js');

//Sends the image to an s3 bucket so far...
module.exports.request = function(request, response){
		console.log("request firing");
		var image = request.body.image;
		var buf = new Buffer(request.body.image.replace(/^data:image\/\w+;base64,/, ""), "base64");
		AWS.config.update({
  		accessKeyId: 'AKIAI7GICYUEB2SRSQUA',
  		secretAccessKey: 'D+uLnTf5qzV0lt3vZVCIkbMs1cO8Ye4lcpGCq9h5',
  		region: 'us-east-1'
		});
		const s3 = new AWS.S3({
  			apiVersion: '2006-03-01',
  			params: { Bucket: 'trash-cam' }
		});
		var params = {
		Body: buf,
		Key: "toProcess.jpg",
		ContentEncoding: 'base64',
		ContentType: 'image/jpeg'
		};
		s3.putObject(params, function(err,data){
			if(err){
				console.log(err, err.stack);
			}
			else{
				console.log(data);
				console.log("trying recognition");
				rekog.rekog(match.matching, doAfter, response);
				console.log("recognition done");
			}
		});
	}

function doAfter(data, response){
  switch (data) {
    case 1: server.incrementCompost
    case 2: server.incrementRecycle
    case 3: server.incrementGarbage
  }

  response.json({
		status : data
	});
}
