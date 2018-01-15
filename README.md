# nwHacks2018
Project for nwHacks2018

## TrashCam 
An image recognition and hardware hack used to help teach individuals to sort their garbage from recyclables and compostable material. 
https://devpost.com/software/trashcam

### Software Used
* Node.js backend server
* Raspberry Pi interface
* Bootstrap frontend  
* Amazon Reckognition 

### Tech Stack and How It Works
1. Raspberry pi is running python and is connected to a webcam that takes a photo about twice a second and runs opencv functions to find the largest object in the frame.
2. If the object is larger than a threshold value, the image is posted to a lightsail server running server.js.
3. The server puts the image into an s3 bucket and runs AWS Rekognition on it to get a list of tags for the image.
4. If a tag with high enough confidence matches one of our known tags, we respond to the post request with numbers that correspond to either trash, recycling, or compost.  If our server doesn't recognize the tags, we send a number that corresponds to opening all 3 bins.
5. The rPie gets the response and opens the correct bin(s).


