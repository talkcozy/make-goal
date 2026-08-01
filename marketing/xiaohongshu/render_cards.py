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
LINE = (214, 221, 214)
SOFT = (238, 243, 236)
GOLD = (178, 135, 54)

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


def draw_panel(draw, rect, radius=26, fill=(252, 253, 250), outline=LINE):
    x1, y1, x2, y2 = rect
    draw.rounded_rectangle((x1, y1 + 10, x2, y2 + 10), radius=radius, fill=(222, 226, 220))
    draw.rounded_rectangle(rect, radius=radius, fill=fill, outline=outline, width=1)


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


def draw_tag(draw, x, y, label, fill=SOFT, text_fill=EMERALD):
    tag_font = font(24, bold=True)
    box = draw.textbbox((0, 0), label, font=tag_font)
    rect = (x, y, x + box[2] + 30, y + 42)
    draw.rounded_rectangle(rect, radius=21, fill=fill, outline=LINE, width=1)
    draw.text((x + 15, y + 7), label, font=tag_font, fill=text_fill)
    return rect[2]


def draw_numbered_rows(draw, rows, x, y, width, row_height=86):
    number_font = font(24, bold=True)
    title_font = font(28, bold=True)
    body_font = font(25)
    for i, (title, body) in enumerate(rows, 1):
        top = y + (i - 1) * row_height
        draw.rounded_rectangle((x, top, x + width, top + row_height - 14), radius=18, fill=(245, 248, 242), outline=LINE)
        draw.ellipse((x + 22, top + 20, x + 58, top + 56), fill=EMERALD)
        draw.text((x + 31, top + 22), str(i), font=number_font, fill=PAPER)
        draw.text((x + 78, top + 14), title, font=title_font, fill=INK)
        draw.text((x + 78, top + 48), body, font=body_font, fill=MUTED)


def draw_chip_grid(draw, items, x, y, col_width, row_height, columns=2):
    title_font = font(29, bold=True)
    body_font = font(23)
    for i, item in enumerate(items):
        col = i % columns
        row = i // columns
        left = x + col * col_width
        top = y + row * row_height
        draw.rounded_rectangle((left, top, left + col_width - 24, top + row_height - 18), radius=18, fill=(246, 248, 244), outline=LINE)
        draw.rectangle((left, top + 24, left + 7, top + row_height - 42), fill=EMERALD if i % 2 == 0 else GOLD)
        draw.text((left + 24, top + 18), item["title"], font=title_font, fill=INK)
        lines = wrap_text(draw, item["body"], body_font, col_width - 72)
        draw_lines(draw, (left + 24, top + 58), lines[:2], body_font, MUTED, spacing=5)


def draw_quote(draw, text, y):
    quote_font = font(30, bold=True)
    draw.rounded_rectangle((72, y, 1008, y + 112), radius=18, fill=(255, 255, 255), outline=LINE)
    draw.rectangle((72, y, 82, y + 112), fill=EMERALD)
    lines = wrap_text(draw, text, quote_font, 830)
    draw_lines(draw, (112, y + 24), lines[:2], quote_font, INK, spacing=8)


def render_cover():
    image = cover_crop(Image.open(BACKGROUND_DIR / "cover-background.png"))
    image = add_text_scrim(image, top_strength=210, bottom_strength=130)
    draw = ImageDraw.Draw(image)

    draw_brand(draw, 72, 92)
    title_font = font(90, bold=True)
    subtitle_font = font(35)
    panel_title_font = font(34, bold=True)

    y = 190
    y = draw_lines(draw, (72, y), ["复杂需求", "别直接丢给 AI"], title_font, INK, spacing=14)
    y += 28
    subtitle = wrap_text(draw, "先生成一个能长期执行、可恢复、可验证的 goal.md", subtitle_font, 620)
    draw_lines(draw, (76, y), subtitle, subtitle_font, MUTED, spacing=8)

    draw_panel(draw, (72, 555, 830, 922))
    draw.text((112, 594), "make-goal 先补齐 3 层信息", font=panel_title_font, fill=INK)
    draw_numbered_rows(
        draw,
        [
            ("Context", "目标、背景、资料、边界"),
            ("Harness", "运行环境、工具、权限、fallback"),
            ("Validation", "里程碑、验收、进度恢复"),
        ],
        112,
        660,
        660,
        row_height=78,
    )

    draw_quote(draw, "你必须非常努力，才会看起来毫不费力。", H - 235)

    image.save(OUTPUT_DIR / "cover.jpg", quality=92, optimize=True)


SLIDES = [
    {
        "source": "slide-01-background.png",
        "out": "slide-01.jpg",
        "index": "01",
        "title": "长任务为什么会烂尾？",
        "lead": "问题通常不是 agent 不努力，而是任务状态没有变成稳定资产。",
        "kind": "failure-table",
        "rows": [
            ("计划在聊天里", "换会话后上下文断片"),
            ("依赖靠口头说", "缺工具时直接卡住"),
            ("验收没写清", "做完也不知道对不对"),
            ("进度没记录", "下一轮重复摸索"),
        ],
        "takeaway": "结论：长期任务需要可执行上下文，而不是一次性 plan。",
    },
    {
        "source": "slide-02-background.png",
        "out": "slide-02.jpg",
        "index": "02",
        "title": "goal.md 不是待办清单",
        "lead": "它更像一份给 agent 的目标合约：能读、能做、能验、能续。",
        "kind": "structure-grid",
        "items": [
            {"title": "目标", "body": "最终交付物、成功标准"},
            {"title": "边界", "body": "明确不做什么，避免漂移"},
            {"title": "上下文", "body": "必须阅读的仓库、文件、链接"},
            {"title": "里程碑", "body": "阶段任务和验收口径"},
            {"title": "验证", "body": "测试、截图、命令、人工检查"},
            {"title": "恢复", "body": "进度记录、阻塞规则、下一步"},
        ],
        "formula": ["goal.md = 目标 + 上下文 + Harness", "里程碑 + 验证 + 进度记录"],
    },
    {
        "source": "slide-03-background.png",
        "out": "slide-03.jpg",
        "index": "03",
        "title": "Harness：别让环境拖垮 Agent",
        "lead": "目标很清楚，但依赖没写清，agent 还是会停在半路。",
        "kind": "harness-groups",
        "groups": [
            ("运行层", ["runtime", "package manager", "CLI 工具"]),
            ("连接层", ["API keys", "MCP / 插件", "本地服务"]),
            ("保障层", ["readiness checks", "权限", "fallback"]),
        ],
        "takeaway": "把 harness 写进 goal.md，agent 才能先检查、再执行、缺什么补什么。",
    },
    {
        "source": "slide-04-background.png",
        "out": "slide-04.jpg",
        "index": "04",
        "title": "正确交给 Agent 的方式",
        "lead": "不要让用户手动下载仓库。给 agent 一段任务，让它自己读、装、验。",
        "kind": "agent-prompt",
        "prompt": [
            "Open https://github.com/talkcozy/make-goal.",
            "Read the repo, install make-goal,",
            "verify it is available, then use $make-goal",
            "to create a goal.md for this project.",
        ],
        "steps": [
            ("读仓库", "理解 skill 结构"),
            ("安装", "放到当前 agent 环境"),
            ("验证", "确认命令可用"),
            ("生成", "产出 goal.md"),
        ],
    },
    {
        "source": "slide-05-background.png",
        "out": "slide-05.jpg",
        "index": "05",
        "title": "适合这些长期任务",
        "lead": "只要任务会跨多轮、跨文件、跨验证，就值得先做 goal。",
        "kind": "scenario-grid",
        "items": [
            {"title": "软件重构", "body": "多目录、多风险、要回归"},
            {"title": "产品 MVP", "body": "功能拆解、验收、迭代"},
            {"title": "研究报告", "body": "资料、假设、引用来源"},
            {"title": "游戏开发", "body": "玩法、资源、手感验证"},
            {"title": "文档迁移", "body": "结构、缺口、一致性"},
            {"title": "知识库清理", "body": "分类、去重、命名标准"},
        ],
        "takeaway": "判断标准：任务越长、环境越复杂，越要先做 goal.md",
    },
]


def render_slide(slide):
    image = cover_crop(Image.open(BACKGROUND_DIR / slide["source"]))
    image = add_text_scrim(image, top_strength=220, bottom_strength=150)
    draw = ImageDraw.Draw(image)

    index_font = font(28, bold=True)
    title_font = font(58, bold=True)
    lead_font = font(27)
    note_font = font(24)
    panel_title_font = font(31, bold=True)

    draw.text((72, 86), f"make-goal / {slide['index']}", font=index_font, fill=EMERALD)
    title_lines = wrap_text(draw, slide["title"], title_font, 900)
    y = draw_lines(draw, (72, 146), title_lines, title_font, INK, spacing=10)
    y += 18
    lead_lines = wrap_text(draw, slide["lead"], lead_font, 860)
    draw_lines(draw, (76, y), lead_lines, lead_font, MUTED, spacing=8)

    if slide["kind"] == "failure-table":
        draw_panel(draw, (72, 330, 1008, 895))
        draw_tag(draw, 112, 374, "表现")
        draw_tag(draw, 550, 374, "结果", fill=(248, 243, 231), text_fill=GOLD)
        row_font = font(30, bold=True)
        result_font = font(29)
        row_y = 452
        for title, result in slide["rows"]:
            draw.rounded_rectangle((112, row_y, 492, row_y + 76), radius=18, fill=(244, 248, 243), outline=LINE)
            draw.text((140, row_y + 20), title, font=row_font, fill=INK)
            draw.line((522, row_y + 38, 548, row_y + 38), fill=GOLD, width=4)
            draw.polygon([(548, row_y + 38), (536, row_y + 30), (536, row_y + 46)], fill=GOLD)
            draw.text((580, row_y + 19), result, font=result_font, fill=MUTED)
            row_y += 106
        draw_quote(draw, slide["takeaway"], 965)

    elif slide["kind"] == "structure-grid":
        draw_panel(draw, (72, 330, 1008, 940))
        draw.text((112, 374), "一个可执行 goal.md 至少包含：", font=panel_title_font, fill=INK)
        draw_chip_grid(draw, slide["items"], 112, 438, 430, 138, columns=2)
        draw_panel(draw, (72, 990, 1008, 1135), radius=22, fill=(19, 24, 20), outline=(19, 24, 20))
        draw.text((112, 1025), "结构公式", font=font(24, bold=True), fill=(158, 207, 178))
        draw_lines(draw, (112, 1060), slide["formula"], font(29, bold=True), PAPER, spacing=7)

    elif slide["kind"] == "harness-groups":
        group_y = 330
        chip_font = font(27, bold=True)
        for i, (group_title, chips) in enumerate(slide["groups"]):
            draw_panel(draw, (72, group_y, 1008, group_y + 175), radius=22)
            color = EMERALD if i != 1 else GOLD
            draw.text((112, group_y + 28), group_title, font=panel_title_font, fill=INK)
            chip_x = 112
            chip_y = group_y + 84
            for chip in chips:
                chip_width = int(draw.textlength(chip, font=chip_font)) + 42
                draw.rounded_rectangle((chip_x, chip_y, chip_x + chip_width, chip_y + 52), radius=26, fill=(241, 247, 240), outline=LINE)
                draw.ellipse((chip_x + 17, chip_y + 20, chip_x + 27, chip_y + 30), fill=color)
                draw.text((chip_x + 38, chip_y + 10), chip, font=chip_font, fill=MUTED)
                chip_x += chip_width + 16
            group_y += 205
        draw_quote(draw, slide["takeaway"], 995)

    elif slide["kind"] == "agent-prompt":
        draw_panel(draw, (72, 330, 1008, 755), radius=24, fill=(17, 22, 18), outline=(17, 22, 18))
        draw.text((112, 372), "可直接发给 Agent 的提示词", font=font(28, bold=True), fill=(158, 207, 178))
        prompt_font = font(25, bold=True)
        prompt_y = 430
        for line in slide["prompt"]:
            wrapped = wrap_text(draw, line, prompt_font, 800)
            prompt_y = draw_lines(draw, (112, prompt_y), wrapped, prompt_font, PAPER, spacing=6)
            prompt_y += 8

        draw_panel(draw, (72, 810, 1008, 1110), radius=24)
        draw.text((112, 852), "agent 应该自动完成：", font=panel_title_font, fill=INK)
        step_x = 112
        step_y = 920
        step_w = 206
        for i, (name, body) in enumerate(slide["steps"], 1):
            left = step_x + (i - 1) * (step_w + 18)
            draw.rounded_rectangle((left, step_y, left + step_w, step_y + 132), radius=18, fill=(246, 248, 244), outline=LINE)
            draw.text((left + 20, step_y + 16), f"0{i}", font=font(24, bold=True), fill=EMERALD)
            draw.text((left + 20, step_y + 50), name, font=font(31, bold=True), fill=INK)
            body_lines = wrap_text(draw, body, font(22), step_w - 40)
            draw_lines(draw, (left + 20, step_y + 90), body_lines[:2], font(22), MUTED, spacing=4)

    elif slide["kind"] == "scenario-grid":
        draw_panel(draw, (72, 330, 1008, 1008))
        draw.text((112, 374), "最适合这些“不该只靠聊天记录”的任务：", font=panel_title_font, fill=INK)
        draw_chip_grid(draw, slide["items"], 112, 438, 430, 150, columns=2)
        draw_quote(draw, slide["takeaway"], 1060)

    draw.text((72, H - 142), "你必须非常努力，才会看起来毫不费力。", font=note_font, fill=MUTED)
    draw_footer(draw, slide["index"])

    image.save(OUTPUT_DIR / slide["out"], quality=92, optimize=True)


def main():
    render_cover()
    for slide in SLIDES:
        render_slide(slide)


if __name__ == "__main__":
    main()
