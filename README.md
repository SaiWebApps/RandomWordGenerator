# RandomWordGenerator
Python Library for Generating Random Words

## Usage
```
from randomwordgenerator import randomwordgenerator

num_words = 20
randomwordgenerator.generate_random_words(n = num_words)
```

Under the hood, the random word generator first tries to use the primary pathway.

### primary
Word Source: <a href="http://svnweb.freebsd.org/csrg/share/dict/words?view=co">FreeBSD Dictionary</a>

```
def get_n_random_words(num_random_words, prefix = None, suffix = None, substr = None):
	'''
		@param prefix
			- A character or phrase that all target words must start with
		@param suffix
			- A character or phrase that all target words must end with
		@param substr
			- A character or phrase that all target words must contain
		@param num_random_words
			- The number of random words to generate
			- Must be nonnegative
		@return 
			- a list of @num_random_words unique words from _URL that 
			meet the specified criteria
			- all words meeting the specified criteria if @num_random_words 
			exceeds the number of matching words
			- None if @num_random_words is < 0, [] if @num_random_words is 0
	'''
```

If the primary generator fails (a.k.a, we lose Internet connectivity, so we can't access the FreeBSD dictionary),
the random word generator switches over to the backup pathway.

### backup
```
def get_random_word(min_word_len, max_word_len):
    '''
        @param min_word_len 
            - Minimum number of characters that must be in random word
            - Must be non-negative
        
        @param max_word_len 
            - Maximum number of characters that can be in random word
            - Must be non-negative

        @return 
            - A random word whose length is >= @min_word_len and <= @max_word_len characters.
            - If any of the inputs are invalid, then raise an InvalidWordLengthBoundsError.
    '''
```

```
def get_n_random_words(n, word_len_bounds = (2, 10)):
    '''
        @param n
        (Required)
        Number of random words to generate

        @param word_len_bounds
        (Optional)
        Tuple containing the bounds for the word length of each randomly generated word;
        item 0 = minimum word length (2 by default), item 1 = maximum word length (10 by default)

        @return
            - A list with @n random words, where word_len_bounds[0] <= len(each word) <= word_len_bounds[1]
            - An InvalidWordLengthBoundsError if word_len_bounds is an invalid tuple (length < 2)
    '''
```

The key difference between the primary and backup pathways is that the latter might not generate actual words; it is
actually creating various strings of varying lengths and characters. Overall, the backup pathway is not as ideal as the
primary, but it is a suitable alternative in the event of a network failure.
