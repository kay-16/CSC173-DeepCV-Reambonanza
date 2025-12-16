import pprint as pp
import numpy as np
from torch.utils.data import random_split
import os
import shutil
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DIR = os.path.join(BASE_DIR, 'dataset', 'raw')
OUT_DIR = os.path.join(BASE_DIR, 'dataset', 'processed')


# Split dataset ratios (70% training set, 15% validation set, 15% test set)
SPLIT = {
    'train': 0.7,
    'val': 0.15,
    'test': 0.15
}

# For reproducibility
random.seed(42) 

# Create output directories
for split in SPLIT:
    for cls in os.listdir(RAW_DIR):
        os.makedirs(os.path.join(OUT_DIR, split, cls), exist_ok=True)

# Split per class
for cls in os.listdir(RAW_DIR):
    # Get all images in the class directory
    cls_path = os.path.join(RAW_DIR, cls)
    images = os.listdir(cls_path)
    random.shuffle(images) # Shuffle images for randomness

    # Calculate split indices
    n_total = len(images)
    n_train = int(SPLIT['train'] * n_total)
    n_val = int(SPLIT['val'] * n_total)

    # Split images into train, val, test
    train_images = images[:n_train]
    val_images = images[n_train:n_train + n_val]
    test_images = images[n_train + n_val:]

    for image in train_images:
        shutil.copy(os.path.join(cls_path, image),
                    os.path.join(OUT_DIR, 'train', cls, image)
        )

    for image in val_images:
        shutil.copy(os.path.join(cls_path, image),
                    os.path.join(OUT_DIR, 'val', cls, image)
        )

    for image in test_images:
        shutil.copy(os.path.join(cls_path, image),
                    os.path.join(OUT_DIR, 'test', cls, image)
        )

print("Dataset split completed.")

