from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
BACKGROUND_DIR = ROOT / "backgrounds"
OUTPUT_DIR = ROOT / "images"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

W, H = 1080, 1440
INK = (12, 15, 14)
MUTED = (77, 86, 82)
PAPER = (248, 249, 246)
EMERALD = (9, 107, 69)
CHARCOAL = (17, 22, 18)

FONT_MEDIUM = "/System/Library/Fonts/STHeiti Medium.ttc"
FONT_LIGHT = "/System/Library/Fonts/STHeiti Light.ttc"


def font(size, bold=False):
    return ImageFont.truetype(FONT_MEDIUM if bold else FONT_LIGHT, size)


def cover_crop(image):
    image = image.convert("RGB")
    scale = max(W / image.width, H / image.height)
    nw, nh = round(image.width * scale), round(image.height * scale)
    image = image.resize((nw, nh), Image.Resampling.LANCZOS)
    left = max(0, (nw - W) // 2)
    top = max(0, (nh - H) // 2)
    return image.crop((left, top, left + W, top + H))


def add_text_scrim(image, top_strength=190, bottom_strength=80):
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    for y in range(H):
        top_alpha = max(0, int(top_strength * (1 - y / 760)))
        bottom_alpha = max(0, int(bottom_strength * ((y - 900) / 540)))
        alpha = max(top_alpha, bottom_alpha)
        if alpha:
            draw.line([(0, y), (W, y)], fill=(248, 249, 246, alpha))
    return Image.alpha_composite(image.convert("RGBA"), overlay).convert("RGB")


def wrap_text(draw, text, text_font, max_width):
    lines = []
    current = ""
    for char in text:
        trial = current + char
        if draw.textlength(trial, font=text_font) <= max_width or not current:
            current = trial
        else:
            lines.append(current)
            current = char
    if current:
        lines.append(current)
    return lines


def draw_lines(draw, xy, lines, text_font, fill, spacing=10):
    x, y = xy
    for line in lines:
        draw.text((x, y), line, font=text_font, fill=fill)
        box = draw.textbbox((x, y), line, font=text_font)
        y = box[3] + spacing
    return y


def draw_brand(draw, x, y, label="make-goal"):
    label_font = font(30, bold=True)
    pad_x, pad_y = 22, 11
    box = draw.textbbox((0, 0), label, font=label_font)
    rect = (x, y, x + box[2] + pad_x * 2, y + box[3] + pad_y * 2)
    draw.rounded_rectangle(rect, radius=28, fill=CHARCOAL)
    draw.text((x + pad_x, y + pad_y - 1), label, font=label_font, fill=PAPER)


def draw_footer(draw, index):
    footer = f"{index}/05  github.com/talkcozy/make-goal"
    footer_font = font(24)
    draw.text((70, H - 88), footer, font=footer_font, fill=(70, 78, 74))


def render_cover():
    image = cover_crop(Image.open(BACKGROUND_DIR / "cover-background.png"))
    image = add_text_scrim(image, top_strength=210, bottom_strength=130)
    draw = ImageDraw.Draw(image)

    draw_brand(draw, 72, 92)
    title_font = font(92, bold=True)
    subtitle_font = font(44)
    quote_font = font(34, bold=True)

    y = 190
    y = draw_lines(draw, (72, y), ["复杂需求", "别直接丢给 AI"], title_font, INK, spacing=14)
    y += 28
    subtitle = wrap_text(draw, "先生成一个能长期执行的 goal.md", subtitle_font, 790)
    y = draw_lines(draw, (76, y), subtitle, subtitle_font, MUTED, spacing=8)

    draw.rounded_rectangle((72, H - 230, 930, H - 108), radius=18, fill=(255, 255, 255))
    draw.rectangle((72, H - 230, 82, H - 108), fill=EMERALD)
    draw.text((112, H - 204), "你必须非常努力，才会看起来毫不费力。", font=quote_font, fill=INK)

    image.save(OUTPUT_DIR / "cover.jpg", quality=92, optimize=True)


SLIDES = [
    {
        "source": "slide-01-background.png",
        "out": "slide-01.jpg",
        "index": "01",
        "title": "为什么长任务会烂尾？",
        "bullets": [
            "计划只在聊天记录里",
            "环境依赖没有写清",
            "验证方式靠临时记忆",
            "下一轮 agent 接不上",
        ],
    },
    {
        "source": "slide-02-background.png",
        "out": "slide-02.jpg",
        "index": "02",
        "title": "goal.md 不是待办清单",
        "bullets": [
            "目标和边界",
            "上下文和参考资料",
            "里程碑和验收标准",
            "进度记录和恢复方式",
        ],
    },
    {
        "source": "slide-03-background.png",
        "out": "slide-03.jpg",
        "index": "03",
        "title": "真正关键的是 Harness",
        "bullets": [
            "runtime 和 package manager",
            "CLI、插件、MCP、服务",
            "环境变量和权限",
            "缺失依赖时的 fallback",
        ],
    },
    {
        "source": "slide-04-background.png",
        "out": "slide-04.jpg",
        "index": "04",
        "title": "正确交给 Agent 的方式",
        "bullets": [
            "让它先读仓库",
            "自己安装 make-goal",
            "验证 skill 可用",
            "再生成并执行 goal.md",
        ],
    },
    {
        "source": "slide-05-background.png",
        "out": "slide-05.jpg",
        "index": "05",
        "title": "适合这些长期任务",
        "bullets": [
            "软件重构、产品 MVP",
            "研究报告、文档迁移",
            "游戏开发、知识库清理",
            "前面越认真，后面越省心",
        ],
    },
]


def render_slide(slide):
    image = cover_crop(Image.open(BACKGROUND_DIR / slide["source"]))
    image = add_text_scrim(image, top_strength=220, bottom_strength=150)
    draw = ImageDraw.Draw(image)

    index_font = font(28, bold=True)
    title_font = font(68, bold=True)
    bullet_font = font(39, bold=True)
    note_font = font(24)

    draw.text((72, 86), f"make-goal / {slide['index']}", font=index_font, fill=EMERALD)
    title_lines = wrap_text(draw, slide["title"], title_font, 850)
    y = draw_lines(draw, (72, 146), title_lines, title_font, INK, spacing=12)

    y += 38
    for bullet in slide["bullets"]:
        wrapped = wrap_text(draw, bullet, bullet_font, 800)
        draw.rounded_rectangle((75, y + 14, 96, y + 35), radius=10, fill=EMERALD)
        y = draw_lines(draw, (118, y), wrapped, bullet_font, INK, spacing=7)
        y += 18

    draw.text((72, H - 142), "你必须非常努力，才会看起来毫不费力。", font=note_font, fill=MUTED)
    draw_footer(draw, slide["index"])

    image.save(OUTPUT_DIR / slide["out"], quality=92, optimize=True)


def main():
    render_cover()
    for slide in SLIDES:
        render_slide(slide)


if __name__ == "__main__":
    main()
