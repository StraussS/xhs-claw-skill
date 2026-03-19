# 发布规则与流程

## 什么时候读这个文件

当任务涉及：
- 图文发布
- 视频发布
- 长文发布
- 定时发布
- 草稿保存
- 从 URL 提取内容后发小红书

## 发布前必须确认

以下写操作必须先确认：
- 标题
- 正文
- 图片或视频
- 标签、定时、可见性等附加参数

## 默认发布策略

优先用分步发布：

1. 填表
2. 让用户确认浏览器中的预览
3. 用户确认后点击发布
4. 用户取消时保存草稿

## 标题与正文

- 标题要尽量简洁，适配小红书风格
- 标题过长时，优先重写而不是机械截断
- 正文保持自然、口语化、分段清晰
- 标签通常放到正文末尾

## 图片与视频

- 图片优先绝对路径
- 图片 URL 也可直接传给 CLI，由脚本处理
- 视频必须使用本地绝对路径
- 不要把图文和视频混在同一次发布里

## 图文分步发布

```bash
python scripts/cli.py fill-publish \
  --title-file /tmp/xhs_title.txt \
  --content-file /tmp/xhs_content.txt \
  --images "/abs/path/pic1.jpg" "/abs/path/pic2.jpg" \
  --tags "标签1" "标签2"
```

确认后：

```bash
python scripts/cli.py click-publish
```

取消时：

```bash
python scripts/cli.py save-draft
```

## 视频分步发布

```bash
python scripts/cli.py fill-publish-video \
  --title-file /tmp/xhs_title.txt \
  --content-file /tmp/xhs_content.txt \
  --video "/abs/path/video.mp4"
```

确认后：

```bash
python scripts/cli.py click-publish
```

取消时：

```bash
python scripts/cli.py save-draft
```

## 一步发布

只有在用户明确希望直接发时，再用：

```bash
python scripts/cli.py publish --title-file /tmp/xhs_title.txt --content-file /tmp/xhs_content.txt --images "/abs/path/pic1.jpg"
python scripts/cli.py publish-video --title-file /tmp/xhs_title.txt --content-file /tmp/xhs_content.txt --video "/abs/path/video.mp4"
```

## 长文发布

```bash
python scripts/cli.py long-article --title-file /tmp/xhs_title.txt --content-file /tmp/xhs_content.txt
python scripts/cli.py select-template --name "模板名"
python scripts/cli.py next-step --content-file /tmp/xhs_description.txt
python scripts/cli.py click-publish
```

## URL 提取模式

如果用户只给网页 URL：
- 先提取网页正文和主图
- 再整理成适合小红书的标题和正文草稿
- 图片为空时，明确告诉用户需要补图
- 最后仍然按分步发布执行

## 失败处理

- `没有有效图片`：检查路径或 URL
- `未登录`：先走认证流程
- `预览后用户不发`：执行 `save-draft`
- `直发失败`：退回分步发布，方便排查
