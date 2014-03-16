import py_compile, zipfile, os

WOTVersion = "0.8.11"

if os.path.exists("randcamo.zip"):
    os.remove("randcamo.zip")

py_compile.compile("src/__init__.py")
py_compile.compile("src/CameraNode.py")
py_compile.compile("src/randcamo.py")

fZip = zipfile.ZipFile("randcamo.zip", "w")
fZip.write("src/__init__.pyc", WOTVersion+"/scripts/client/mods/__init__.pyc")
fZip.write("src/randcamo.pyc", WOTVersion+"/scripts/client/mods/randcamo.pyc")
fZip.write("src/CameraNode.pyc", WOTVersion+"/scripts/client/CameraNode.pyc")
fZip.close()
