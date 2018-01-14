"""
import boto3


if __name__ == "__main__":
    fileName='Good WinLoss.png'
    bucket='trash-cam'

    client=boto3.client('rekognition')

    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':fileName}},MinConfidence=75)

    print('Detected labels for ' + fileName)
    print(response)
    for label in response['Labels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))




"""
import boto3


BUCKET = "trash-cam"
KEY = "1.jpg"



def detect_labels(bucket, key, max_labels=10, min_confidence=90, region="us-east-1"):
	rekognition = boto3.client("rekognition", region)
	response = rekognition.detect_labels(
		Image={
			"S3Object": {
				"Bucket": bucket,
				"Name": key,
			}
		},
		MaxLabels=max_labels,
		MinConfidence=min_confidence,
	)
	return response['Labels']


for label in detect_labels(BUCKET, KEY):
	print ("{Name} - {Confidence}".format(**label))



"""
	Expected output:
	People - 99.2436447144%
	Person - 99.2436447144%
	Human - 99.2351226807%
	Clothing - 96.7797698975%
	Suit - 96.7797698975%
"""
