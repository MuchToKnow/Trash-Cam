const fs = require('fs');
var S3FS = require('s3fs');
const AWS = require('aws-sdk');
var PythonShell = require('python-shell');
var rekog = require('./js-rekognition');
var match = require('./matching');
var server = require('./../server.js');
var keys = require('./../keys.js')

//Sends the image to an s3 bucket so far...
module.exports.request = function(request, response){
		console.log("request firing");
		var image = request.body.image;
		var buf = new Buffer(request.body.image.replace(/^data:image\/\w+;base64,/, ""), "base64");
		AWS.config.update({
  		accessKeyId: keys.key0,
  		secretAccessKey: keys.key1,
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
  console.log("doAfter " + data)
  switch (data) {
    case 1: server.incCompost();
            break;
    case 2: server.incRecycle();
            break;
    case 3: server.incGarbage();
            break;
  }

  response.json({
		status : data
	});
}
