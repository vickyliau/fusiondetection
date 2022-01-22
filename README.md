# Sensor Fusion and Object Detection

This project aims for fusing camera data with LIDAR data. 

## Initial Tracking

python loop_over_dataset.py

![alt_text](https://github.com/vickyting0910/fusiondetection/blob/main/img/track0.png)

![alt_text](https://github.com/vickyting0910/fusiondetection/blob/main/img/rmse0.png)


## Kalman Filter: filter.py

- training_segment-10072231702153043603_5725_000_5745_000_with_camera_labels.tfrecord

- show_only_frames = [150, 200]

- configs_det = det.load_configs(model_name='fpn_resnet')

- configs_det.lim_y = [-5, 10]

1. system matrix F

2. process noise covariance Q

3. predict state x and estimation error covariance P to next timestep

4. update state x and covariance P with associated measurement

![alt_text](https://github.com/vickyting0910/fusiondetection/blob/main/img/track1.png)

![alt_text](https://github.com/vickyting0910/fusiondetection/blob/main/img/rmse1.png)


## Track: trackmanagement.py

- show_only_frames = [65, 100]

- configs_det.lim_y = [-5, 15]

1. Track initialization from unassigned measurements

2. Track Score

3. Track States

4. Old Tracks

![alt_text](https://github.com/vickyting0910/fusiondetection/blob/main/img/track2.png)

![alt_text](https://github.com/vickyting0910/fusiondetection/blob/main/img/rmse2.png)


## association.py

- training_segment-1005081002024129653_5313_150_5333_150_with_camera_labels.tfrecord

- show_only_frames = [0, 200] in order to use the whole sequence now.

- configs_det.lim_y = [-25, 25]

1. Nearest neighbor data association

2. nearest track and measurement for association

3. Gating method with chi-square-distribution

![alt_text](https://github.com/vickyting0910/fusiondetection/blob/main/img/track3.png)

![alt_text](https://github.com/vickyting0910/fusiondetection/blob/main/img/rmse3.png)

![alt_text](https://github.com/vickyting0910/fusiondetection/blob/main/images/animation_step3.avi)


## measurements.py

1. Camera measurements

2. Nonlinear camera measurement model h(x)

3. checks whether an object can be seen by the camera or is outside the field of view

![alt_text](https://github.com/vickyting0910/fusiondetection/blob/main/img/track4.png)

![alt_text](https://github.com/vickyting0910/fusiondetection/blob/main/img/rmse4.png)

![alt_text](https://github.com/vickyting0910/fusiondetection/blob/main/images/animation_step4.avi)

