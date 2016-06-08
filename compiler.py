import py_compile, zipfile, os

WOTVersion = "0.9.15"

if os.path.exists("wotrc.zip"):
    os.remove("wotrc.zip")

py_compile.compile("src/__init__.py")
py_compile.compile("src/CameraNode.py")
py_compile.compile("src/wotrc.py")

fZip = zipfile.ZipFile("wotrc.zip", "w")
fZip.write("src/__init__.pyc", WOTVersion+"/scripts/client/mods/__init__.pyc")
fZip.write("src/wotrc.pyc", WOTVersion+"/scripts/client/mods/wotrc.pyc")
fZip.write("src/CameraNode.pyc", WOTVersion+"/scripts/client/CameraNode.pyc")
fZip.write("data/wotrc.json", WOTVersion+"/scripts/client/mods/wotrc.json")
fZip.close()
