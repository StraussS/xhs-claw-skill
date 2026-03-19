# 搜索、详情与字段说明

## 什么时候读这个文件

当任务涉及：
- 搜索小红书内容
- 查看首页推荐
- 查看笔记详情
- 查看用户主页
- 为评论/点赞/收藏准备参数

## 首页推荐

```bash
python scripts/cli.py list-feeds
```

通常返回：
- `feeds`
- `count`

每条 feed 常见包含：
- `id`
- `xsec_token`
- 标题、封面、作者、互动信息等字段

## 搜索

```bash
python scripts/cli.py search-feeds --keyword "露营"
```

可选筛选：

```bash
python scripts/cli.py search-feeds \
  --keyword "露营" \
  --sort-by 最多点赞 \
  --note-type 图文 \
  --publish-time 一周内
```

常用筛选项：
- `--sort-by`：综合、最新、最多点赞、最多评论、最多收藏
- `--note-type`：不限、视频、图文
- `--publish-time`：不限、一天内、一周内、半年内
- `--search-scope`：不限、已看过、未看过、已关注
- `--location`：不限、同城、附近

## 详情

获取详情前，先从搜索结果或首页 feed 中取：
- `feed_id`
- `xsec_token`

```bash
python scripts/cli.py get-feed-detail --feed-id FEED_ID --xsec-token XSEC_TOKEN
```

如需更多评论：

```bash
python scripts/cli.py get-feed-detail \
  --feed-id FEED_ID \
  --xsec-token XSEC_TOKEN \
  --load-all-comments \
  --click-more-replies
```

## 用户主页

```bash
python scripts/cli.py user-profile --user-id USER_ID --xsec-token XSEC_TOKEN
```

## 参数来源规则

- 点赞、收藏、评论、回复等写操作都依赖 `feed_id + xsec_token`
- `comment_id` 或 `user_id` 往往来自详情评论区
- 如果参数不确定，先做搜索或详情，不要硬猜

## 结果呈现建议

对用户汇报时优先展示：
- 标题
- 作者
- 点赞/评论/收藏等关键指标
- 适合下一步操作的 ID 信息

如果用户是做分析，优先整理成要点或表格。
