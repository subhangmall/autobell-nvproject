import jetson.inference
import jetson.utils
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--camera", help="Protocol://CameraPath; ex: v4l2:///dev/video0, csi://0", default="v4l2:///dev/video0")
args = parser.parse_args()
print(args.camera)
#note: if you don't hear the bell sound: 1. ensure that your sound is working, 2. go into pulseaudio volume control, turn your volume up, go to playback, and turn all the sliders up

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5) #network used is ssd-mobilenet-v2
cameraProtocolFSRepresentation = args.camera #ex: v4l2:///dev/video1, v4l2:///dev/video0, csi://0 etc.. (Interface://FSRepresentation)
camera = jetson.utils.videoSource(cameraProtocolFSRepresentation) #set the camera to the camera interface plus the camera filesystem representation

personNumberInFront = [0, 0, 0] #[currentamountofpeople, oldamountofpeople, reallyoldamountofpeople], for comparison purposes

while True:
        img = camera.Capture()
        detections = net.Detect(img) #classify the image and the objects
        for detection in detections: #going thorough each detection
                print(detection.ClassID, " ", net.GetClassDesc(detection.ClassID))
                if detection.ClassID in range(1, 3): #ID 1: person, ID 2: bike, if the ID is equal to 1 or 2, execute the below
                        personNumberInFront[0] += 1 #since this runs in a loop, every time a human/bike is the object, add 1 to the personNumberInFront to get the total number of people in the frame
        if (personNumberInFront[0] > 0) and (personNumberInFront[0] != personNumberInFront[1] or personNumberInFront[1] != personNumberInFront[2]): #if there are people in front, but not the same amount as the last 2 times, ring the bell
                os.system("mpv bell.mp3")
        personNumberInFront[2] = personNumberInFront[1] #set the reallyoldamountofpeople to the oldamountofpeople
        personNumberInFront[1] = personNumberInFront[0] #set the oldamountofpeople to the currentamountofpeople, but if the currentamountofpeople is personNumberInFront is 0, don't do that
        personNumberInFront[0] = 0  #reset the currentamountofpeople to 0
        print(personNumberInFront)
