# Dog Detector

This project was made to solve the problem of our dogs pooping in our rooms. The webcam will be placed in the hallway and checks for a dog every frame and prints a message based on if there is one or not.

![add image description here](direct image link here)

## The Algorithm

Add an explanation of the algorithm and how it works. Make sure to include details about how the code works, what it depends on, and any other relevant info. Add images or other descriptions for your project here. 

This project uses SSD Mobilenet V2, which is an efficient neural network designed for image recognition. It employs techniques such as depthwise separable convolution, inverted residuals, and global average pooling to optimize the computational efficiency of the network, making it suitable for deployment on resource-constrained devices (e.g Jetson Nano). Essentially, it's an advanced artificial intelligence (AI) model that excels at quickly and accurately identifying objects within images by intelligently processing visual information.. 

## Running this project

1. Add steps for running this project.
   For me, I used terminal to run this code. To run the project, first you have to change directories into the file with the project. I 
   named the file "my" and the project "project.py", so the code for running the project would be:
   cd my
   python3 project.py /dev/video0
3. Make sure to include any required libraries that need to be installed for your project to run.
   You have to download SSD Mobilenet V2 before running. The code to download it is:
   $ cd jetson-inference/python/training/detection/ssd
   $ wget https://nvidia.box.com/shared/static/djf5w54rjvpqocsiztzaandq1m3avr7c.pth -O models/mobilenet-v1-ssd-mp-0_675.pth
   $ pip3 install -v -r requirements.txt
[View a video explanation here](video link)
