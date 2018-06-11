from cx_Freeze import setup, Executable


base = None
executables = [Executable("slither.py", base=base)]
packages = ["pygame"]
options={"build_exe":{"packages":["pygame"], "include_files":["images/resizedimage.jpg",
"images/slitherintro.png","images/131-512.png","images/rsz_1snakehead.png", "images/rsz_apple.png",
"images/rsz_rock.png"]}}

setup(
    name = "Slither",
    options = options,
    #version = "VERSION_NUMBER e.g. 0.1",
    description = 'Slither Game',
    executables = executables
)
