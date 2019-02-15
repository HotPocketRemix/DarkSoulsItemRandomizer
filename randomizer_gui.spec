# -*- mode: python -*-

block_cipher = None


a = Analysis(['randomizer_gui.py'],
             pathex=['C:\\Users\\ekrechmer\\DarkSoulsItemRandomizer'],
             binaries=[],
             datas=[('favicon.ico', '.'), ('favicon.gif', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='DarkSoulsItemRandomizer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='favicon.ico')

import shutil
shutil.copyfile('randomizer.ini', '{0}/randomizer.ini'.format(DISTPATH))
