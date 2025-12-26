#!/bin/bash

echo "Starting model weight download..."

DEST_DIR="models"
mkdir -p $DEST_DIR

DOWNLOAD_URL="https://drive.google.com/uc?export=download&id=1CqeDa8ar9KSz4Ro8EcgaiFCclnbbg8sm"

ZIP_FILE="final_weights.zip"

echo "Downloading $ZIP_FILE..."
wget --no-check-certificate "$DOWNLOAD_URL" -O "$ZIP_FILE"

# Check if download was successful
if [ $? -ne 0 ]; then
    echo "Error: Download failed. Please check the permissions of the Google Drive link."
    exit 1
fi

echo "Extracting weights into $DEST_DIR/..."

unzip -o "$ZIP_FILE" -d "$DEST_DIR"

echo "Cleaning up temporary zip file..."
rm "$ZIP_FILE"

echo "Download and setup complete. The project is ready to run."