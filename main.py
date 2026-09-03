"""TextHack text analytics system with three query categories."""

ARTICLES = [
    "Python is widely used for Data Science and Machine Learning.",
    "Machine Learning is an important area of Artificial Intelligence.",
    "Text Analytics helps in processing and analysing textual data.",
    "Python programming is useful for Artificial Intelligence applications.",
    "Data Science uses statistics, programming and Machine Learning.",
]

QUERY_CATEGORIES = {
    1: "Single Keyword Search",
    2: "Multi-Keyword Search",
    3: "Exact Phrase Search",
}


def search_articles(choice: int, query: str, articles: list[str] = ARTICLES) -> list[int]:
    """Return zero-based indexes of articles matching the selected query."""
    normalized_query = query.strip().lower()
    if not normalized_query or choice not in QUERY_CATEGORIES:
        return []

    if choice == 2:
        terms = normalized_query.split()
        return [
            index
            for index, article in enumerate(articles)
            if all(term in article.lower() for term in terms)
        ]

    return [
        index
        for index, article in enumerate(articles)
        if normalized_query in article.lower()
    ]


def display_repository(articles: list[str] = ARTICLES) -> None:
    """Display all articles in the repository."""
    print("========== TEXT HACK ARTICLE REPOSITORY ==========")
    for index, article in enumerate(articles, start=1):
        print(f"Article {index}: {article}")


def display_categories() -> None:
    """Display the query categories available to the user."""
    print("\n========== QUERY CATEGORIES ==========")
    for number, category in QUERY_CATEGORIES.items():
        print(f"{number}. {category}")


def main() -> None:
    display_repository()
    display_categories()

    try:
        choice = int(input("\nEnter your choice (1-3): "))
    except ValueError:
        print("\nInvalid choice!")
        return

    if choice not in QUERY_CATEGORIES:
        print("\nInvalid choice!")
        return

    query = input("Enter your search query: ")
    matches = search_articles(choice, query)

    print("\n========== SEARCH RESULTS ==========")
    for index in matches:
        print(f"\nArticle {index + 1}: {ARTICLES[index]}")

    if not matches:
        print("\nNo matching articles found.")


if __name__ == "__main__":
    main()
