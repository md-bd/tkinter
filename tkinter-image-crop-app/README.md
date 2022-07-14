# Image Crop Application

This app loads an image, then user can crop that image and then save the cropped image. 

I have added a dockerfile to create the application image. The image is tested on ubuntu 20.04.

## How to run the application

First create the docker image by running this command:

```
docker build -t md/tkinter_docker_image:v0 .
```

This will create docker image named md/tkinter_docker_image:v0. Now we can run a docker container using this image:

```
docker run -u=$(id -u $USER):$(id -g $USER) -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix:rw -v $(pwd):/app --rm -it md/tkinter_docker_image:v0 
```


The application should open after the docker run command. You can browse a png image file and see it on display. If we need to crop the image, we can click the crop button and start cropping the image. After the crop area is fixed, one can again click the crop button to crop the image. After the crop user can also save the image by clicking the save button.

