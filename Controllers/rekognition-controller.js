function getRekognition () {
  //var rekognitionScript = "rekognition.py";
  console.log("right before data return");
  /*var spawn = require("child_process").spawn;
  var process = spawn('python',["rekognition.py"]);

  process.stdout.on('data', (data) => {
    console.log(uint8arrayToString(data));
    return data;
  });*/
}
module.exports.getRekognition = getRekognition();

/*
// for aws rekognition

const Rekognition = require('node-rekognition')

// Set your AWS credentials
const AWSParameters = {
    "accessKeyId": "AKIAI7GICYUEB2SRSQUA",
    "secretAccessKey": "D+uLnTf5qzV0lt3vZVCIkbMs1cO8Ye4lcpGCq9h5",
    "region": "us-east-1",
    "bucket": "trash-cam",
  //  "ACL": "XXX" // optional
}

const rekognition = new Rekognition(AWSParameters)


var s3Image = "currentImg.jpg"

*/

/**
 * Detects instances of real-world labels within an image
 *
 * @param {Object} s3Image
 * @param {string} threshold (optional. Defaults 50)
 */

/*
const imageLabels = await rekognition.detectLabels(s3Image)

console.log(imageLabels);
*/
