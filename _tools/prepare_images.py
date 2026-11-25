"""Regenerate website previews after updating the original images (Pillow and PyYAML)."""

from io import BytesIO
from pathlib import Path

import yaml
from PIL import Image, ImageCms, ImageOps


ROOT = Path(__file__).resolve().parents[1]
SRGB = ImageCms.createProfile("sRGB")


def records(name):
    return yaml.safe_load((ROOT / "_data" / f"{name}.yml").read_text(encoding="utf-8"))


def save_preview(source, image, suffix, quality):
    output = source.with_name(f"{source.name}.{suffix}.webp")
    encoded = BytesIO()
    image.save(encoded, "WEBP", quality=quality, method=6)
    data = encoded.getvalue()
    if not output.exists() or output.read_bytes() != data:
        output.write_bytes(data)
    elif source.stat().st_mtime_ns > output.stat().st_mtime_ns:
        output.touch()


def prepare(source, kind):
    with Image.open(source) as original:
        image = ImageOps.exif_transpose(original)
        profile = image.info.get("icc_profile")
        mode = "RGBA" if image.has_transparency_data else "RGB"
        if profile:
            image = ImageCms.profileToProfile(image, BytesIO(profile), SRGB, outputMode=mode)
        else:
            image = image.convert(mode)

        if kind == "gallery":
            for width, suffix in [(600, "preview"), (1080, "retina")]:
                card = ImageOps.fit(image, (width, width * 2 // 3), Image.Resampling.LANCZOS)
                save_preview(source, card, suffix, 79)
        elif kind == "poster":
            image.thumbnail((1440, 1440), Image.Resampling.LANCZOS)
            save_preview(source, image, "preview", 91)
        else:
            centering = (0.5, 0.25 if kind == "students" else 0.5)
            portrait = ImageOps.fit(image, (480, 600), Image.Resampling.LANCZOS, centering=centering)
            save_preview(source, portrait, "preview", 84)


if __name__ == "__main__":
    for year in records("gallery"):
        for album in year["activities"]:
            for photo in album["photos"]:
                prepare(ROOT / photo.lstrip("/"), "gallery")
    for group in ["students", "team_members"]:
        for member in records(group):
            prepare(ROOT / "images/teampic" / member["photo"], group)
    prepare(ROOT / "images/picpic/UTL-Research-Poster-Square.png", "poster")
