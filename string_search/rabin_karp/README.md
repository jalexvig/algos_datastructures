# Rabin Karp

Search for a pattern in a text.

1. Hash the pattern.
2. For each substring of text that has length pattern, hash it and compare the hash to the hashed pattern.
3. If the hash matches, confirm by checking the characters.

This is improved by using a rolling hash.

1. Hash each element of the pattern.
2. Shift each hash by increasing multiples of a base such that no information is lost when summed.
3. Sum.
4. Can mod this result to get it into a reasonable range.
5. Repeat this process for the first correct-length substring of text.
6. Do normal hash comparison followed by text comparison.
7. Update the text hash by adding in the hash of the next character and subtracting the hash of the first (shifted by a multiple of the base).

### Characteristics

* `m` = length of pattern
* `n` = length of search string

**Worst speed** : `O(m n)`
