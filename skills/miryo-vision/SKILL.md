---
name: miryo-vision
description: Analyze images, inspect image properties, recognize visible objects and scenes, and extract text from images using OCR. Use when the user asks Claude to inspect, describe, analyze, or read an image.
---

# MiryoVision

MiryoVision is an open-source image analysis plugin for Claude Code.

Its purpose is to provide image inspection, image information extraction, visual analysis, and OCR capabilities.

## Capabilities

- Inspect image files and their properties.
- Describe visible image contents.
- Identify visible everyday objects and animals.
- Analyze scenes and image composition.
- Extract text from images using OCR.
- Read screenshots and scanned documents.
- Return structured image analysis results.

## Supported formats

- PNG
- JPG
- JPEG
- WEBP
- BMP
- TIFF

## Image information

When the user requests image metadata or basic image inspection:

1. Obtain the image path from the user.
2. Verify that the image exists.
3. Run the MiryoVision Python analyzer:

   ```bash
   "${CLAUDE_PLUGIN_ROOT}/.venv/bin/python" \
     "${CLAUDE_PLUGIN_ROOT}/scripts/miryo_vision.py" \
     "/absolute/path/to/image.png"
   ```

4. Read the JSON output.
5. Explain the image properties in a clear format.

The analyzer reports:

- File path
- Image format
- Width and height
- Color mode
- File size in bytes

Do not describe metadata analysis as object recognition.

## Visual analysis

When the user requests visual analysis:

1. Inspect the image using Claude's available image-reading capabilities.
2. Describe only details that are actually visible.
3. Identify objects and scene elements when reasonably clear.
4. Explain uncertainty when an object or detail cannot be identified confidently.
5. Organize the results into useful sections when appropriate.

Do not claim that the Python metadata analyzer performs visual recognition.

## Optical Character Recognition (OCR)

When the user requests text extraction:

1. Verify that the image exists.
2. Determine whether an OCR engine is available.
3. Use the configured OCR engine when installed.
4. Preserve the original language.
5. Preserve line breaks and document structure where possible.
6. Mark unreadable or uncertain text instead of inventing it.

If OCR is unavailable, clearly explain that it has not been performed.

## Workflow

For every image-related request:

1. Identify the requested operation.
2. Locate and validate the image file.
3. Select the appropriate analysis method.
4. Execute the required tool or script.
5. Check the actual result.
6. Present the result to the user.

## Rules

- Never invent image contents or extracted text.
- Never claim an operation succeeded without an actual result.
- Do not overwrite or modify the original image.
- Do not expose private image paths unnecessarily.
- Distinguish objective observations from interpretations.
- Report errors clearly.
- Do not install packages or change system configuration without user permission.

## Python environment

MiryoVision uses Python scripts stored in the plugin's `scripts/` directory.

The development environment uses a local virtual environment:

`.venv/`

Python dependencies must be installed inside this environment, not into the system Python.

## Project structure

```text
MiryoVision/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   └── miryo-vision/
│       └── SKILL.md
├── scripts/
│   └── miryo_vision.py
├── .venv/
├── LICENSE
└── .gitignore
```
