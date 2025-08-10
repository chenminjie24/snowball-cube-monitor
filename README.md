# 雪球组合监控通知

这是一个用于监控雪球组合调仓变化并通过PushDeer发送通知的工具。

## 功能特点

- 🔄 **持续监控**: 程序启动后持续运行，每分钟检查一次调仓变化
- ⏰ **智能时间控制**: 只在交易时间段（9:30-16:00）进行监控，其他时间休眠
- 📱 **即时通知**: 发现新调仓时立即通过PushDeer发送详细通知
- 🚀 **首次推送**: 首次监控组合时会推送最近一次调仓信息
- 📊 **详细信息**: 通知包含组合名称、股票代码、仓位变化等详细信息
- ⚙️ **灵活配置**: 支持监控多个组合，通过配置文件管理

## 安装依赖

```bash
pip install -r requirements.txt
```

## 配置

1. 编辑 `config.json` 文件：

```json
{
  "snowball": {
    "token": "你的雪球token"
  },
  "pushdeer": {
    "pushkey": "你的PushDeer推送key",
    "server": "https://api2.pushdeer.com"
  },
  "monitor": {
    "check_interval": 60,
    "active_hours": {
      "start": "09:30",
      "end": "16:00",
      "timezone": "Asia/Shanghai"
    },
    "sleep_interval_inactive": 300,
    "cubes": [
      {
        "id": "ZH3126091",
        "name": "你的组合名称"
      }
    ]
  }
}
```

2. 配置说明：
   - `snowball.token`: 雪球API token, [获取 Token 方法](https://blog.crackcreed.com/diy-xue-qiu-app-shu-ju-api/)
   - `pushdeer.pushkey`: PushDeer推送key, [PushDeer文档](https://www.pushdeer.com/)
   - `monitor.cubes`: 要监控的组合列表，可以添加多个

## 运行

```bash
python monitor.py
```

程序启动后会：
- 显示监控配置信息
- 首次监控组合时推送最近一次调仓信息
- 在活跃时间段内每分钟检查一次调仓变化
- 发现新调仓时发送通知
- 非活跃时间段内休眠等待

## 停止

按 `Ctrl+C` 优雅停止程序。

## 通知内容示例

```
📈 组合调仓通知

组合：示例组合1 (ZH3334492)
调仓时间：2025-01-08 14:30

📊 仓位变化：
• 新增持仓：
  - 浪潮数字企业 (00596): 0% → 4%

• 减仓/清仓：
  - 中国龙工 (03339): 3% → 0% (清仓)

• 调整仓位：
  - 重庆机电 (02722): 37.54% → 35% (↓2.54%)

💰 现金比例：61%
```

## 文件说明

- `monitor.py`: 主监控脚本
- `config.json`: 配置文件
- `storage.py`: 数据存储模块
- `notifier.py`: 通知模块
- `data/last_rebalancing.json`: 存储最新调仓记录ID
- `requirements.txt`: Python依赖包列表
