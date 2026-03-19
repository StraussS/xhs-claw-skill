# 评论、回复、点赞、收藏

## 什么时候读这个文件

当任务涉及：
- 发表评论
- 回复评论
- 点赞或取消点赞
- 收藏或取消收藏

## 执行前检查

1. 已登录
2. 已拿到 `feed_id` 和 `xsec_token`
3. 对评论/回复内容完成确认

## 评论

```bash
python scripts/cli.py post-comment \
  --feed-id FEED_ID \
  --xsec-token XSEC_TOKEN \
  --content "评论内容"
```

## 回复评论

通过评论 ID：

```bash
python scripts/cli.py reply-comment \
  --feed-id FEED_ID \
  --xsec-token XSEC_TOKEN \
  --content "回复内容" \
  --comment-id COMMENT_ID
```

通过用户 ID：

```bash
python scripts/cli.py reply-comment \
  --feed-id FEED_ID \
  --xsec-token XSEC_TOKEN \
  --content "回复内容" \
  --user-id USER_ID
```

## 点赞 / 取消点赞

```bash
python scripts/cli.py like-feed --feed-id FEED_ID --xsec-token XSEC_TOKEN
python scripts/cli.py like-feed --feed-id FEED_ID --xsec-token XSEC_TOKEN --unlike
```

## 收藏 / 取消收藏

```bash
python scripts/cli.py favorite-feed --feed-id FEED_ID --xsec-token XSEC_TOKEN
python scripts/cli.py favorite-feed --feed-id FEED_ID --xsec-token XSEC_TOKEN --unfavorite
```

## 互动建议

- 评论先确认文本，不要直接发送草稿
- 回复前先确认回复对象，避免回错人
- 点赞和收藏可以作为低风险动作优先执行
- 批量互动要控制频率，避免连续高频操作

## 失败处理

- `评论失败`：检查是否有敏感词或页面结构变化
- `参数缺失`：先回到搜索或详情流程
- `互动频率过高`：暂停并降低节奏
