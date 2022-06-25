# Autobell

This is a system that can detect pedestrians and ring a bell (using speakers). This can make pedestrians safer.

## The Algorithm

Add an explanation of the algorithm and how it works. Make sure to include details about how the code works, what it depends on, and any other relevant info. Add images or other descriptions for your project here. 
This program uses a pretrained ssd-mobilenet-v2 and detectNet. The code works by asking the algorithm what it sees in the image, sorting through them using a loop, and if it detects a person/bike, adding one to the personNumberInFront[0] variable. The next part of this code plays the bell sound (using mpv), if the personNumberInFront[0] variable is greater than 0, and if the personNumberInFront[0] isn't equal to the last personNumberInFront[1 and 2]. The next part of this program sets personNumberInFront[2] to personNumberInFront[1] and personNumberInFront[1] to personNumberInFront[0]. Finally, it sets personNumberInFront[0] to 0, then repeats the program. 

## Running this project

Needed libraries: jetson.utils, jetson.inference, os (os is included with python, you can install jetson.inference and jetson.utils by using this link https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md)
Needed executables: mpv 
Needed hardware: Monitor(for initial troubleshooting and running the program), speaker and soundcard (you can also just use the speaker of the monitor if it has one), jetson nano, keyboard, mouse, and ethernet cable/wifi usb stick
Setup:
1. With your monitor attached, boot up into LXDE (default nano desktop environment), go into the “start menu”, click on Sound & Video, and click on Pulseaudio Volume Control
2. Make sure it is set to the right speaker.
3. Click on “Playback”
4. Make sure the volume is turned up for the right outputs
Running the program: 
1. Clone this github repository (github.com/subhangmall/autobell-nvproject.git)
2. cd into the autobell-nvproject directory
3. run main.py by typing python3 main.py

Troubleshooting:
My audio doesn’t work:
If your audio doesn’t work, while the bell is ringing, follow these steps. Firstly, ensure you have followed all of the previous instructions and installed all the packages. Secondly, try a different speaker and change the settings. If it still doesn’t work, go to the “start menu”, click on Sound & Video, and click on Pulseaudio Volume Control and to Playback. Start the program and ensure that a human is in the webcam frame so the bell will ring. While the bell is ringing, go back to the Pulseaudio window, and make sure the audio for MPV is turned up all the way.


[View a video explanation here](video link)
