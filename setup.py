import sys
from distutils.core import setup

if sys.platform == "darwin":
    import py2app

    options = {"py2app": {"optimize": 2,
                          "dist_dir": "dist",
                          "xref": False,
                          "strip": True,
                          "argv_emulation": True,
                          "site_packages": True,
                          "arch": "i386",
                          "iconfile": "anidl.icns",
                          "resources": ["anidl.ico"],
                          "plist": {"CFBundleName": "anidl",
                                    "CFBundleShortVersionString":"1.0.0",
                                    "CFBundleVersion": "1.0.0",
                                    "CFBundleDevelopmentRegion": "English"}}}

    args = {"app": ["anidl.py"], "options": options}
elif sys.platform == "win32":
    import py2exe

    includes = []
    excludes = ["_gtkagg", "_tkagg", "bsddb", "curses", "email", "pywin.debugger",
                "pywin.debugger.dbgcon", "pywin.dialogs", "tcl", "Tkconstants", "Tkinter"]

    packages = []
    for dbmodule in ["dbhash", "gdbm", "dbm", "dumbdbm"]:
        try:
            __import__(dbmodule)
        except ImportError:
            pass
        else:
             # If we found the module, ensure it"s copied to the build directory.
            packages.append(dbmodule)

    dll_excludes = ["libgdk-win32-2.0-0.dll", "libgobject-2.0-0.dll", "tcl84.dll", "tk84.dll", "w9xpopen.exe"]

    options = {"py2exe": {"compressed": 2,
                          "optimize": 2,
                          "includes": includes,
                          "excludes": excludes,
                          "packages": packages,
                          "dll_excludes": dll_excludes,
                          "bundle_files": 1,
                          "dist_dir": "dist",
                          "xref": False,
                          "skip_archive": False,
                          "ascii": False,
                          "custom_boot_script": ""}}

    args = {"windows": [{"script": "anidl.py", "icon_resources": [(1, "anidl.ico")]}],
            "zipfile": None,
            "options": options}
else:
    args = {"scripts": ["anidl.py"]}

setup(name="anidl", **args)
