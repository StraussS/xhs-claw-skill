from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from title_utils import calc_title_length
from image_downloader import is_image_url


def check_media(paths: list[str]) -> list[dict]:
    result = []
    for p in paths:
        if is_image_url(p):
            result.append({"input": p, "kind": "url", "exists": True, "ready": True})
        else:
            exists = os.path.exists(p)
            result.append(
                {
                    "input": p,
                    "kind": "file",
                    "exists": exists,
                    "ready": exists and os.path.isabs(p),
                    "absolute": os.path.isabs(p),
                }
            )
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="发布前检查")
    parser.add_argument("--title-file", required=True)
    parser.add_argument("--content-file", required=True)
    parser.add_argument("--images", nargs="*")
    parser.add_argument("--video")
    args = parser.parse_args()

    title = Path(args.title_file).read_text(encoding="utf-8").strip()
    content = Path(args.content_file).read_text(encoding="utf-8").strip()
    title_len = calc_title_length(title)
    media_inputs = args.images or ([] if not args.video else [args.video])
    media = check_media(media_inputs)

    warnings = []
    if title_len > 20:
        warnings.append(f"标题长度超限: {title_len}/20")
    if not content:
        warnings.append("正文为空")
    if args.images and not media:
        warnings.append("未提供图片")
    for item in media:
        if not item.get("ready"):
            warnings.append(f"媒体不可用: {item['input']}")
        if item["kind"] == "url" and "xhscdn.com" in item["input"]:
            warnings.append("检测到小红书 CDN 图片外链，可能出现 403，生产使用优先本地图片路径")

    print(json.dumps(
        {
            "success": len(warnings) == 0,
            "title": title,
            "title_length": title_len,
            "content_length": len(content),
            "media": media,
            "warnings": warnings,
        },
        ensure_ascii=False,
        indent=2,
    ))


if __name__ == "__main__":
    main()
