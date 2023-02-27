# Nevermind

This code was written to be an equivalent of absurdle but for the game mastermind. Absurdle was designed in response to Wordle to make the player take the longest amount of guesses to guess the final word while having all the previous clues remain consistent.

Created Summer 2022

## Use

The `Nevermind.py` is standalone and contains the entire algorithm.

In mastermind, the colors are orange, yellow, green, pink, fuschia, and white. The code represents the colors as *o*, *y*, *g*, *p*, *f*, and *w* respectively.

The program prompts the codemaker to enter the codebreaker's guess, a permutation of 4 of the 6 colors awailable. It will then return list showing how many codes fall into the different categories of codemaker response using the white and red pins. It simply picks the bin containing the most amount of available codes that could still be considered valid and returns the necessary pins to allow the game to continue accordingly (the codemaker has red and white pins represented as *r* and *w*). 

The process continues until the codebreaker correctly guesses the only available valid code.

## Observations

The algorithm can extend Mastermind gameplay to at least 5 attempts from the codebreaker even against the most optimal of guesses.
