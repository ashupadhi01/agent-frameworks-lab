# 01 Research Agent: spec

## Purpose
Answer a user's question by searching the web, choosing which pages to read, and producing a short, sourced report.

This spec is framework-agnostic. Every framework implementation is judged against it.

## Input
A single free-text question from the user.
Example: "What are the main trade-offs between SQLite and PostgreSQL for a small web app?"

## Tools
| Tool | Arguments | Returns |
|---|---|---|
| `web_search` | `query: str` | List of results: `title`, `url`, `snippet` |
| `web_fetch` | `url: str` | Full text content of the page (or an error if the URL is unknown/unreachable) |

Both tools are mocks backed by a fixed set of fake pages in `common/mock_tools.py`.

## Behavior
1. The agent reads the question and issues one or more `web_search` calls, using different phrasings of the question. It decides how many.
2. From the returned results, the agent decides which URLs are worth fetching. It may skip fetching if snippets are enough.
3. The agent calls `web_fetch` on the chosen URLs.
4. The agent may loop (new searches, more fetches) if it judges the information insufficient.
5. When satisfied, it stops calling tools and produces the final report.

The following are decided by the model at runtime, not by code:
- number and wording of searches
- which pages to fetch and how many
- when to stop

## Output
A structured report:
- `summary`: 3 to 5 sentences answering the question
- `key_points`: list of short strings
- `sources`: list of URLs actually used (must be URLs the agent fetched or saw in search results)

## Streaming
- Final answer text should stream to the user where the framework supports it.
- Optionally emit progress events for tool calls (e.g., "searching: ...", "fetching: ...").
- Streaming and structured output may conflict; note how each framework handles it.

## Error handling
- If `web_fetch` fails (unknown URL, timeout), the error is returned to the agent as a tool result so it can recover (try another URL or search again).
- If the structured output fails validation, observe what the framework does (retry, raise, return raw text).

## Mock data requirements
The fake web should contain, for each test question:
- at least 2 clearly relevant pages
- at least 1 irrelevant page that looks plausible from its title/snippet
- at least 1 page with outdated or misleading information
- at least 1 search result whose URL fails on fetch

This makes page-selection behavior visible.

## Test questions
1. A question answerable from a single page.
2. A question requiring information from two or more pages.
3. A question where the first search returns poor results and a reworded search is needed.
4. A question with no good answer in the fake web (agent should say so, not invent sources).

## Success criteria
- Uses more than one search phrasing on at least the multi-page question.
- Does not fetch obviously irrelevant pages.
- Sources in the report are all real URLs from the mock data.
- Recovers from the failing URL.
- Stops within a bounded number of steps (set a max, e.g., 10 tool calls).
- Report passes schema validation.

## What to observe (for NOTES.md)
- How tools are declared and how much boilerplate it takes
- What the framework sends to the model (raw prompt and tool schema)
- How tool errors surface back to the model
- How structured output is validated and what happens on failure
- How streaming behaves with tool calls and structured output