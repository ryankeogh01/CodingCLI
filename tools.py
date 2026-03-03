from google.genai import types

read_file_function = {
    "name": "read_file",
    "description": "Read a file from the users directory for a given file name",
    "parameters": {
        "type": "object",
        "properties": {
            "file_name": {
                "type": "string",
                "description": "File name to read e.g app.py"
            }
        },
        "required": ["file_name"]

    }
}

write_file_function = {
    "name": "write_file",
    "description": "Write code and bug fixes to files given the name",
    "parameters": {
        "type": "object",
        "properties": {
            "file_name": {
                "type": "string",
                "description": "File Name of where to write code to e.g app.py"
            },
            "content": {
                "type": "string",
                "description": "The code that is to be written"
            }
        },
        "required": ["file_name"]

    }
}

list_directory_funtion = {
    "name": "list_directory",
    "description": "List the directories at current path",
    "parameters": {
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
                "description": "List the directories at the current path"
            }
        },
        "required": ["path"]
    }
}

run_command_function = {
    "name": "run_command",
    "description": "Run a command in the terminal",
    "parameters": {
        "type": "object",
        "properties": {
            "command": {
                "type": "string",
                "description": "The command to be run"
            },
        },
        "required": ["command"]
    }
}

tools = types.Tool(function_declarations=[read_file_function, write_file_function, list_directory_funtion, run_command_function])
