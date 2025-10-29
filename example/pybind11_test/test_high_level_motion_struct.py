#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MagicDog_W SDK Python 使用示例 - 高级运动控制结构体测试

这个文件展示了如何使用 MagicDog_W SDK 的 Python 绑定来测试高级运动控制相关的结构体。
"""

import sys
import time
import magicdog_w_python as magicdog_w
from magicdog_w_python import (
    TtsCommand,
    TtsPriority,
    TtsMode,
    GetSpeechConfig,
    ErrorCode,
)


print("=== 测试系统状态结构体 ===")
# 测试成功状态
success_status = magicdog_w.Status()
success_status.code = magicdog_w.ErrorCode.OK
success_status.message = "系统运行正常，所有服务已就绪"
print(f"成功状态: 代码={success_status.code}, 消息='{success_status.message}'")

# 测试错误状态
error_status = magicdog_w.Status()
error_status.code = magicdog_w.ErrorCode.SERVICE_NOT_READY
error_status.message = "语音服务未就绪，请稍后重试"
print(f"错误状态: 代码={error_status.code}, 消息='{error_status.message}'")

# 测试状态值
if success_status.code != magicdog_w.ErrorCode.OK:
    print(f"错误: 成功状态代码不匹配")
    sys.exit(1)
if success_status.message != "系统运行正常，所有服务已就绪":
    print(f"错误: 成功状态消息不匹配")
    sys.exit(1)
if error_status.code != magicdog_w.ErrorCode.SERVICE_NOT_READY:
    print(f"错误: 错误状态代码不匹配")
    sys.exit(1)
if error_status.message != "语音服务未就绪，请稍后重试":
    print(f"错误: 错误状态消息不匹配")
    sys.exit(1)
print("✓ 系统状态结构体测试通过")

print("\n=== 测试控制器层级枚举 ===")
controller_level = magicdog_w.ControllerLevel.HIGH_LEVEL
print(
    f"控制器层级: {controller_level} (HIGH_LEVEL - 高层级控制器，负责路径规划和任务调度)"
)

low_level = magicdog_w.ControllerLevel.LOW_LEVEL
print(f"控制器层级: {low_level} (LOW_LEVEL - 低层级控制器，负责关节控制和稳定性)")

# 测试控制器层级枚举值
if controller_level != magicdog_w.ControllerLevel.HIGH_LEVEL:
    print(f"错误: 高层级控制器枚举值不匹配")
    sys.exit(1)
if low_level != magicdog_w.ControllerLevel.LOW_LEVEL:
    print(f"错误: 低层级控制器枚举值不匹配")
    sys.exit(1)
print("✓ 控制器层级枚举测试通过")

print("\n=== 测试摇杆控制指令 ===")
# 测试前进指令
forward_command = magicdog_w.JoystickCommand()
forward_command.left_x_axis = 0.0  # 不左右移动
forward_command.left_y_axis = 0.8  # 前进80%速度
forward_command.right_x_axis = 0.0  # 不旋转
forward_command.right_y_axis = 0.0  # 待定功能
print("前进指令:")
print(f"  左摇杆X轴: {forward_command.left_x_axis} (0.0 = 不左右移动)")
print(f"  左摇杆Y轴: {forward_command.left_y_axis} (0.8 = 前进80%速度)")
print(f"  右摇杆X轴: {forward_command.right_x_axis} (0.0 = 不旋转)")
print(f"  右摇杆Y轴: {forward_command.right_y_axis} (待定功能)")

# 测试前进指令值
if abs(forward_command.left_x_axis - 0.0) > 1e-6:
    print(f"错误: 前进指令左摇杆X轴 期望值 0.0，实际值 {forward_command.left_x_axis}")
    sys.exit(1)
if abs(forward_command.left_y_axis - 0.8) > 1e-6:
    print(f"错误: 前进指令左摇杆Y轴 期望值 0.8，实际值 {forward_command.left_y_axis}")
    sys.exit(1)
if abs(forward_command.right_x_axis - 0.0) > 1e-6:
    print(f"错误: 前进指令右摇杆X轴 期望值 0.0，实际值 {forward_command.right_x_axis}")
    sys.exit(1)
if abs(forward_command.right_y_axis - 0.0) > 1e-6:
    print(f"错误: 前进指令右摇杆Y轴 期望值 0.0，实际值 {forward_command.right_y_axis}")
    sys.exit(1)
print("✓ 前进指令测试通过")

# 测试左转指令
turn_left_command = magicdog_w.JoystickCommand()
turn_left_command.left_x_axis = -0.6  # 左转60%速度
turn_left_command.left_y_axis = 0.0  # 不前进后退
turn_left_command.right_x_axis = 0.0  # 不旋转
turn_left_command.right_y_axis = 0.0  # 待定功能
print("\n左转指令:")
print(f"  左摇杆X轴: {turn_left_command.left_x_axis} (-0.6 = 左转60%速度)")
print(f"  左摇杆Y轴: {turn_left_command.left_y_axis} (0.0 = 不前进后退)")
print(f"  右摇杆X轴: {turn_left_command.right_x_axis} (0.0 = 不旋转)")
print(f"  右摇杆Y轴: {turn_left_command.right_y_axis} (待定功能)")

# 测试左转指令值
if abs(turn_left_command.left_x_axis - -0.6) > 1e-6:
    print(
        f"错误: 左转指令左摇杆X轴 期望值 -0.6，实际值 {turn_left_command.left_x_axis}"
    )
    sys.exit(1)
if abs(turn_left_command.left_y_axis - 0.0) > 1e-6:
    print(f"错误: 左转指令左摇杆Y轴 期望值 0.0，实际值 {turn_left_command.left_y_axis}")
    sys.exit(1)
if abs(turn_left_command.right_x_axis - 0.0) > 1e-6:
    print(
        f"错误: 左转指令右摇杆X轴 期望值 0.0，实际值 {turn_left_command.right_x_axis}"
    )
    sys.exit(1)
if abs(turn_left_command.right_y_axis - 0.0) > 1e-6:
    print(
        f"错误: 左转指令右摇杆Y轴 期望值 0.0，实际值 {turn_left_command.right_y_axis}"
    )
    sys.exit(1)
print("✓ 左转指令测试通过")

# 测试旋转指令
rotate_command = magicdog_w.JoystickCommand()
rotate_command.left_x_axis = 0.0  # 不左右移动
rotate_command.left_y_axis = 0.0  # 不前进后退
rotate_command.right_x_axis = 0.7  # 右旋转70%速度
rotate_command.right_y_axis = 0.0  # 待定功能
print("\n旋转指令:")
print(f"  左摇杆X轴: {rotate_command.left_x_axis} (0.0 = 不左右移动)")
print(f"  左摇杆Y轴: {rotate_command.left_y_axis} (0.0 = 不前进后退)")
print(f"  右摇杆X轴: {rotate_command.right_x_axis} (0.7 = 右旋转70%速度)")
print(f"  右摇杆Y轴: {rotate_command.right_y_axis} (待定功能)")

# 测试旋转指令值

if abs(rotate_command.left_x_axis - 0.0) > 1e-6:
    print(f"错误: 旋转指令左摇杆X轴 期望值 0.0，实际值 {rotate_command.left_x_axis}")
    sys.exit(1)
if abs(rotate_command.left_y_axis - 0.0) > 1e-6:
    print(f"错误: 旋转指令左摇杆Y轴 期望值 0.0，实际值 {rotate_command.left_y_axis}")
    sys.exit(1)
if abs(rotate_command.right_x_axis - 0.7) > 1e-6:
    print(f"错误: 旋转指令右摇杆X轴 期望值 0.7，实际值 {rotate_command.right_x_axis}")
    sys.exit(1)
if abs(rotate_command.right_y_axis - 0.0) > 1e-6:
    print(f"错误: 旋转指令右摇杆Y轴 期望值 0.0，实际值 {rotate_command.right_y_axis}")
    sys.exit(1)
print("✓ 旋转指令测试通过")

print("\n=== 测试步态模式枚举 ===")
# 测试常用步态（根据 magic_type.h 中 GaitMode 枚举）
passive_gait = magicdog_w.GaitMode.GAIT_PASSIVE
print(f"步态模式: {passive_gait} (GAIT_PASSIVE - 失能/掉电)")

damper_gait = magicdog_w.GaitMode.GAIT_PURE_DAMPER
print(f"步态模式: {damper_gait} (GAIT_PURE_DAMPER - 阻尼模式)")

stand_gait = magicdog_w.GaitMode.GAIT_STAND_R
print(f"步态模式: {stand_gait} (GAIT_STAND_R - 站立模式/恢复站立)")

lowlevel_sdk_gait = magicdog_w.GaitMode.GAIT_LOWLEVL_SDK
print(f"步态模式: {lowlevel_sdk_gait} (GAIT_LOWLEVL_SDK - 底层SDK步态)")

rl_move_quick_gait = magicdog_w.GaitMode.GAIT_RL_MOVE_QUICK
print(f"步态模式: {rl_move_quick_gait} (GAIT_RL_MOVE_QUICK - 快速移动)")

rl_terrain_gait = magicdog_w.GaitMode.GAIT_RL_TERRAIN
print(f"步态模式: {rl_terrain_gait} (GAIT_RL_TERRAIN - 全地形模式)")

rl_climb_gait = magicdog_w.GaitMode.GAIT_RL_CLIMB
print(f"步态模式: {rl_climb_gait} (GAIT_RL_CLIMB - 爬楼梯)")

rl_hand_stand_gait = magicdog_w.GaitMode.GAIT_RL_HAND_STAND
print(f"步态模式: {rl_hand_stand_gait} (GAIT_RL_HAND_STAND - 倒立行走)")

rl_foot_stand_gait = magicdog_w.GaitMode.GAIT_RL_FOOT_STAND
print(f"步态模式: {rl_foot_stand_gait} (GAIT_RL_FOOT_STAND - 足底行走)")

none_gait = magicdog_w.GaitMode.GAIT_NONE
print(f"步态模式: {none_gait} (GAIT_NONE - 无步态)")


print("\n=== 测试特技动作枚举 ===")
# 只保留 magic_type.h 中已定义动作
action_none = magicdog_w.TrickAction.ACTION_NONE
print(f"特技动作: {action_none} (ACTION_NONE - 无特技动作)")

action_lie_down = magicdog_w.TrickAction.ACTION_LIE_DOWN
print(f"特技动作: {action_lie_down} (ACTION_LIE_DOWN - 趴下，实用动作)")

print("\n=== 测试动作组合场景 ===")
print("场景1: 基本测试")
print(f"  1. {magicdog_w.TrickAction.ACTION_NONE} (无特技动作)")
print(f"  2. {magicdog_w.TrickAction.ACTION_LIE_DOWN} (趴下)")

print("\n=== 测试完成 ===")
print("已成功测试以下结构体和枚举:")
print("  - Status: 系统状态信息")
print("  - ControllerLevel: 控制器层级")
print("  - JoystickCommand: 摇杆控制指令")
print("  - GaitMode: 步态模式")
print("  - TrickAction: 特技动作")
print("\n所有测试数据都使用了有意义的实际场景值，便于理解各字段的用途。")
