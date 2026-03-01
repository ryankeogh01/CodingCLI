import os
import subprocess

class Operations: 
    def __init__(self):
        self.cwd = os.getcwd()

    def read_file(self, file_name: str):
        """Reads the file at the given file name"""
        full_path = os.path.join(self.cwd, file_name)
        with open(full_path, "r") as f:
            return f.read()

    def write_file(self, file_name: str, content: str):
        """Writes content to the file at the given path"""
        full_path = os.path.join(self.cwd, file_name)
        with open(full_path, "w") as f:
            return f.write(content)

    def run_command(self, path, command):
        nav = subprocess.run("cd ", path)
        com = subprocess.run(command, shell=True, capture_output = True, text=True)
        return com.stdout + com.stderr

    def list_directory(self, path="."):
        return os.listdir(path)

    