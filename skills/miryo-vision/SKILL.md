---
name: miryo-vision
description: Analyze images using the active model's visual capabilities and Python metadata inspection. Describe photographs, identify visible objects and scenes, inspect image properties, and extract text when an OCR engine is available.
---

# MiryoVision

MiryoVision is an open-source image analysis plugin for Claude Code.

It combines the active AI model's visual understanding with a Python image metadata analyzer.

## Core capabilities

### 1. Visual analysis — AI Vision

When a user asks to describe or analyze an image:

1. Locate the image supplied by the user.
2. Check whether the active AI model supports image input.
3. Inspect the image using the model's available image-reading capabilities.
4. Describe the visible scene and objects.
5. Identify animals, everyday objects, and visible activities when reasonably clear.
6. Describe composition, colors, and relevant visual details.
7. Explain uncertainty instead of guessing.

Do not use the Python metadata analyzer as a substitute for visual understanding.

A local file path alone does not guarantee that the AI model can access the image contents. The image must be provided through a supported image-input mechanism.

Do not claim that an image was visually inspected if the active model cannot access its contents.

### 2. Image metadata — Python Analyzer

When the user requests technical image information:

1. Verify that the image exists.
2. Run the Python analyzer using Python 3.
3. Read and validate its JSON output.
4. Present the actual metadata.
5. Report errors if the analyzer cannot run.

Command:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/miryo_vision.py" \
  "/absolute/path/to/image.png"
```

The analyzer reports:

- File path
- Image format
- Width and height
- Color mode
- File size in bytes

### 3. Combined analysis

When the user requests a complete image analysis:

1. Perform visual analysis using the active model's image-reading capabilities.
2. Run the Python analyzer for technical metadata.
3. Combine both results into one response.
4. Clearly distinguish visual observations from technical metadata.
5. Explain if either part of the analysis could not be completed.

### 4. Optical Character Recognition (OCR)

When the user requests text extraction:

1. Check whether an OCR engine is available.
2. Use it only when properly configured.
3. Preserve the original language and line breaks where possible.
4. Mark uncertain text rather than inventing it.
5. If OCR is unavailable, explain that text recognition has not been performed.

Do not claim that OCR is implemented by the metadata analyzer.

### 5. Supported formats

The Python analyzer supports:

- PNG
- JPG
- JPEG
- WEBP
- BMP
- TIFF

Actual visual format support depends on the active AI model and its image-input mechanism.

## Rules

- Never invent image contents or extracted text.
- Never claim an operation succeeded without an actual result.
- Do not overwrite or modify original images.
- Do not expose private image paths unnecessarily.
- Distinguish objective observations from interpretations.
- Report errors clearly.
- Do not install packages or change system configuration without user permission.
- Do not treat metadata as evidence of what an image depicts.

## Python environment

MiryoVision uses Python 3 and Pillow.

Python dependencies are defined in `requirements.txt`.

The development environment may use a local virtual environment:

`.venv/`

The `.venv/` directory is excluded from Git.

The published plugin does not include the development virtual environment. Do not assume that `.venv/` exists in an installed plugin.

Python 3 and the dependencies listed in `requirements.txt` must be available in the execution environment.
