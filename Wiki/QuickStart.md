# 快速开始（本地 / Docker）

先决条件
- Python 3.10+（与项目中 requirements.txt 的版本匹配）
- MongoDB 实例（可本地或远程）
- Navidrome 服务（用于创建/管理用户）
- Telegram Bot Token（通过 @BotFather 获取）

方式 A：Docker（推荐）
- 示例 docker-compose.yml（示意）：
```yaml
version: '3.8'
services:
  navidromebot:
    image: python:3.10-slim
    container_name: navidromebot
    volumes:
      - ./Navidrome:/app/Navidrome
      - ./config:/app/config
    working_dir: /app
    command: python Navidrome/telegram_bot.py
    environment:
      - TELEGRAM_BOT_TOKEN=<your_token>
      - MONGO_URI=<mongo_uri>
      - NAVIDROME_BASE_URL=<navidrome_api_url>
      - NAVIDROME_API_KEY=<navidrome_key>
    restart: unless-stopped
```
把上述变量改成真实值并运行：
```
docker-compose up -d
```

方式 B：本地虚拟环境
```
git clone https://github.com/weitie79-wq/NavidromeBot.git
cd NavidromeBot
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# 设置环境变量或编辑 config.py
python Navidrome/telegram_bot.py
```

启动后在日志里查看 Bot 是否正常连接并开始轮询。
