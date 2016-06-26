# -*- mode: python -*-

block_cipher = None


a = Analysis(['DITagger/dit.py'],
             pathex=['/home/beapen/PycharmProjects/DITagger'],
             binaries=None,
             datas=[('settings.ini','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='DermTagger',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='dit_icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='DermTagger')
