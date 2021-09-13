def __split_path(filepath):
     try:
         last_slash_index = filepath.rindex('/') + 1
         file_directory = filepath[:last_slash_index]
         file_name = filepath[last_slash_index:]
         return file_directory, file_name
     except:
         return '', filepath


def get_file_directory(filepath):
    return __split_path(filepath)[0]


def get_file_name(filepath):
    return __split_path(filepath)[1]


def get_file_extension_type(filepath):
    try:
        last_dot_index = int(filepath.rindex('.'))
        return filepath[last_dot_index + 1:]
    except:
        return ''


assert(__split_path("log/cups/access_log")[0] == "log/cups/")
assert(__split_path("log/cups/access_log")[1] == "access_log")
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
