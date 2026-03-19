# 生产化加固建议

## 适用范围

当准备把这个项目从“能跑”推进到“长期稳定使用”时，读这个文件。

## 已验证能力

- 登录
- 搜索
- 详情与评论抓取
- 点赞
- 收藏
- 图文填写发布表单
- 保存草稿
- 正式发布

## 生产使用建议

### 1. 媒体输入优先级

优先级：
1. 本地绝对路径图片
2. 通用公网图片 URL
3. 小红书自身 CDN 外链（最不稳）

原因：小红书 CDN 外链可能返回 403，不适合直接复用为发布素材。

### 2. 发布流程

生产环境默认使用：
- `publish_preflight.py` 先检查
- `fill-publish` / `fill-publish-video`
- 人确认
- `click-publish`

如果用户取消：
- `save-draft`

### 3. 高频动作控制

- 不要短时间连续评论或收藏
- 批量互动时加明显间隔
- 先做搜索和详情，再决定是否互动

### 4. 冒烟测试

日常检查建议运行：

```bash
python scripts/prod_smoke.py
```

如果要把登录也纳入检查：

```bash
python scripts/prod_smoke.py --include-login
```

### 5. 失败排查顺序

1. `python scripts/doctor.py`
2. 检查 Chrome 是否还活着
3. 检查登录状态
4. 检查是否使用了不稳定的图片 URL
5. 再看页面结构是否变了

## 建议继续补的内容

- 视频发布 smoke test
- 长文发布 smoke test
- 收藏 / 点赞状态检测增强
- 更细的错误码和重试策略
