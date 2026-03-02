from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from crud import Operations
from tools import tools

load_dotenv()
oper = Operations()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

async def run_agent(user_message: str):
    config = types.GenerateContentConfig(
        tools=[tools],
        system_instruction="You are a coding assistant. Be concise dont give big explanations, just show fixed solutions"                                 
    )


    contents = [
        types.Content(
            role="user", parts=[types.Part(text=user_message)]
        )
    ]

    while True:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=contents,
            config=config
        )
        tool_call = response.candidates[0].content.parts[0]
        if tool_call.function_call:
            if tool_call.function_call.name == "read_file":
                result = oper.read_file(**dict(tool_call.function_call.args))
            elif tool_call.function_call.name == "write_file":
                result = oper.write_file(**dict(tool_call.function_call.args))
            elif tool_call.function_call.name == "list_directory":
                result = oper.list_directory(**dict(tool_call.function_call.args))

            function_response_part = types.Part.from_function_response(
                name=tool_call.function_call.name,
                response={"response": result}
            )
            contents.append(response.candidates[0].content)
            contents.append(types.Content(role="user", parts=[function_response_part]))
        else:
            print(response.text)
            break