# title.py - Manage title bar
import platform


def print_title(app_name, description, version, year,
                author, license_name, enable_color=True):
    if platform.system() == 'Windows':
        from colorama import init
        init()
    print(FormatTitle(app_name, description, version, enable_color))
    print(FormatCopyright(year, author, license_name, enable_color))


def FormatTitle(strAppName, strAppDescription, strVersion, blnColor):
    NoneColored = "{} - {} Version {}\n"
    Colored = "\033[1;33m{}\033[0;33m - {} \033[1;33mVersion {}\033[0m"
    strFormat = Colored if blnColor else NoneColored
    return strFormat.format(strAppName, strAppDescription, strVersion)


def FormatCopyright(strAppYear, strCopyright, strLicense, blnColor):
    NoneColored = "Copyright (c) {} {}, Licensed under {}\n\n"
    Colored = ("\033[0;33mCopyright (c) \033[1;33m{} \033[1;34m{}" +
               "\033[0;33m, Licensed under \033[1;33m{}\033[0m\n")
    strFormat = Colored if blnColor else NoneColored
    return strFormat.format(strAppYear, strCopyright, strLicense)
