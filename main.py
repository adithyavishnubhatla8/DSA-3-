def compute_lps(pattern: str) -> list[int]:
    """Compute the Longest Prefix Suffix (LPS) array for KMP."""
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text: str, pattern: str) -> tuple[bool, list[int]]:
    """Search for pattern in text using KMP and return match status plus LPS array."""
    if pattern == "":
        return True, []

    lower_text = text.lower()
    lower_pattern = pattern.lower()
    lps = compute_lps(lower_pattern)
    i = 0
    j = 0

    while i < len(lower_text):
        if lower_text[i] == lower_pattern[j]:
            i += 1
            j += 1

            if j == len(lower_pattern):
                return True, lps
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return False, lps


if __name__ == "__main__":
    try:
        with open("Sample.txt", "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print("Error: Sample.txt not found.")
    else:
        print("-----File Content-----")
        print(text)
        pattern = input("\nEnter the word to search: ")
        found, lps = kmp_search(text, pattern)

        print("\nPattern LPS array:", lps)
        if found:
            print("\n✅ Pattern Found")
        else:
            print("\n❌ Pattern Not Found") 