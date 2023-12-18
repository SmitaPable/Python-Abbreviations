# Python-Abbreviations
The Treename Abbreviation Program.
A Python programme that accepts a list of treenames, assigns letters scores depending on their location, and creates sensible abbreviations. Here's a explanation:
The programme uses a scoring method ('calculate_score_for_letter') that gives letters scores based on their placement in words, with specific emphasis given to the beginning and final letters.
'load_values_from_file' loads values (letter scores) from a file.
'process_line_and_clean' processes and cleans each line of treenames using regular expressions. Non-letter characters are eliminated and words are transformed to uppercase.
'generate_abbreviations_for_treename_list' generates abbreviations for each treename. It loops over treenames, investigating different places and generating unique abbreviations depending on established guidelines.
The programme manages data effectively with sets to ensure unique abbreviations and removes duplicates with'remove_duplicates_from_list'.

The main programme ('main_program') establishes file paths, loads values, processes treenames, creates abbreviations, scores are evaluated, and the results are printed. It enables future flexibility for expansions and improvements.

To summarise, the algorithm generates and evaluates treename abbreviations methodically using a scoring system, data processing, and efficient structures. The primary programme coordinates various components in order to create an effective solution.

Input file : trees.txt
Output file: pable_trees_abbrevs.txt
values : values.txt

