from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from crud import Operations
from tools import tools

load_dotenv()
oper = Operations()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_INSTRUCTION = "You are a coding assistant. Be concise dont give big explanations, just show fixed solutions and if running commnds keep explanations short"
MODEL_NAME = "gemini-2.5-flash"
CONFIRM_WRITE_MESSAGE = "Allow me to write to file {file_name} - allow? (y/n): "
USER_REJECTED_WRITE = "User rejected the write action"
TOOL_NOT_FOUND = "Tool not Found"
CONFIRM_NEEDED= {"run_command", "write_file"}

contents = []
tool_map = {
    "read_file": oper.read_file,
    "write_file": oper.write_file,
    "list_directory": oper.list_directory,
    "run_command" : oper.run_command
}

config = types.GenerateContentConfig(
    tools=[tools],
    system_instruction=SYSTEM_INSTRUCTION                                 
)

def run_agent(user_message: str):
    contents.append(types.Content(role="user", parts=[types.Part(text=user_message)]))
    while True:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=contents,
            config=config
        )
        hasTool = False
        contents.append(response.candidates[0].content)

        for part in response.candidates[0].content.parts:
            if part.function_call:
                hasTool = True
                tool_name = part.function_call.name
                tool_args = dict(part.function_call.args)

                if tool_name in CONFIRM_NEEDED:
                    confirm = input(f"Agent wants to run {tool_name} with {tool_args} - allow? y/n ")

                    if confirm == 'y':
                        result = tool_map[tool_name](**tool_args)
                    else:
                        result = USER_REJECTED_WRITE
                elif tool_name in tool_map:
                    result = tool_map[tool_name](**tool_args)
                else:
                    result = TOOL_NOT_FOUND

                function_response_part = types.Part.from_function_response(
                    name=tool_name,
                    response={"response": result}
                )
                contents.append(types.Content(role="user", parts=[function_response_part]))
        if not hasTool:
            return response.text    