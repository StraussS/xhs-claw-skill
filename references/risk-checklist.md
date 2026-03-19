# 风险与维护清单

## 日常检查
- [ ] `python scripts/doctor.py`
- [ ] `python scripts/prod_smoke.py`
- [ ] Chrome / Chromium 可正常启动
- [ ] 当前账号登录态仍有效

## 发布前检查
- [ ] 标题长度合规
- [ ] 正文不为空
- [ ] 图片/视频路径有效
- [ ] 图片优先本地绝对路径
- [ ] 非必要不直接使用小红书 CDN 图片 URL

## 运行时关注
- [ ] 搜索是否还能正常返回结构化结果
- [ ] 详情页是否还能抓到 `note` / `comments`
- [ ] 点赞与收藏按钮是否仍匹配当前页面结构
- [ ] 长文编辑器是否仍能识别 `.ProseMirror` / `contenteditable`

## 异常优先排查顺序
1. 运行 `doctor.py`
2. 检查登录是否失效
3. 检查页面结构是否改版
4. 检查素材源是否不稳定
5. 再考虑补丁和重试

## 建议维护点
- selectors 变更统一收敛到 `scripts/xhs/selectors.py`
- 长文编辑器变更优先检查 `scripts/xhs/publish_long_article.py`
- 素材下载问题优先检查 `scripts/image_downloader.py`
