#!/usr/bin/env python3

import argparse
import json
import sys
from pathlib import Path

from PIL import Image, UnidentifiedImageError


SUPPORTED_FORMATS = {
    "PNG",
    "JPEG",
    "WEBP",
    "BMP",
    "TIFF",
}


def analyze_image(image_path: Path) -> dict:
    if not image_path.is_file():
        raise FileNotFoundError(f"Image not found: {image_path}")

    try:
        with Image.open(image_path) as image:
            image_format = image.format

            if image_format not in SUPPORTED_FORMATS:
                raise ValueError(f"Unsupported image format: {image_format}")

            return {
                "file": str(image_path.resolve()),
                "format": image_format,
                "width": image.width,
                "height": image.height,
                "mode": image.mode,
                "size_bytes": image_path.stat().st_size,
            }

    except UnidentifiedImageError as error:
        raise ValueError("The file is not a recognized image.") from error


def main():
    parser = argparse.ArgumentParser(
        description="MiryoVision — image information analyzer."
    )
    parser.add_argument("image", help="Path to an image file")
    args = parser.parse_args()

    try:
        result = analyze_image(Path(args.image))
        print(json.dumps(result, ensure_ascii=False, indent=2))

    except (FileNotFoundError, ValueError, OSError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
