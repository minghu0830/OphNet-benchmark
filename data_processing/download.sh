#!/bin/bash


python -c "
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id='xioamiyh/OphNet2024',
    repo_type='dataset',
    allow_patterns='OphNet2024_all/**',
    local_dir='./'
)
"

echo "✅ Download complete"
