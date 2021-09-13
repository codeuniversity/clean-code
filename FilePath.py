import re


# Get the File path E.g. log/cups/
# sFile is the file path
def get_file_directory(filepath):
    if len(filepath) > 0 and filepath[len(filepath) - 1] == '/':
        return filepath

    try:
        last_slash_index = int(filepath.rindex('/'))
    except:
        last_slash_index = -1
    dirName = ''
    if last_slash_index >= 0:
        dirName = filepath[0: last_slash_index + 1]
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


assert(get_file_directory("log/cups/access_log") == "log/cups/")
assert(get_file_directory("log/cups/") == "log/cups/")
assert(get_file_directory("cups/access_log") == "cups/")
assert(get_file_directory("access_log") == "")
assert(get_file_name("log/cups/access_log") == "access_log")
assert(get_file_name("log/cups/") == "")
assert(get_file_name("cups/access_log") == "access_log")
assert(get_file_name("access_log") == "access_log")
assert(get_file_extension_type("log/cups/access_log") == "")
assert(get_file_extension_type("base/FileHelper.cpp") == "cpp")
assert(get_file_extension_type("base/FileHelper.cpp.bak") == "bak")
