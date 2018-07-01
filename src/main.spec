# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py', 'decode_encode.py', 'MyWindow.py', 'ui_MyWindow.py', 'ui_selectcard.py', 'data.py'],
             pathex=['G:\\python-projects\\GodSlayTheSpire\\src'],
             binaries=[],
             datas=[('cards_sorted.json', '.'), ('relics.json', '.'), ('potions.json', '.')],
             hiddenimports=['queue'],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='cute.ico')
