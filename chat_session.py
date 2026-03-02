from agent import run_agent

async def chat_loop():
    """This runs an interactive chat loop with the user"""
    print("\n Welcome to CodingCLI")
    print("\n type exit to quit")

    while True:
        try:
            user_message = input("\nQuery: ").strip()

            if user_message.lower() == 'exit':
                break

            response = run_agent(user_message)
            print("\n" + str(response))
            
        except Exception as e:
            print(f"\nError: {str(e)}")