import sys
import argparse
import time

from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput, Log

# parse the command line
parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.",
                                 formatter_class=argparse.RawTextHelpFormatter,
                                 epilog=detectNet.Usage() + videoSource.Usage() + videoOutput.Usage() + Log.Usage())
parser.add_argument("input", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="ssd-mobilenet-v2", help="pre-trained model to load (see below for options)")
parser.add_argument("--overlay", type=str, default="box,labels,conf", help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use")
try:
        args = parser.parse_known_args()[0]
except:
        print("")
        parser.print_help()
        sys.exit(0)

# create video sources and outputs
input = videoSource(args.input, argv=sys.argv)
output = videoOutput(args.output, argv=sys.argv)

# load the object detection network
net = detectNet(args.network, sys.argv, args.threshold)
while True:
    # capture the next image
    img = input.Capture()

    if img is None: # timeout
        continue

    # detect objects in the image (with overlay)
    detections = net.Detect(img, overlay=args.overlay)

    for detection in detections:
        class_idx = detection.ClassID
        class_desc = net.GetClassDesc(class_idx)

        #React if ClassID is that of a dog
        if class_desc == "dog":
            print("There is a dog!")
        print("No dog on screen")
        #time.sleep(20)

        # render the image
        output.Render(img)

        # update the title bar
        output.SetStatus("{:s} | Network {:.0f} FPS".format(args.network, net.GetNetworkFPS()))

        # exit on input/output EOS
        if not input.IsStreaming() or not output.IsStreaming():
            break