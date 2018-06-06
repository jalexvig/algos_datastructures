# Aho-Corasick

Search for a pattern in a string.

1. Recursively determine longest matching pattern prefix (fail state) at every position of pattern.
2. Create DFA using fail state lookups when characters don't match.

### Characteristics

* `m` = length of pattern -- O(m) incurred when building fail state array
* `n` = length of search string

**Worst speed** : `O(m + n)`

### See also

* This is [Aho-Corasick](https://github.com/jalexvig/learn_algos/tree/master/string_search/aho_corasick) with only one pattern
