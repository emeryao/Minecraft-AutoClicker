#!/bin/env sh

python -m PyInstaller --specpath ./dist --distpath ./dist --workpath ./build --clean -F ./src/clicker.py -i ../assets/right-click.ico
