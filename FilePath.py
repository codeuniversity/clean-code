import re


# Get the File path E.g. log/cups/
# sFile is the file path
def get_file_path(sFile):
    if len(sFile) > 0 and sFile[len(sFile) - 1] == '/':
        return sFile

    try:
        last_slash_index = int(sFile.rindex('/'))
    except:
        last_slash_index = -1
    dirName = ''
    if last_slash_index >= 0:
        dirName = sFile[0: last_slash_index + 1]
    else:
        dirName = '' #sFilename

    return dirName


def get_file_name(sFilename):
    try:
        int(sFilename.rindex('/'))
    except:
        return sFilename

    pos = sFilename.rindex('/')
    base_name = sFilename[pos + 1:]
    return base_name


def get_file_extension_type(sFilename):
    try:
        occurrences = [m.start() for m in re.finditer('\.', sFilename)]
        return sFilename[occurrences[-1] + 1:]
    except:
        pass

    return ''


assert(get_file_path("log/cups/access_log") == "log/cups/")
assert(get_file_path("log/cups/") == "log/cups/")
assert(get_file_path("cups/access_log") == "cups/")
assert(get_file_path("access_log") == "")
assert(get_file_name("log/cups/access_log") == "access_log")
assert(get_file_name("log/cups/") == "")
assert(get_file_name("cups/access_log") == "access_log")
assert(get_file_name("access_log") == "access_log")
assert(get_file_extension_type("log/cups/access_log") == "")
assert(get_file_extension_type("base/FileHelper.cpp") == "cpp")
assert(get_file_extension_type("base/FileHelper.cpp.bak") == "bak")
