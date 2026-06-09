# NavidromeBot（基于 Telegram 的 Navidrome 管理机器人）

概述  
NavidromeBot 通过 Telegram 提供对 Navidrome 用户的管理功能（创建账号、使用注册码、查看用户信息、线路信息、签到、广播等）。此仓库为原项目的复刻与改进版本，已包含对 ConversationHandler 状态处理、未匹配回调调试等的修复。

主要功能
- 私聊菜单：用户信息、线路信息、创建账号、用注册码、签到
- 管理功能（管理员专用）：创建/删除兑换码、广播、备份/还原数据库、查看/管理用户白名单与列表
- 支持图片/多媒体广播
- 定时任务：备份数据库、删除长时间不活跃用户等
- 调试工具：记录未处理的 CallbackQuery 以便定位问题

目录结构（重要文件/目录）
- Navidrome/telegram_bot.py — Bot 启动与 Handler 注册
- Navidrome/handlers/ — 各类处理器（start, button, broadcast, message, …）
- Navidrome/jobs/ — 定时任务
- Navidrome/services/ — 与 Navidrome API 的交互
- config.py — 配置项与常量
- database.py — 数据库连接（Mongo）
- README / Wiki — 使用与部署说明
