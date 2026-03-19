# 认证与账号流程

## 什么时候读这个文件

当任务涉及：
- 检查登录状态
- 扫码登录
- 手机验证码登录
- 退出登录
- 切换账号
- 多账号管理

## 推荐顺序

### 1. 环境检查

先确认 Chrome 和依赖可用：

```bash
python scripts/doctor.py
```

### 2. 账号选择

先运行：

```bash
python scripts/cli.py list-accounts
```

处理规则：
- `count = 0`：使用默认账号，不加 `--account`
- `count = 1`：告知用户将使用该账号
- `count > 1`：先询问用户选择哪个账号，再在后续命令里统一加 `--account <name>`

## 登录状态检查

```bash
python scripts/cli.py check-login
python scripts/cli.py --account work check-login
```

关注输出：
- `logged_in: true` → 已登录
- `logged_in: false` → 按输出给出的二维码或手机验证码方式继续

## 二维码登录

### 一步式

```bash
python scripts/cli.py login
```

适合本地带界面场景。

### 分步式

```bash
python scripts/cli.py get-qrcode
python scripts/cli.py wait-login
```

适合先展示二维码，再单独等待登录结果。

## 手机验证码登录

每次都要**重新向用户确认手机号**，不要擅自使用历史号码。

```bash
python scripts/cli.py send-code --phone 13800138000
python scripts/cli.py verify-code --code 123456
```

也可以使用交互式命令：

```bash
python scripts/cli.py phone-login --phone 13800138000
```

## 退出登录 / 清理状态

```bash
python scripts/cli.py delete-cookies
python scripts/cli.py --account work delete-cookies
```

## 多账号管理

```bash
python scripts/cli.py add-account --name work --description "工作号"
python scripts/cli.py list-accounts
python scripts/cli.py set-default-account --name work
python scripts/cli.py remove-account --name personal
```

## 失败处理

- `Chrome 未启动`：先运行 `python scripts/chrome_launcher.py`
- `二维码超时`：重新运行 `get-qrcode`
- `验证码受限`：切回二维码登录
- `登录后状态异常`：先 `delete-cookies` 再重新登录
