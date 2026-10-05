import asyncio
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool

from common.config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL, OPENROUTER_MODEL_ID
from common.prompts import RESEARCH_AGENT_INSTRUCTION
from common.schemas import ResearchReport
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
    handoff_description = "Doing deep research!",
    instructions = RESEARCH_AGENT_INSTRUCTION,
    model = OpenAIChatCompletionsModel(
        model = OPENROUTER_MODEL_ID,
        openai_client = client
    ),
    tools = [web_search, web_fetch],
    output_type = ResearchReport
)


async def main() -> None:
    result = await Runner.run(agent, "What are the main trade-offs between SQLite and PostgreSQL for a small web app?")

    print("-" * 50, "Final Output", "-" * 50)
    print(type(result.final_output), result.final_output)
    print("-" * 100)

    print("-" * 50, "Raw Responses", "-" * 50)
    print(type(result.raw_responses), result.raw_responses)
    print("-" * 100)

    # print("-" * 50, "Tool Call Arguments", "-" * 50)
    # from openai.types.responses import ResponseFunctionToolCall
    # import json

    # for item in result.output:
    #     if isinstance(item, ResponseFunctionToolCall):
    #         args = json.loads(item.arguments)
    #         print(args["query"])
    # print("-" * 100)



    print("-" * 50, "New Items", "-" * 50)
    print(type(result.new_items), result.new_items)
    print("-" * 100)


    # for item in result.new_items:
        # print(item)

if __name__ == "__main__":
    asyncio.run(main())
    # print(web_search("sqlite vs postgres"))
    # print(web_fetch("https://example.com/sqlite-vs-postgres"))