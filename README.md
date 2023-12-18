SMITA SANJAY PABLE

**The Tree name Abbreviation Program.**
This assignment consists of a Python 3 programming, where The task is to read a file containing a list of names of some kind, and generate three-letter abbreviations for each of these objects satisfying certain rules,
The abbreviations consists of entirely upper case letters, Apostrophes (') are ignored completely and any abbreviation which can be formed from more than one name on the list is excluded.
This Python programme that accepts a list of tree names from treenames.txt, assigns letters scores from (values.txt) depending on their location , and creates sensible abbreviations. Here's an explanation:
The programme uses a scoring method ('calculate_score_for_letter') that gives letters scores based on their placement in words, with specific emphasis given to the beginning and final letters.
'load_values_from_file' loads values (letter scores) from a file.
'process_line_and_clean' processes and cleans each line of treenames using regular expressions. Non-letter characters are eliminated and words are transformed to uppercase.
'generate_abbreviations_for_treename_list' generates abbreviations for each treename. It loops over treenames, investigating different places and generating unique abbreviations depending on established guidelines.
The programme manages data effectively with sets to ensure unique abbreviations and removes duplicates with'remove_duplicates_from_list'.
The main programme ('main_program') establishes file paths, loads values, processes treenames, creates abbreviations, scores are evaluated, and the results are printed. It enables future flexibility for expansions and improvements.

To summarise, the algorithm generates and evaluates treename abbreviations methodically using a scoring system, data processing, and efficient structures. The primary programme coordinates various components in order to create an effective solution.

Input file : trees.txt
values : values.txt
Output file: pable_trees_abbrevs.txt
