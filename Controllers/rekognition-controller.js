// for aws rekognition

const Rekognition = require('node-rekognition')

// Set your AWS credentials
const AWSParameters = {
    "accessKeyId": "XXX",
    "secretAccessKey": "XXX",
    "region": "XXX",
    "bucket": "XXX",
    "ACL": "XXX" // optional
}

const rekognition = new Rekognition(AWSParameters)


/**
 * Detects instances of real-world labels within an image
 *
 * @param {Object} s3Image
 * @param {string} threshold (optional. Defaults 50)
 */
const imageLabels = await rekognition.detectLabels(s3Image)
