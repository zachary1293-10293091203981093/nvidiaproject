# Dog Detector

This project was made to solve the problem of our dogs pooping in our rooms. The webcam will be placed in the hallway and checks for a dog every frame and prints a message based on if there is one or not.

![Output of the code in the terminal]([Imgur](https://imgur.com/3JYoaYc))

## The Algorithm

Add an explanation of the algorithm and how it works. Make sure to include details about how the code works, what it depends on, and any other relevant info. Add images or other descriptions for your project here. 

This project uses SSD Mobilenet V2, which is an efficient neural network designed for image recognition. It employs techniques such as depthwise separable convolution, inverted residuals, and global average pooling to optimize the computational efficiency of the network, making it suitable for deployment on resource-constrained devices like the Jetson Nano. It's an advanced AI model that excels at quickly and accurately identifying objects within images by intelligently processing visual information. The code captures an image every second and uses SSD Mobilenet V2 to get the ClassID of the objects in the image and then if the object is a dog, it reacts by printing a message saying there is one. If there isn't a dog, it will print a message saying there isn't one.

![Full code]([[Imgur](https://imgur.com/0sUbFe0))
## Running this project

1. Before running the code, you need to connect the webcam to the Jetson Nano. For me, I used terminal to run this code. To run the project,    first you have to change directories into the file with the project. I named the file "my" and the project "project.py", so the code for     running the project would be:                                                                                                           
   $ cd my                                                                                                                              
   $ python3 project.py /dev/video0
2. You have to download SSD Mobilenet V2 before running the code. The code to download it from terminal is:                                 
   $ cd jetson-inference/python/training/detection/ssd                                                                                      
   $ wget https://nvidia.box.com/shared/static/djf5w54rjvpqocsiztzaandq1m3avr7c.pth -O models/mobilenet-v1-ssd-mp-0_675.pth                 
   $ pip3 install -v -r requirements.txt
[View a video explanation here](video link)
