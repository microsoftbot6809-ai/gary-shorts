#!/bin/bash
# Run once per fresh session, from inside engine/ :  bash setup.sh
set -e
pip install --break-system-packages -q kokoro-onnx pillow numpy scipy soundfile 2>&1 | tail -n 2 || true
mkdir -p models
B=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
[ -f models/kokoro-v1.0.int8.onnx ] || curl -sL -o models/kokoro-v1.0.int8.onnx $B/kokoro-v1.0.int8.onnx
[ -f models/voices-v1.0.bin ] || curl -sL -o models/voices-v1.0.bin $B/voices-v1.0.bin
ls -la models; which ffmpeg
ls /usr/share/fonts/truetype/google-fonts/ofl/anton/Anton-Regular.ttf /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf
