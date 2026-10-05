"""Fake web + mock tools for the research agent.

Random (unseeded) so runs vary; the dead link appears in ~1 in 3 searches
to exercise the agent's error-recovery path.
"""

import random

from common.schemas import SearchResult

# url -> page. web_search ignores the query and samples pages randomly.
FAKE_WEB: dict[str, dict] = {
    # clearly relevant
    "https://example.com/sqlite-vs-postgres": {
        "title": "SQLite vs PostgreSQL: choosing for small apps",
        "text": (
            "SQLite is embedded and needs no server, making deployment trivial "
            "for small apps. PostgreSQL offers richer types, concurrency, and "
            "extensions, at the cost of running a service. For a small web app "
            "with a single writer, SQLite is often enough; multi-user writes "
            "favor PostgreSQL."
        ),
    },
    # plausible but irrelevant
    "https://example.com/sqlite-history": {
        "title": "A history of SQLite",
        "text": "SQLite was created in 2000 by D. Richard Hipp for a naval project.",
    },
    # outdated / misleading
    "https://example.com/db-2012": {
        "title": "Why SQLite can't handle concurrent users",
        "text": (
            "SQLite locks the whole database on writes, so it cannot serve "
            "concurrent web users. Any web app with more than one user needs "
            "a client-server database."
        ),
    },
    # second relevant page (for the multi-page test question)
    "https://example.com/postgres-ops": {
        "title": "Operating PostgreSQL on small servers",
        "text": (
            "PostgreSQL needs memory tuning, backups, and upgrades. On tiny "
            "servers this overhead dominates; managed Postgres removes it for "
            "a monthly cost."
        ),
    },
    # listed in search results ~1 in 3 searches, but fetching it fails
    "https://example.com/dead-link": {
        "title": "Complete database comparison guide",
        "text": "",  # never fetched
    },
}

FAILING_URL = "https://example.com/dead-link"

_rng = random.Random()


def web_search(query: str) -> list[SearchResult]:
    """Return 2 random pages; the dead link is appended ~1 in 3 searches."""
    urls = _rng.sample([u for u in FAKE_WEB if u != FAILING_URL], 2)
    if _rng.random() < 1 / 3:
        urls.append(FAILING_URL)
    return [
        SearchResult(title=FAKE_WEB[u]["title"], url=u, content=FAKE_WEB[u]["text"])
        for u in urls
    ]


def web_fetch(url: str) -> str:
    """Return the page text; the dead link and unknown URLs both fail."""
    if url == FAILING_URL:
        return f"ERROR: could not fetch {url}"
    page = FAKE_WEB.get(url)
    if page is None:
        return f"ERROR: unknown URL {url}"
    return page["text"]


if __name__ == "__main__":
    from pprint import pprint

    # pprint(web_search("sqlite vs postgresql for a small web app"))
    print(web_fetch("https://example.com/dead-link"))
    # print(web_fetch("https://example.com/does-not-exist"))
