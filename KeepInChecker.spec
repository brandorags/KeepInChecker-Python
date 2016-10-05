# -*- mode: python -*-

import os


block_cipher = None

a = Analysis(['gui\\system_tray.py'],
             pathex=[os.getcwd()],
             binaries=None,
             datas=None,
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
          name='KeepInChecker.exe',
          debug=False,
          strip=False,
          upx=True,
          console=True )
		  
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='system_tray')
