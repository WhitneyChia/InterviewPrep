"""
Search functionality:

Min 2 letters before start searching.
As a customer starts entering in a search string, return likely matches. At most return 3, if greater than 3,
sort alphabetically.

You start returning once there are two letters entered.

Return a list of lists representing the search results as you go

Example:
    Input:
    repository = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    customerQuery = "mouse"

    Ouput:
    "mo" -> ["mobile", "moneypot", "monitor"]
    "mou" -> ["mouse", "mousepad"]
    "mous" -> ["mouse", "mousepad"]
    "mouse" -> ["mouse", "mousepad"]

This is the very brute force way right now, very slow.
1. We are iterating through the list multiple times for every letter
2. We are sorting the results every time for every letter
3. Edge case is going to be casing, want case insensitive
    This solution is lowering on the compare and on the sorting, no good.

This is probably the use case for a trie, or a heap?
Heap will be tough to make work, probably trie
"""


def searchSuggestions(repository, customerQuery):
    if len(customerQuery) < 2:
        return None

    overall_query_results = []
    i = 2

    while i < len(customerQuery) + 1:
        query_results = []
        for word in repository:
            if word[0: i].lower() == customerQuery[0:i].lower():
                query_results.append(word)
        overall_query_results.append(sortWords(query_results))
        i += 1

    return overall_query_results


def sortWords(search_results: list):
    search_results = [x.lower() for x in search_results]
    key_words = sorted(search_results)
    return key_words[0:3]

# if __name__ == "__main__":

    # Make up some test cases
