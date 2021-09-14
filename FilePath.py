class FilePath:
    def __init__(self, filepath):
        try:
            last_slash_index = filepath.rindex('/') + 1
            self.file_directory = filepath[:last_slash_index]
            self.file_name = filepath[last_slash_index:]
        except:
            self.file_directory = ''
            self.file_name = filepath

    def get_file_directory(self):
        return self.file_directory

    def get_file_name(self):
        return self.file_name

    def get_file_extension_type(self):
        try:
            last_dot_index = self.file_name.rindex('.')
            return self.file_name[last_dot_index + 1:]
        except:
            return ''



assert(FilePath("log/cups/access_log").file_directory == "log/cups/")
assert(FilePath("log/cups/access_log").file_name == "access_log")
assert(FilePath("log/cups/access_log").get_file_directory() == "log/cups/")
assert(FilePath("log/cups/").get_file_directory() == "log/cups/")
assert(FilePath("cups/access_log").get_file_directory() == "cups/")
assert(FilePath("access_log").get_file_directory() == "")
assert(FilePath("log/cups/access_log").get_file_name() == "access_log")
assert(FilePath("log/cups/").get_file_name() == "")
assert(FilePath("cups/access_log").get_file_name() == "access_log")
assert(FilePath("access_log").get_file_name() == "access_log")
assert(FilePath("log/cups/access_log").get_file_extension_type() == "")
assert(FilePath("base/FileHelper.cpp").get_file_extension_type() == "cpp")
assert(FilePath("base/FileHelper.cpp.bak").get_file_extension_type() == "bak")
