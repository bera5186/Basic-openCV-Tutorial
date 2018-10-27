# Basic OpenCV Tutorial

This repository contains a complete tutorial of basic OpenCV functionalities for begginers.
OpenCV is basically library for image procesing. It has bindings in C++, Python, Java. But we will use python version in this tutorial.

## How to Install OpenCV

>No need to build OpenCV from source or binary. Instead we will use python binding for OpenCV ie. python-opencv.

## PreRequisites :
1. Python 3.x installed in system.
2. pip installed in your system.
3. :sparkles: You are ready to go.

## Step 1:

**Create a virtual environment using virtualenv:**
```python
# install virtualenv
$ pip install virtualenv
# to create an environment just type virtualenv then env name
$ virtualenv opencv
# activate the env
$ source opencv/bin/activate
```
## Step 2:
**Confused How to install it ? Just type in the command below in your terminal.**
```plain
(opencv) $ pip install python-opencv
```
**Or you can simply download the wheel file uploaded in this repository and type the command**
```plain
(opencv) $ pip install opencv_python-3.4.3.18-cp36-cp36m-manylinux1_x86_64.whl
```
## Step 3:
**Check your installation by importing cv2:**
```python
>>> import cv2
```
If no error is raised then :tada: you are ready to :rocket: .


# Contributing to this repo :
Contributers are always welcomed :smiley:  to contribute in this repo. As this repo teaches from the begining lot of peoples will learn from it.

**Steps for contributing to this repo :**
* Fork this repo.
* Add or delete things according to you.
* Open a Pull-Request
* Wait while your changes are being evaluated .

```python
if pr.merged() == True:
    print('Congrats')
elif pr.AskedForSomeChanges() == True:
    dosomeChanges()
    pr.createNewpr()
else :
    print('Sorry it was not up to the mark')
