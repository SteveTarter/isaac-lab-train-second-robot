
# Copyright (c) 2022-2025, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Configuration for the Universal Robots.
Reference: https://github.com/ros-industrial/universal_robot
"""

import isaaclab.sim as sim_utils
from pathlib import Path
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg

UR_GRIPPER_CFG = ArticulationCfg(

home = Path.home()

# Where is the USD file for this robot?
spawn=sim_utils.UsdFileCfg(
    usd_path=f"{home}/git/robot-sim-assets/robots/ur/UR-with-gripper.usd",
        activate_contact_sensors=False,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            rigid_body_enabled=True,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=5.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True,
            solver_position_iteration_count=8,
            solver_velocity_iteration_count=0
        ),
    ),
# What is its initial position of the robot, and its joints?
    init_state=ArticulationCfg.InitialStateCfg(
        joint_pos={
            "shoulder_pan_joint": 0.0,
            "shoulder_lift_joint": -1.712,
            "elbow_joint": 1.712,
            "wrist_1_joint": 0.0,
            "wrist_2_joint": 0.0,
            "wrist_3_joint": 0.0,
        },
    ),
# What parts of the robot move, and how stiff / damped are they?
    actuators={
        "shoulder_pan": ImplicitActuatorCfg(
            joint_names_expr=["shoulder_pan_joint"],
            stiffness=350.0,
            damping=35.0
        ),
        "shoulder_lift": ImplicitActuatorCfg(
            joint_names_expr=["shoulder_lift_joint"],
            stiffness=350.0,
            damping=35.0
        ),
        "elbow": ImplicitActuatorCfg(
            joint_names_expr=["elbow_joint"],
            stiffness=350.0,
            damping=35.0
        ),
        "wrist_1": ImplicitActuatorCfg(
            joint_names_expr=["wrist_1_joint"],
            stiffness=350.0,
            damping=35.0
        ),
        "wrist_2": ImplicitActuatorCfg(
            joint_names_expr=["wrist_2_joint"],
            stiffness=350.0,
            damping=35.0
        ),
        "wrist_3": ImplicitActuatorCfg(
            joint_names_expr=["wrist_3_joint"],
            stiffness=350.0,
            damping=35.0
        ),
        "gripper": ImplicitActuatorCfg(
            joint_names_expr=["finger_joint"],
            stiffness=280.0,
            damping=28.0,
        ),
    }
)
