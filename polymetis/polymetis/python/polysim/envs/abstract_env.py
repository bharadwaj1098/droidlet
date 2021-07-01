# Copyright (c) Facebook, Inc. and its affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
import abc
import numpy as np


class AbstractControlledEnv(abc.ABC):
    """Parent class for simulation environments."""

    @abc.abstractmethod
    def reset(self):
        """Reset the environment."""
        pass

    @abc.abstractmethod
    def get_num_dofs(self):
        """Get the number of degrees of freedom for controlling the simulation.

        Returns:
          int: Number of control input dimensions
        """
        pass

    @abc.abstractmethod
    def get_current_joint_pos_vel(self):
        """
        Returns:
          np.ndarray: Joint positions
          np.ndarray: Joint velocities
        """
        pass

    @abc.abstractmethod
    def get_current_joint_torques(self):
        """
        Returns:
          np.ndarray: Torques received from apply_joint_torques
          np.ndarray: Torques sent to robot (e.g. after clipping)
          np.ndarray: Torques generated by the actuators (e.g. after grav comp)
          np.ndarray: Torques exerted onto the robot
        """
        pass

    @abc.abstractmethod
    def apply_joint_torques(self, torques):
        """
        input:
          np.ndarray: Desired torques
        """
        pass