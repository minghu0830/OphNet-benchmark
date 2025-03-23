#!/bin/bash

#  allow_patterns: OphNet2024_all,OphNet2024_trimmed_operation,OphNet2024_trimmed_phase,Features,Checkpoints
python -c "
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id='xioamiyh/OphNet2024',
    repo_type='dataset',
    # allow_patterns='OphNet2024_all/**',
    # all untrimmed video

    # allow_patterns='OphNet2024_localization/**',
    # untrimmed videos annotated with temporal boundaries

    # allow_patterns='OphNet2024_trimmed_operation/**',
    # trimmed videos-operation level

    allow_patterns='OphNet2024_trimmed_phase/**',
    # trimmed videos-phase level

    # allow_patterns='Checkpoints/**',

    # allow_patterns='Features/**',

    local_dir='./'
)
"

echo "✅ Download complete"
