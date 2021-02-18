# gRPC Image Project


##### Description
gRPC is an alternative to REST and runs on HTTP2, which is a newer, more efficient communication protocol than its 
predecessor HTTP1. gRPC uses protocol buffers as its underlying message interchange format, allowing a client to call
service methods as if they were local.

This project explores gRPC through an image service that transposes and blurs images.


##### Design
A protocol buffer interface was chosen to model images, along with their affiliated request objects.
A gRPC client and server are ran separately from the command line, where input and configuration parameters can be 
provided.


##### Contents

    input - directory containing sample images
    output - directory for service output
    proto - directory containing protobuf service interface file
    build - build shell script
    client - script that implements and runs gRPC client
    requirements.txt - text file containing list of used packages
    server - script that implements and runs gRPC service
    setup - setup shell script
    utils.py - script containing various utility functions


##### Installation
At the terminal, type `pip install -r requirements.txt`


##### Run
To run the code, open two terminals. In one, enter `./client [args]`. In the other, enter `./server [args]`.

