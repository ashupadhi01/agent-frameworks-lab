import asyncio
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool

from common.config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL
from common.prompts import RESEARCH_AGENT_INSTRUCTION
from common.mock_tools import web_search, web_fetch

web_search = function_tool(web_search)
web_fetch = function_tool(web_fetch)

# Disabling OpenAI tracing
set_tracing_disabled(True)

# Define LLM client
client = AsyncOpenAI(
    base_url = OPENROUTER_BASE_URL,
    api_key = OPENROUTER_API_KEY
)

agent = Agent(
    name = "Research Agent",
    instructions = RESEARCH_AGENT_INSTRUCTION,
    model = OpenAIChatCompletionsModel(
        model = "openrouter/free",
        openai_client = client
    ),
    tools = [web_search, web_fetch]
)

async def main() -> None:
    result = await Runner.run(agent, "Tell me something surprising about ancient life on Earth.")
    print(result.final_output)

if __name__ == "__main__":
    # asyncio.run(main())
    print(web_search("sqlite vs postgres"))
    print(web_fetch("https://example.com/sqlite-vs-postgres"))