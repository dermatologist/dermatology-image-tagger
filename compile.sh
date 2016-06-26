
rm -rf build
rm -rf dist
pyinstaller --windowed --icon=dit_icon.ico --name DermTagger DITagger/dit.py