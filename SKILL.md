---
name: xhs-claw-skill
description: 小红书自动化标准技能，基于本项目自带的 Python CLI 与 Chrome CDP 脚本完成登录、发布、搜索、详情查看、评论、点赞、收藏和多步骤运营分析。当用户要求操作小红书、发布笔记、搜索内容、查看博主、评论互动、切换账号或做小红书运营分析时使用。
---

# 小红书自动化（OpenClaw 适配版）

使用本项目自带的 `python scripts/cli.py` 和辅助脚本完成操作。优先把技能当作 **OpenClaw 本地自动化项目** 使用。

## 快速判断

按用户意图选择流程：

- **登录 / 检查登录 / 切换账号** → 参考 `references/auth-flows.md`
- **发布图文 / 视频 / 长文** → 参考 `references/publish-rules.md`
- **搜索笔记 / 首页推荐 / 笔记详情 / 用户主页** → 参考 `references/explore-fields.md`
- **评论 / 回复 / 点赞 / 收藏** → 参考 `references/interaction-rules.md`
- **竞品分析 / 热点追踪 / 研究后创作发布 / 批量互动策略** → 参考 `references/ops-playbooks.md`
- **准备长期稳定运行、做生产化检查或排查发布前风险** → 参考 `references/production-hardening.md`
- **查看当前项目已知风险与维护要点** → 参考 `references/risk-checklist.md`

## 默认工作方式

1. 先确认本地环境可用：必要时运行 `python scripts/doctor.py`
2. 涉及账号时，先运行 `python scripts/cli.py list-accounts`
3. 涉及发布、评论、回复时，先向用户展示最终内容并确认
4. 默认优先使用 **分步发布**：`fill-publish` / `fill-publish-video` → 用户确认 → `click-publish`
5. 如果用户取消发布，优先 `save-draft`，不要直接丢弃已填写内容

## 核心约束

- 依赖本地 Chrome 与 Python 3.11+
- 媒体文件优先使用绝对路径；图片 URL 也可直接交给 CLI 处理
- `feed_id` 和 `xsec_token` 应成对使用，通常从搜索结果、首页 feed 或详情结果中获得
- 评论、回复、发布属于高风险写操作，执行前必须确认
- 如果未登录、Chrome 未启动、页面结构变化或平台限流，先向用户说明，再给出下一步建议

## 常用命令

```bash
# 环境自检
python scripts/doctor.py

# 启动 Chrome
python scripts/chrome_launcher.py

# 检查登录
python scripts/cli.py check-login

# 搜索笔记
python scripts/cli.py search-feeds --keyword "关键词"

# 查看详情
python scripts/cli.py get-feed-detail --feed-id FEED_ID --xsec-token XSEC_TOKEN

# 分步填写图文
python scripts/cli.py fill-publish \
  --title-file /tmp/xhs_title.txt \
  --content-file /tmp/xhs_content.txt \
  --images "/abs/path/pic1.jpg"

# 确认发布
python scripts/cli.py click-publish
```

## 失败时怎么做

- **环境问题**：先跑 `python scripts/doctor.py`
- **未登录**：按 `references/auth-flows.md` 处理
- **参数不确定**：先搜索 / 详情，不要盲目执行互动命令
- **要做复合任务**：按 `references/ops-playbooks.md` 拆成搜索 → 筛选 → 查看详情 → 互动 / 创作 / 发布
