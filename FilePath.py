import re


def get_file_directory(filepath):
    try:
        last_slash_index = int(filepath.rindex('/'))
        return filepath[0: last_slash_index + 1]
    except:
        return ''


def get_file_name(filepath):
    try:
        last_slash_index = int(filepath.rindex('/'))
        return filepath[last_slash_index + 1:]
    except:
        return filepath


def get_file_extension_type(filepath):
    try:
        occurrences = [m.start() for m in re.finditer('\.', filepath)]
        return filepath[occurrences[-1] + 1:]
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
