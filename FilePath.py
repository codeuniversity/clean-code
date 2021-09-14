class FilePath:
   file_directory: str
   file_name: str

    def __init__(self, filepath):
        try:
            last_slash_index = filepath.rindex('/') + 1
            self.file_directory = filepath[:last_slash_index]
            self.file_name = filepath[last_slash_index:]
        except:
            self.file_directory = ''
            self.file_name = filepath

    def get_file_directory(self, filepath):
        return self.split_path(filepath)[0]

    def get_file_name(self, filepath):
        return self.split_path(filepath)[1]

    def get_file_extension_type(self, filepath):
        file_name = self.split_path(filepath)[1]
        try:
            last_dot_index = file_name.rindex('.')
            return file_name[last_dot_index + 1:]
        except:
            return ''


assert(FilePath("log/cups/access_log").file_directory == "log/cups/")
assert(FilePath("log/cups/access_log").file_name == "access_log")
assert(FilePath().get_file_directory("log/cups/access_log") == "log/cups/")
assert(FilePath().get_file_directory("log/cups/") == "log/cups/")
assert(FilePath().get_file_directory("cups/access_log") == "cups/")
assert(FilePath().get_file_directory("access_log") == "")
assert(FilePath().get_file_name("log/cups/access_log") == "access_log")
assert(FilePath().get_file_name("log/cups/") == "")
assert(FilePath().get_file_name("cups/access_log") == "access_log")
assert(FilePath().get_file_name("access_log") == "access_log")
assert(FilePath().get_file_extension_type("log/cups/access_log") == "")
assert(FilePath().get_file_extension_type("base/FileHelper.cpp") == "cpp")
assert(FilePath().get_file_extension_type("base/FileHelper.cpp.bak") == "bak")
