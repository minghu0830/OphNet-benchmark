python ./extract_tad_feature.py \
    --part 0 --gpu 0 --total 1 \
    --data_path ../../dataset/videos \
    --save_path ./features/videomae \
    --model vit_giant_patch14_224 \
    --ckpt_path ./ckpt/vit_g_hybrid_pt_1200e_k710_ft.pth