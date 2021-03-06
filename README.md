https://github.com/Wyverns010/Body-Keypoints-Detection.git

## Original repo
**[quanhua92/human-pose-estimation-opencv](https://github.com/quanhua92/human-pose-estimation-opencv.git)**

# human-pose-estimation-opencv
Perform Human Pose Estimation in OpenCV Using OpenPose MobileNet

![OpenCV Using OpenPose MobileNet](output.JPG)


# How to use current impl

- Test with image
```
python keypoints_detector.py
```

**Things to Note**:

* All images that being processed by the code are in `images` folder
* The keypoints for all the iamgesw processed are stored in `keypoints.csv` file

# How to use

- Test with webcam

```
python openpose.py
```

- Test with image
```
python openpose.py --input image.jpg
```

- Use `--thr` to increase confidence threshold

```
python openpose.py --input image.jpg --thr 0.5
```

## Notes(quanhua92, original author):
- I modified the [OpenCV DNN Example](https://github.com/opencv/opencv/blob/master/samples/dnn/openpose.py) to use the `Tensorflow MobileNet Model`, which is provided by [ildoonet/tf-pose-estimation](https://github.com/ildoonet/tf-pose-estimation/tree/master/models/graph/mobilenet_thin), instead of `Caffe Model` from CMU OpenPose. The original `openpose.py` from `OpenCV example` only uses `Caffe Model` which is more than 200MB while the `Mobilenet` is only 7MB.
- Basically, we need to change the `cv.dnn.blobFromImage` and use `out = out[:, :19, :, :]` to get only the first 19 rows in the `out` variable.