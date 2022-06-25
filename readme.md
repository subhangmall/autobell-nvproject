# Autobell

This is a system that can detect pedestrians and ring a bell (using speakers). > 

![add image descrition here](direct image link here)

## The Algorithm

Add an explanation of the algorithm and how it works. Make sure to include details about how the code works, what it depends on, and any other relevant info. Add images or other descriptions for your project here. 
This program uses a pretrained ssd-mobilenet-v2 and detectNet. The code works by asking the algorithm what it sees in the image, sorting through them using a loop, and if it detects a person/bell, adding one to the personNumberInFront[0] variable. The next part of this code plays the bell sound (using mpv), if the personNumberInFront[0] variable is greater than 0, and if the personNumberInFront[0] isn't equal to the last personNumberInFront[1 and 2]. The next part of this program sets personNumberInFront[2] to personNumberInFront[1] and personNumberInFront[1] to personNumberInFront[0].

## Running this project

1. Add steps for running this project.
2. Make sure to include any required libraries that need to be installed for your project to run.

[View a video explanation here](video link)
