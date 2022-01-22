# ---------------------------------------------------------------------
# Project "Track 3D-Objects Over Time"
# Copyright (C) 2020, Dr. Antje Muntzinger / Dr. Andreas Haja.
#
# Purpose of this file : Kalman filter class
#
# You should have received a copy of the Udacity license together with this program.
#
# https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013
# ----------------------------------------------------------------------
#

# imports
import numpy as np

# add project directory to python path to enable relative imports
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import misc.params as params 

class Filter:
    '''Kalman filter class'''
    def __init__(self):
        self.dim_state = params.dim_state # process model dimension
        self.dt = params.dt # time increment
        self.q=params.q # process noise variable for Kalman filter Q

    def F(self):
        ############
        # TODO Step 1: implement and return system matrix F
        ############
        F = np.identity(self.dim_state).reshape(self.dim_state, self.dim_state)
        for i, j in zip(range(int(self.dim_state/2)), range(int(self.dim_state/2), self.dim_state, 1)):
            F[i, j] = self.dt
        return np.matrix(F)

    def Q(self):
        ############
        # TODO Step 1: implement and return process noise covariance Q
        ############
        qq = self.dt * self.q
        Q = np.zeros((self.dim_state, self.dim_state))
        np.fill_diagonal(Q, qq)
        return np.matrix(Q)

    def predict(self, track):
        ############
        # TODO Step 1: predict state x and estimation error covariance P to next timestep, save x and P in track
        ############
        x = self.F() * track.x  # state prediction
        P = self.F() * track.P * self.F().transpose() + self.Q() # covariance prediction
        track.set_x(np.matrix(x))
        track.set_P(np.matrix(P))

    def update(self, track, meas):
        ############
        # TODO Step 1: update state x and covariance P with associated measurement, save x and P in track
        ############
        
        #track.update_attributes(meas)
        H = meas.sensor.get_H(track.x) # measurement matrix
        gamma = self.gamma(track, meas) # residual
        S = self.S(track, meas, H) # covariance of residual
        K = track.P * H.transpose()* np.linalg.inv(S) # Kalman gain
        x = track.x + K * gamma # state update
        I = np.identity(self.dim_state)
        P = (I - K * H) * track.P # covariance update
        track.set_x(np.matrix(x))
        track.set_P(np.matrix(P))
        track.update_attributes(meas)
    
    def gamma(self, track, meas):
        ############
        # TODO Step 1: calculate and return residual gamma
        ############
        # gamma = z - H*x # residual
        return np.matrix(meas.z - meas.sensor.get_hx(track.x))
        
    def S(self, track, meas, H):
        ############
        # TODO Step 1: calculate and return covariance of residual S
        ############
        # S = H*P*H.transpose() + R # covariance of residual
        return np.matrix(H * track.P * H.transpose() + meas.R)
