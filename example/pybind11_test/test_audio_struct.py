#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MagicDog_W SDK Python 使用示例

这个文件展示了如何使用 MagicDog_W SDK 的 Python 绑定来控制机器人。
"""

import sys
import time
import magicdog_w_python as magicdog_w
from magicdog_w_python import TtsCommand, TtsPriority, TtsMode, GetSpeechConfig

print("=== 测试 TTS 优先级枚举 ===")
tts_priority = magicdog_w.TtsPriority.HIGH
print(f"TTS优先级: {tts_priority} (HIGH - 最高优先级，用于紧急提醒)")

tts_mode = magicdog_w.TtsMode.ADD
print(f"TTS模式: {tts_mode} (ADD - 追加到队列尾部，不打断当前播放)")

# 测试枚举值
if tts_priority != magicdog_w.TtsPriority.HIGH:
    print(
        f"错误: TTS优先级 期望值 {magicdog_w.TtsPriority.HIGH}，实际值 {tts_priority}"
    )
    sys.exit(1)
if tts_mode != magicdog_w.TtsMode.ADD:
    print(f"错误: TTS模式 期望值 {magicdog_w.TtsMode.ADD}，实际值 {tts_mode}")
    sys.exit(1)
print("✓ TTS枚举测试通过")

print("\n=== 测试 TTS 命令结构体 ===")
tts_cmd = magicdog_w.TtsCommand()
tts_cmd.id = "weather_alert_001"
tts_cmd.content = "今日天气晴朗，温度25度，适合户外活动"
tts_cmd.priority = tts_priority
tts_cmd.mode = tts_mode
print(
    f"TTS命令: ID={tts_cmd.id}, 内容='{tts_cmd.content}', 优先级={tts_cmd.priority}, 模式={tts_cmd.mode}"
)

# 测试TTS命令值
if tts_cmd.id != "weather_alert_001":
    print(f"错误: TTS命令ID 期望值 'weather_alert_001'，实际值 '{tts_cmd.id}'")
    sys.exit(1)
if tts_cmd.content != "今日天气晴朗，温度25度，适合户外活动":
    print(f"错误: TTS命令内容不匹配")
    sys.exit(1)
if tts_cmd.priority != tts_priority:
    print(f"错误: TTS命令优先级不匹配")
    sys.exit(1)
if tts_cmd.mode != tts_mode:
    print(f"错误: TTS命令模式不匹配")
    sys.exit(1)
print("✓ TTS命令结构体测试通过")

print("\n=== 测试自定义机器人信息 ===")
custom_bot_info = magicdog_w.CustomBotInfo()
custom_bot_info.name = "智能客服助手"
custom_bot_info.workflow = "customer_service_workflow_v2.1"
custom_bot_info.token = "cs_token_2024_001"
print(
    f"自定义机器人: 名称='{custom_bot_info.name}', 工作流='{custom_bot_info.workflow}', 令牌='{custom_bot_info.token}'"
)

# 测试自定义机器人信息值
if custom_bot_info.name != "智能客服助手":
    print(f"错误: 机器人名称 期望值 '智能客服助手'，实际值 '{custom_bot_info.name}'")
    sys.exit(1)
if custom_bot_info.workflow != "customer_service_workflow_v2.1":
    print(
        f"错误: 工作流 期望值 'customer_service_workflow_v2.1'，实际值 '{custom_bot_info.workflow}'"
    )
    sys.exit(1)
if custom_bot_info.token != "cs_token_2024_001":
    print(f"错误: 令牌 期望值 'cs_token_2024_001'，实际值 '{custom_bot_info.token}'")
    sys.exit(1)
print("✓ 自定义机器人信息测试通过")

custom_bot_map = magicdog_w.StringCustomBotMap()
custom_bot_map["cs_bot_001"] = custom_bot_info
for key, value in custom_bot_map.items():
    print(f"机器人映射: {key} -> {value.name}")

# 测试机器人映射
if "cs_bot_001" not in custom_bot_map:
    print(f"错误: 机器人映射中缺少 'cs_bot_001'")
    sys.exit(1)
if custom_bot_map["cs_bot_001"].name != "智能客服助手":
    print(f"错误: 映射的机器人名称不匹配")
    sys.exit(1)
print("✓ 机器人映射测试通过")

print("\n=== 测试语音设置配置 ===")
set_speech_config = magicdog_w.SetSpeechConfig()
set_speech_config.speaker_id = "xiaoyun_female"
set_speech_config.region = "zh-CN"
set_speech_config.bot_id = "main_assistant"
set_speech_config.is_front_doa = True
set_speech_config.is_fullduplex_enable = True
set_speech_config.is_enable = True
set_speech_config.is_doa_enable = True
set_speech_config.speaker_speed = 1.2
set_speech_config.wakeup_name = "小云"
set_speech_config.custom_bot = custom_bot_map
print(
    f"语音设置: 音色ID='{set_speech_config.speaker_id}', 地区='{set_speech_config.region}', 机器人ID='{set_speech_config.bot_id}'"
)
print(
    f"语音设置: 语速={set_speech_config.speaker_speed}, 唤醒词='{set_speech_config.wakeup_name}'"
)

print("\n=== 测试音色配置选择 ===")
speaker_config_selected = magicdog_w.SpeakerConfigSelected()
speaker_config_selected.region = "zh-CN"
speaker_config_selected.speaker_id = "xiaoyun_female"
print(
    f"选中的音色配置: 地区='{speaker_config_selected.region}', 音色ID='{speaker_config_selected.speaker_id}'"
)

print("\n=== 测试音色配置数据结构 ===")
speaker_config_data = magicdog_w.String2DStringVectorMap()

# 创建中文音色数据
array1 = ["xiaoyun_female", "小云女声"]

array2 = ["xiaogang_male", "小刚男声"]

array3 = ["xiaomei_female", "小美女声"]

# 创建向量并添加音色数组
vector_data = [array1, array2, array3]

# 设置中文地区音色数据
speaker_config_data["zh-CN"] = vector_data

# 创建英文音色数据
array_en1 = ["john_male", "John Male Voice"]
array_en2 = ["sarah_female", "Sarah Female Voice"]

vector_en_data = [array_en1, array_en2]


# 设置英文地区音色数据
speaker_config_data["en-US"] = vector_en_data

print("音色配置数据:")
for region, speakers in speaker_config_data.items():
    print(f"  地区: {region}")
    for speaker in speakers:
        print(f"    音色ID: {speaker[0]}, 音色名称: {speaker[1]}")

# 测试音色配置数据结构
for region, speakers in speaker_config_data.items():
    if region == "en-US":
        if (
            speakers[0][0] != "john_male"
            or speakers[0][1] != "John Male Voice"
            or speakers[1][0] != "sarah_female"
            or speakers[1][1] != "Sarah Female Voice"
        ):
            print(f"错误: 英文地区音色数据不匹配")
            sys.exit(1)
    if region == "zh-CN":
        if (
            speakers[0][0] != "xiaoyun_female"
            or speakers[0][1] != "小云女声"
            or speakers[1][0] != "xiaogang_male"
            or speakers[1][1] != "小刚男声"
            or speakers[2][0] != "xiaomei_female"
            or speakers[2][1] != "小美女声"
        ):
            print(f"错误: 中文地区音色数据不匹配")
            sys.exit(1)

speaker_config = magicdog_w.SpeakerConfig()
speaker_config.data = speaker_config_data
speaker_config.selected = speaker_config_selected
speaker_config.speaker_speed = 1.2
print(f"音色配置: 语速={speaker_config.speaker_speed}")

# 测试音色配置数据结构
for region, speakers in speaker_config_data.items():
    if region == "en-US":
        if (
            speakers[0][0] != "john_male"
            or speakers[0][1] != "John Male Voice"
            or speakers[1][0] != "sarah_female"
            or speakers[1][1] != "Sarah Female Voice"
        ):
            print(f"错误: 英文地区音色数据不匹配")
            sys.exit(1)
    if region == "zh-CN":
        if (
            speakers[0][0] != "xiaoyun_female"
            or speakers[0][1] != "小云女声"
            or speakers[1][0] != "xiaogang_male"
            or speakers[1][1] != "小刚男声"
            or speakers[2][0] != "xiaomei_female"
            or speakers[2][1] != "小美女声"
        ):
            print(f"错误: 中文地区音色数据不匹配")
            sys.exit(1)

if speaker_config.selected.region != "zh-CN":
    print(f"错误: 选中的地区不匹配")
    sys.exit(1)
if speaker_config.selected.speaker_id != "xiaoyun_female":
    print(f"错误: 选中的音色ID不匹配")
    sys.exit(1)

if speaker_config.speaker_speed != 1.2:
    print(f"错误: 语速不匹配")
    sys.exit(1)

print("\n=== 测试机器人配置 ===")
bot_info = magicdog_w.BotInfo()
bot_info.name = "智能家居控制"
bot_info.workflow = "smart_home_control_v1.0"

bot_config_selected = magicdog_w.BotConfigSelected()
bot_config_selected.bot_id = "home_bot_001"

bot_config_data = magicdog_w.StringBotInfoMap()
bot_config_data["home_bot_001"] = bot_info

# 创建另一个机器人
bot_info2 = magicdog_w.BotInfo()
bot_info2.name = "天气查询助手"
bot_info2.workflow = "weather_query_v2.1"
bot_config_data["weather_bot_002"] = bot_info2

print("标准机器人配置:")
for bot_id, info in bot_config_data.items():
    print(f"  机器人ID: {bot_id}, 名称: {info.name}, 工作流: {info.workflow}")

custom_bot_info = magicdog_w.CustomBotInfo()
custom_bot_info.name = "智能客服助手"
custom_bot_info.workflow = "customer_service_workflow_v2.1"
custom_bot_info.token = "cs_token_2024_001"

custom_bot_map = magicdog_w.StringCustomBotMap()
custom_bot_map["cs_bot_001"] = custom_bot_info

bot_config = magicdog_w.BotConfig()
bot_config.data = bot_config_data
bot_config.custom_data = custom_bot_map
bot_config.selected = bot_config_selected
print(f"机器人配置: 选中的机器人ID='{bot_config.selected.bot_id}'")

print("\n=== 测试唤醒配置 ===")
wakeup_config_data = magicdog_w.StringStringMap()
wakeup_config_data["小云"] = "xiao yun"
wakeup_config_data["小刚"] = "xiao gang"
wakeup_config_data["小美"] = "xiao mei"
wakeup_config_data["Hello"] = "he llo"

wakeup_config = magicdog_w.WakeupConfig()
wakeup_config.name = "小云"
wakeup_config.data = wakeup_config_data

print("唤醒配置:")
print(f"  唤醒名称: {wakeup_config.name}")
for wakeup_word, pinyin in wakeup_config.data.items():
    print(f"  唤醒词: '{wakeup_word}' -> 拼音: '{pinyin}'")

print("\n=== 测试对话配置 ===")
dialog_config = magicdog_w.DialogConfig()
dialog_config.is_front_doa = True
dialog_config.is_fullduplex_enable = True
dialog_config.is_enable = True
dialog_config.is_doa_enable = True

print("对话配置:")
print(f"  强制正前方拾音: {dialog_config.is_front_doa}")
print(f"  全双工对话: {dialog_config.is_fullduplex_enable}")
print(f"  语音开关: {dialog_config.is_enable}")
print(f"  唤醒方位转头: {dialog_config.is_doa_enable}")

print("\n=== 测试完整语音配置 ===")
get_speech_config = magicdog_w.GetSpeechConfig()
get_speech_config.speaker_config = speaker_config
get_speech_config.bot_config = bot_config
get_speech_config.wakeup_config = wakeup_config
get_speech_config.dialog_config = dialog_config

print("完整语音配置已创建，包含:")
print(f"  - 音色配置: {len(speaker_config.data)} 个地区")
print(
    f"  - 机器人配置: {len(bot_config.data)} 个标准机器人 + {len(bot_config.custom_data)} 个自定义机器人"
)
print(f"  - 唤醒配置: {len(wakeup_config.data)} 个唤醒词")
print(f"  - 对话配置: 语音{'启用' if dialog_config.is_enable else '禁用'}")

print("\n=== 测试设置值读取和验证 ===")

# 验证音色配置设置值
print("验证音色配置:")
print(
    f"  设置值 - 地区: '{speaker_config.selected.region}', 音色ID: '{speaker_config.selected.speaker_id}', 语速: {speaker_config.speaker_speed}"
)
print(
    f"  读取值 - 地区: '{speaker_config.selected.region}', 音色ID: '{speaker_config.selected.speaker_id}', 语速: {speaker_config.speaker_speed}"
)

# 验证音色配置数据
print("验证音色配置数据:")
for region, speakers in speaker_config.data.items():
    print(f"  地区 '{region}' 包含 {len(speakers)} 个音色:")
    for i, speaker in enumerate(speakers):
        print(f"    [{i}] 音色ID: '{speaker[0]}', 名称: '{speaker[1]}'")

# 验证机器人配置设置值
print("验证机器人配置:")
print(f"  设置值 - 选中机器人ID: '{bot_config.selected.bot_id}'")
print(f"  读取值 - 选中机器人ID: '{bot_config.selected.bot_id}'")

# 验证标准机器人数据
print("验证标准机器人数据:")
for bot_id, info in bot_config.data.items():
    print(f"  机器人ID: '{bot_id}' -> 名称: '{info.name}', 工作流: '{info.workflow}'")

# 验证自定义机器人数据
print("验证自定义机器人数据:")
for bot_id, info in bot_config.custom_data.items():
    print(
        f"  自定义机器人ID: '{bot_id}' -> 名称: '{info.name}', 工作流: '{info.workflow}', 令牌: '{info.token}'"
    )

# 验证唤醒配置设置值
print("验证唤醒配置:")
print(f"  设置值 - 唤醒名称: '{wakeup_config.name}'")
print(f"  读取值 - 唤醒名称: '{wakeup_config.name}'")

# 验证唤醒词数据
print("验证唤醒词数据:")
for wakeup_word, pinyin in wakeup_config.data.items():
    print(f"  唤醒词: '{wakeup_word}' -> 拼音: '{pinyin}'")

# 验证对话配置设置值
print("验证对话配置:")
print(
    f"  设置值 - 强制正前方拾音: {dialog_config.is_front_doa}, 全双工对话: {dialog_config.is_fullduplex_enable}"
)
print(
    f"  设置值 - 语音开关: {dialog_config.is_enable}, 唤醒方位转头: {dialog_config.is_doa_enable}"
)
print(
    f"  读取值 - 强制正前方拾音: {dialog_config.is_front_doa}, 全双工对话: {dialog_config.is_fullduplex_enable}"
)
print(
    f"  读取值 - 语音开关: {dialog_config.is_enable}, 唤醒方位转头: {dialog_config.is_doa_enable}"
)

# 验证语音设置配置
print("验证语音设置配置:")
print(
    f"  设置值 - 音色ID: '{set_speech_config.speaker_id}', 地区: '{set_speech_config.region}'"
)
print(
    f"  设置值 - 机器人ID: '{set_speech_config.bot_id}', 语速: {set_speech_config.speaker_speed}"
)
print(f"  设置值 - 唤醒名称: '{set_speech_config.wakeup_name}'")
print(
    f"  读取值 - 音色ID: '{set_speech_config.speaker_id}', 地区: '{set_speech_config.region}'"
)
print(
    f"  读取值 - 机器人ID: '{set_speech_config.bot_id}', 语速: {set_speech_config.speaker_speed}"
)
print(f"  读取值 - 唤醒名称: '{set_speech_config.wakeup_name}'")

# 验证TTS命令设置值
print("验证TTS命令:")
print(f"  设置值 - ID: '{tts_cmd.id}', 内容: '{tts_cmd.content}'")
print(f"  设置值 - 优先级: {tts_cmd.priority}, 模式: {tts_cmd.mode}")
print(f"  读取值 - ID: '{tts_cmd.id}', 内容: '{tts_cmd.content}'")
print(f"  读取值 - 优先级: {tts_cmd.priority}, 模式: {tts_cmd.mode}")

# 验证自定义机器人信息设置值
print("验证自定义机器人信息:")
print(
    f"  设置值 - 名称: '{custom_bot_info.name}', 工作流: '{custom_bot_info.workflow}', 令牌: '{custom_bot_info.token}'"
)
print(
    f"  读取值 - 名称: '{custom_bot_info.name}', 工作流: '{custom_bot_info.workflow}', 令牌: '{custom_bot_info.token}'"
)

# 执行一致性检查
print("\n=== 执行一致性检查 ===")
all_checks_passed = True

# 检查音色配置一致性
if speaker_config.selected.region != "zh-CN":
    print(
        f"❌ 音色配置地区不一致: 期望 'zh-CN', 实际 '{speaker_config.selected.region}'"
    )
    all_checks_passed = False
else:
    print("✅ 音色配置地区一致")

if speaker_config.selected.speaker_id != "xiaoyun_female":
    print(
        f"❌ 音色配置ID不一致: 期望 'xiaoyun_female', 实际 '{speaker_config.selected.speaker_id}'"
    )
    all_checks_passed = False
else:
    print("✅ 音色配置ID一致")

if speaker_config.speaker_speed != 1.2:
    print(f"❌ 音色配置语速不一致: 期望 1.2, 实际 {speaker_config.speaker_speed}")
    all_checks_passed = False
else:
    print("✅ 音色配置语速一致")

# 检查机器人配置一致性
if bot_config.selected.bot_id != "home_bot_001":
    print(
        f"❌ 机器人配置选中ID不一致: 期望 'home_bot_001', 实际 '{bot_config.selected.bot_id}'"
    )
    all_checks_passed = False
else:
    print("✅ 机器人配置选中ID一致")

# 检查唤醒配置一致性
if wakeup_config.name != "小云":
    print(f"❌ 唤醒配置名称不一致: 期望 '小云', 实际 '{wakeup_config.name}'")
    all_checks_passed = False
else:
    print("✅ 唤醒配置名称一致")

# 检查对话配置一致性
if not dialog_config.is_front_doa:
    print(
        f"❌ 对话配置强制正前方拾音不一致: 期望 True, 实际 {dialog_config.is_front_doa}"
    )
    all_checks_passed = False
else:
    print("✅ 对话配置强制正前方拾音一致")

if not dialog_config.is_fullduplex_enable:
    print(
        f"❌ 对话配置全双工对话不一致: 期望 True, 实际 {dialog_config.is_fullduplex_enable}"
    )
    all_checks_passed = False
else:
    print("✅ 对话配置全双工对话一致")

if not dialog_config.is_enable:
    print(f"❌ 对话配置语音开关不一致: 期望 True, 实际 {dialog_config.is_enable}")
    all_checks_passed = False
else:
    print("✅ 对话配置语音开关一致")

if not dialog_config.is_doa_enable:
    print(
        f"❌ 对话配置唤醒方位转头不一致: 期望 True, 实际 {dialog_config.is_doa_enable}"
    )
    all_checks_passed = False
else:
    print("✅ 对话配置唤醒方位转头一致")

# 检查语音设置配置一致性
if set_speech_config.speaker_id != "xiaoyun_female":
    print(
        f"❌ 语音设置音色ID不一致: 期望 'xiaoyun_female', 实际 '{set_speech_config.speaker_id}'"
    )
    all_checks_passed = False
else:
    print("✅ 语音设置音色ID一致")

if set_speech_config.region != "zh-CN":
    print(f"❌ 语音设置地区不一致: 期望 'zh-CN', 实际 '{set_speech_config.region}'")
    all_checks_passed = False
else:
    print("✅ 语音设置地区一致")

if set_speech_config.bot_id != "main_assistant":
    print(
        f"❌ 语音设置机器人ID不一致: 期望 'main_assistant', 实际 '{set_speech_config.bot_id}'"
    )
    all_checks_passed = False
else:
    print("✅ 语音设置机器人ID一致")

if set_speech_config.speaker_speed != 1.2:
    print(f"❌ 语音设置语速不一致: 期望 1.2, 实际 {set_speech_config.speaker_speed}")
    all_checks_passed = False
else:
    print("✅ 语音设置语速一致")

if set_speech_config.wakeup_name != "小云":
    print(
        f"❌ 语音设置唤醒名称不一致: 期望 '小云', 实际 '{set_speech_config.wakeup_name}'"
    )
    all_checks_passed = False
else:
    print("✅ 语音设置唤醒名称一致")

# 检查TTS命令一致性
if tts_cmd.id != "weather_alert_001":
    print(f"❌ TTS命令ID不一致: 期望 'weather_alert_001', 实际 '{tts_cmd.id}'")
    all_checks_passed = False
else:
    print("✅ TTS命令ID一致")

if tts_cmd.content != "今日天气晴朗，温度25度，适合户外活动":
    print(f"❌ TTS命令内容不一致")
    all_checks_passed = False
else:
    print("✅ TTS命令内容一致")

if tts_cmd.priority != magicdog_w.TtsPriority.HIGH:
    print(
        f"❌ TTS命令优先级不一致: 期望 {magicdog_w.TtsPriority.HIGH}, 实际 {tts_cmd.priority}"
    )
    all_checks_passed = False
else:
    print("✅ TTS命令优先级一致")

if tts_cmd.mode != magicdog_w.TtsMode.ADD:
    print(f"❌ TTS命令模式不一致: 期望 {magicdog_w.TtsMode.ADD}, 实际 {tts_cmd.mode}")
    all_checks_passed = False
else:
    print("✅ TTS命令模式一致")

# 检查自定义机器人信息一致性
if custom_bot_info.name != "智能客服助手":
    print(
        f"❌ 自定义机器人名称不一致: 期望 '智能客服助手', 实际 '{custom_bot_info.name}'"
    )
    all_checks_passed = False
else:
    print("✅ 自定义机器人名称一致")

if custom_bot_info.workflow != "customer_service_workflow_v2.1":
    print(
        f"❌ 自定义机器人工作流不一致: 期望 'customer_service_workflow_v2.1', 实际 '{custom_bot_info.workflow}'"
    )
    all_checks_passed = False
else:
    print("✅ 自定义机器人工作流一致")

if custom_bot_info.token != "cs_token_2024_001":
    print(
        f"❌ 自定义机器人令牌不一致: 期望 'cs_token_2024_001', 实际 '{custom_bot_info.token}'"
    )
    all_checks_passed = False
else:
    print("✅ 自定义机器人令牌一致")

# 输出最终结果
print(f"\n=== 一致性检查结果 ===")
if all_checks_passed:
    print("🎉 所有设置值与读取值完全一致！测试通过！")
else:
    print("❌ 发现不一致的值，测试失败！")
    sys.exit(1)

print("\n=== 测试完成 ===")
