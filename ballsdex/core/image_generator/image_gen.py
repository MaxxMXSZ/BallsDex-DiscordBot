import os
import textwrap
from pathlib import Path
from typing import TYPE_CHECKING

from PIL import Image, ImageDraw, ImageFont, ImageOps

if TYPE_CHECKING:
    from ballsdex.core.models import BallInstance


SOURCES_PATH = Path(os.path.dirname(os.path.abspath(__file__)), "./src")
WIDTH = 1500
HEIGHT = 2000

RECTANGLE_WIDTH = WIDTH - 40
RECTANGLE_HEIGHT = (HEIGHT // 5) * 2

CORNERS = ((34, 261), (1393, 992))
artwork_size = [b - a for a, b in zip(*CORNERS)]

title_font = ImageFont.truetype(str(SOURCES_PATH / "ArsenicaTrial-Extrabold.ttf"), 165)
capacity_name_font = ImageFont.truetype(str(SOURCES_PATH / "Bobby Jones Soft.otf"), 90)
capacity_description_font = ImageFont.truetype(str(SOURCES_PATH / "OpenSans-Semibold.ttf"), 55)
stats_font = ImageFont.truetype(str(SOURCES_PATH / "Bobby Jones Soft.otf"), 90)
stats_percent = ImageFont.truetype(str(SOURCES_PATH / "Pusab.ttf"), 50)
credits_font = ImageFont.truetype(str(SOURCES_PATH / "arial.ttf"), 40)


def draw_card(ball_instance: "BallInstance"):
    ball = ball_instance.countryball
    ball_health = (255, 255, 255, 255)
    ball_attack = (255, 255, 255, 255)
    ball_health_bonus = (255, 255, 255, 255)
    ball_attack_bonus = (255, 255, 255, 255)
    if ball_instance.shiny:
        image = Image.open(str(SOURCES_PATH / "shiny.png"))
        ball_health = (255, 255, 255, 255)
        ball_attack = (255, 255, 255, 255)
        ball_health_bonus = (255, 255, 255, 255)
        ball_attack_bonus = (255, 255, 255, 255)
    elif special_image := ball_instance.special_card:
        image = Image.open("." + special_image)
    else:
        image = Image.open("." + ball.cached_regime.background)
    image = image.convert("RGBA")
    icon = (
        Image.open("." + ball.cached_economy.icon).convert("RGBA") if ball.cached_economy else None
    )

    draw = ImageDraw.Draw(image)
    draw.text((50, 90), ball.short_name or ball.country, font=title_font, stroke_width=6, stroke_fill=(0, 0, 0, 255))
    for i, line in enumerate(textwrap.wrap(f"Ability: {ball.capacity_name}", width=26)):
        draw.text(
            (70, 1070 + 75 * i),
            line,
            font=capacity_name_font,
            fill=(255, 255, 255, 255),
            stroke_width=3,
            stroke_fill=(0, 0, 0, 255),
        )
    for i, line in enumerate(textwrap.wrap(ball.capacity_description, width=40)):
        draw.text(
            (60, 1370 + 50 * i),
            line,
            font=capacity_description_font,
            stroke_width=3,
            stroke_fill=(0, 0, 0, 255),
        )
    draw.text(
        (320, 1725),
        str(ball_instance.health),
        font=stats_font,
        fill=ball_health,
        stroke_width=3,
        stroke_fill=(0, 0, 0, 255),
    )
    draw.text(
        (1120, 1725),
        str(ball_instance.attack),
        font=stats_font,
        stroke_width=3,
        stroke_fill=(0, 0, 0, 255),
        anchor="ra",
    )
    if ball_instance.health_bonus >= 0:
        draw.text(
            (320, 1795),
            str("(+{}%)").format(ball_instance.health_bonus),
            font=stats_percent,
            stroke_width=3,
            stroke_fill=(0, 0, 0, 255),
        )
    else:
         draw.text(
            (320, 1795),
            str("({}%)").format(ball_instance.health_bonus),
            font=stats_percent,
            stroke_width=3,
            stroke_fill=(0, 0, 0, 255),
        )
    if ball_instance.attack_bonus >= 0:
        draw.text(
            (1120, 1795),
            str("(+{}%)").format(ball_instance.attack_bonus),
            font=stats_percent,
            stroke_width=3,
            stroke_fill=(0, 0, 0, 255),
            anchor="ra",
        )
    else:
         draw.text(
            (1120, 1795),
            str("({}%)").format(ball_instance.attack_bonus),
            font=stats_percent,
            stroke_width=3,
            stroke_fill=(0, 0, 0, 255),
            anchor="ra",
        )
    draw.text(
        (2470, 30),
        str(ball_instance.health),
        font=stats_font,
        stroke_width=3,
        stroke_fill=(0, 0, 0, 255),
    )
    draw.text(
        (1820, 30),
        str(ball_instance.attack),
        font=stats_font,
        stroke_width=3,
        stroke_fill=(0, 0, 0, 255),
    )
    if ball_instance.health_bonus >= 0:
        draw.text(
            (2470, 100),
            str("(+{}%)").format(ball_instance.health_bonus),
            font=stats_percent,
            stroke_width=3,
            stroke_fill=(0, 0, 0, 255),
        )
    else:
         draw.text(
            (2470, 100),
            str("({}%)").format(ball_instance.health_bonus),
            font=stats_percent,
            stroke_width=3,
            stroke_fill=(0, 0, 0, 255),
        )
    if ball_instance.attack_bonus >= 0:
        draw.text(
            (1820, 100),
            str("(+{}%)").format(ball_instance.attack_bonus),
            font=stats_percent,
            stroke_width=3,
            stroke_fill=(0, 0, 0, 255),
        )
    else:
         draw.text(
            (1820, 100),
            str("({}%)").format(ball_instance.attack_bonus),
            font=stats_percent,
            stroke_width=3,
            stroke_fill=(0, 0, 0, 255),
        )
    for i, line in enumerate(textwrap.wrap(f"Ability: {ball.capacity_name}", width=26)):
        draw.text(
            (1750, 200 + 75 * i),
            line,
            font=capacity_name_font,
            fill=(255, 255, 255, 255),
            stroke_width=3,
            stroke_fill=(0, 0, 0, 255),
        )
    for i, line in enumerate(textwrap.wrap(ball.capacity_description, width=40)):
        draw.text(
            (1750, 400 + 50 * i),
            line,
            font=capacity_description_font,
            stroke_width=3,
            stroke_fill=(0, 0, 0, 255),
        )
    draw.text(
        (30, 1870),
        # Modifying the line below is breaking the licence as you are removing credits
        # If you don't want to receive a DMCA, just don't
        "Created by El Laggron\n" f"Artwork author: {ball.credits}",
        font=credits_font,
        fill=(0, 0, 0, 255),
        stroke_width=0,
        stroke_fill=(255, 255, 255, 255),
    )
    draw.text(
        (30, 1927),
        str("ID {}").format(hex(ball_instance.pk).upper()[2:]),
        font=credits_font,
        fill=(0, 0, 0, 255),
        stroke_width=0,
        stroke_fill=(255, 255, 255, 255),
    )
    tmfcg = (f"{ball_instance.catch_date}"[11:19])
    draw.text(
        (30, 1956),
        str("Catch Date: {}".format(ball_instance.catch_date)[:22]),
        font=credits_font,
        fill=(0, 0, 0, 255),
        stroke_width=0,
        stroke_fill=(255, 255, 255, 255),
    )
    draw.text(
        (550, 1956),
        str("(Time: {} UTC)".format(tmfcg)),
        font=credits_font,
        fill=(0, 0, 0, 255),
        stroke_width=0,
        stroke_fill=(255, 255, 255, 255),
    )
    draw.text(
        (1700, 900),
        "Created by El Laggron\n" f"Artwork author: {ball.credits}",
        font=credits_font,
        fill=(0, 0, 0, 255),
        stroke_width=0,
        stroke_fill=(255, 255, 255, 255),
    )
    draw.text(
        (1700, 957),
        str("ID {}").format(hex(ball_instance.pk).upper()[2:]),
        font=credits_font,
        fill=(0, 0, 0, 255),
        stroke_width=0,
        stroke_fill=(255, 255, 255, 255),
    )
    draw.text(
        (1700, 986),
        str("Catch Date: {}".format(ball_instance.catch_date)[:22]),
        font=credits_font,
        fill=(0, 0, 0, 255),
        stroke_width=0,
        stroke_fill=(255, 255, 255, 255),
    )
    draw.text(
        (2220, 986),
        str("(Time: {} UTC)".format(tmfcg)),
        font=credits_font,
        fill=(0, 0, 0, 255),
        stroke_width=0,
        stroke_fill=(255, 255, 255, 255),
    )
    artwork = Image.open("." + ball.collection_card).convert("RGBA")
    image.paste(ImageOps.fit(artwork, artwork_size), CORNERS[0])  # type: ignore

    if icon:
        icon = ImageOps.fit(icon, (192, 192))
        image.paste(icon, (1200, 30), mask=icon)
        icon.close()
    artwork.close()

    return image
