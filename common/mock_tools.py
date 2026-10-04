# Fake web: url -> page. Each page has a title, text, and keywords used by search.
FAKE_WEB = {
    "https://example.com/sqlite-vs-postgres": {
        "title": "SQLite vs PostgreSQL: choosing for small apps",
        "text": "...full article text...",
        "keywords": {"sqlite", "postgresql", "postgres", "small", "web", "app", "tradeoffs"},
    },
    "https://example.com/sqlite-history": {   # plausible but irrelevant
        "title": "A history of SQLite",
        "text": "...",
        "keywords": {"sqlite", "history", "origin"},
    },
    "https://example.com/db-2012": {          # outdated/misleading
        "title": "Why SQLite can't handle concurrent users",
        "text": "...claims that are no longer true...",
        "keywords": {"sqlite", "concurrent", "users", "web", "app"},
    },
    # a URL that appears in search results but is NOT in FAKE_WEB -> fetch fails
}

def web_search(query: str) -> list[dict]:
    """Return up to 5 results as {title, url, snippet}, ranked by keyword overlap."""
    ...

def web_fetch(url: str) -> str:
    """Return the page text, or an 'ERROR: ...' string if the URL is unknown."""
    ...

