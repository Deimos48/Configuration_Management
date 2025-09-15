class VirtualFileSystem:
    def __init__(self):
        # виртуальная "файловая система"
        self.cwd = "/"

    def listdir(self, path="."):
        # для простоты пока фиксированный список
        return ["file1.txt", "file2.txt", "dir1"]

    def chdir(self, path):
        if path == "/":
            self.cwd = "/"
        elif path == "..":
            self.cwd = "/"
        else:
            self.cwd = "/" + path

    def getcwd(self):
        return self.cwd
