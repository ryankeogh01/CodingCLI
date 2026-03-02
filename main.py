import asyncio
from chat_session import chat_loop

async def main():
    session = await chat_loop()

if __name__ == "__main__":
    import sys
    asyncio.run(main())