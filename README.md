# simple-yolo-object-recognition

simple YOLO implementation (Windows)

## Requirement
* Python 3.7
* OpenCV
* Tensorflow 1.15.0
* Pillow
* Cython
* Microsoft Visual C++ Redistributable Package
* CPUs wich support AVX2 Instruction

## Installation
#### Install Python 3.7
> Download from https://www.python.org/ftp/python/3.7.4/python-3.7.4-amd64.exe

#### Install OpenCV
``` # pip install opencv-python ```

#### Install Pillow
``` # pip install pillow ```

#### Install Cython
``` # pip install cython ```

#### Install Tensorflow 1.15.0
``` # pip install tensorflow==1.15.0 ```

#### Install Microsoft Visual C++ Redistributable Package
> Download Visual Studio from https://visualstudio.microsoft.com/downloads/ and install Windows 10 SDK Component

After installation, open cmd and go to project folder

#### Download yolo.weights
> Download yolo.weights file from https://drive.google.com/drive/folders/0B1tW_VtY7onidEwyQ2FtQVplWEU and copy to bin

#### Build Darknet
``` 
# python setup.py build_ext --inplace
# pip install -e .
```

## Run script
``` > python object_recognition.py ```

## Result
![Sample 1](https://res.cloudinary.com/dimasdwib/image/upload/v1574622667/ss1_f3ogb6.png)

![Sample 2](https://res.cloudinary.com/dimasdwib/image/upload/v1574622666/ss2_w9ng8k.png)
