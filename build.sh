#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo "[~] Updating and installing dependencies..."
pacman -Syu --noconfirm
pacman -S radare2 --noconfirm
echo "Radare2 installed successfully"
