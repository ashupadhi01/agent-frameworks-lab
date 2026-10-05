from tavily import TavilyClient
from common.config import TAVILY_API_KEY
from common.schemas import SearchResult
from pprint import pprint

# Initialising tavily_client
tavily_client = TavilyClient(api_key = TAVILY_API_KEY)

def web_search(query: str) -> list[SearchResult]:
    """Return up to 5 results as {title, url, snippet}, ranked by keyword overlap."""
    
    response = tavily_client.search(query)
    return [SearchResult(**result)for result in response["results"]]

# def web_fetch(url: str) -> str:
#     """Return the page text, or an 'ERROR: ...' string if the URL is unknown."""
#     ...



if __name__ == "__main__":
    pprint(web_search("Who won cricket world cup in recent times?"))

