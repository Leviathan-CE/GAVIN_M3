# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['gavin_m3.py'],
    pathex=['/Users/LeviM/Desktop/GAVIN_M3', '/Users/LeviM/Desktop/Files/Dev/Projects/GAVIN_M3'],
    binaries=[],
    datas=[],
    hiddenimports=['src'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='gavin_m3',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    onefile = True,
)
