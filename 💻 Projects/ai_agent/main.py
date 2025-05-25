import os
import chainlit as cl
from dotenv import load_dotenv
from typing import Optional, Dict
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.tool import function_tool
import requests

# Load environment variables
load_dotenv()


class AIAgent:
    def __init__(self):
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        self.provider = AsyncOpenAI(
            api_key=self.gemini_api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai",
        )
        self.model = OpenAIChatCompletionsModel(
            model="gemini-2.0-flash", openai_client=self.provider
        )
        self.agent = self.create_agent()

    @function_tool("get_rohma_info")
    def get_rohma_info() -> str:
        """
        Fetch information about Rohma Shabbir from the GitHub API
        """
        try:
            response = requests.get("https://api.github.com/users/rohmashabbir")
            if response.status_code == 200:
                return response.text
            else:
                return f"Error fetching data: Status code {response.status_code}"
        except Exception as e:
            return f"Error fetching data: {str(e)}"

    def create_agent(self) -> Agent:
        return Agent(
            name="Greeting Agent",
            instructions="""You are a Greeting Agent designed to provide friendly interactions and information about Rohma Shabbir.

1. Greet users warmly when they say hello (respond with 'Salam from Rohma Shabbir')
2. Say goodbye appropriately when users leave (respond with 'Allah Hafiz from Rohma Shabbir')
3. When users request information about Rohma Shabbir, use the get_rohma_info tool to retrieve and share his profile information
4. For any questions not related to greetings or Rohma Shabbir, politely explain: 'I'm only able to provide greetings and information about Rohma Shabbir. I can't answer other questions at this time.'

Always maintain a friendly, professional tone and ensure responses are helpful within your defined scope.""",
            model=self.model,
            tools=[self.get_rohma_info],
        )


# Create an instance of the AIAgent
ai_agent = AIAgent()

# OAuth callback (no changes)
@cl.oauth_callback
def oauth_callback(
    provider_id: str,
    token: str,
    raw_user_data: Dict[str, str],
    default_user: cl.User,
) -> Optional[cl.User]:
    print(f"Provider: {provider_id}")
    print(f"User data: {raw_user_data}")
    return default_user


# Handle new chat session
@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(content="Hello! How can I help you today?").send()


# Handle user messages
@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})

    result = await cl.make_async(Runner.run_sync)(ai_agent.agent, input=history)

    response_text = result.final_output
    await cl.Message(content=response_text).send()

    history.append({"role": "assistant", "content": response_text})
    cl.user_session.set("history", history)
