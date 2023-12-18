import re

def calculate_score_for_letter(current_letter, position_in_word, is_last_letter, values):
    """
    Calculate the score for a given letter based on its position in a word and other criteria.
    """
    current_letter = current_letter.upper()  # Convert letter to uppercase
    
    if position_in_word == 1:
        return 0  # First letter of a word has score 0
    elif is_last_letter:
        if current_letter == 'E':
            return 20  # Last letter is 'E'
        else:
            return 5
    else:
        position_value = min(position_in_word - 1, 2)  # Position value scores (maximum of 2)
        return position_value + values.get(current_letter, 0)  # Used get to handle missing letters

def load_values_from_file(values_file):
    """
    Load values from a file and return them as a dictionary.
    """
    values = {}
    with open(values_file, 'r') as file:
        for line in file:
            letter, score = line.strip().split()
            values[letter] = int(score)
    return values

def process_line_and_clean(line):
    """
    Process a line by replacing apostrophes, removing non-letter characters, and converting to uppercase.
    """
    # Replace apostrophes with an empty string
    line = line.replace("'", "")
    
    # Remove sequences of non-letter characters
    line = re.sub(r'[^a-zA-Z\s]', '', line)
    
    # Split the line into words
    words = line.split()

    # Convert each word to uppercase
    words = [word.upper() for word in words]
    
    return words

def generate_abbreviations_for_treename_list(treename_list, values):
    """
    Generate abbreviations for a list of treenames based on specified rules.
    """
    abbreviations_list = []
    #Iterate over each treename in the list along with its index 'n'
    for n, treename in enumerate(treename_list):
        abbreviations_n = set()
        structured_treename = structure_treename(treename, n)
        #Iterate through positions in the structured treename, excluding the first and last positions
        for i in range(1, len(structured_treename) - 1):
            abbreviations_n.update(
                (
                    # Create an abbreviation by combining characters at specific positions and convert to uppercase
                    (structured_treename[0] + structured_treename[i] + structured_treename[j + 1]).upper(),
                    # Calculate the score for the abbreviation using the specified function
                    sum(calculate_score_for_letter(letter, idx + 1, idx == len(structured_treename) - 2, values) 
                        for idx, letter in enumerate(structured_treename[0] + structured_treename[i] + structured_treename[j + 1]))
                )
                for j in range(i, len(structured_treename) - 1)
                # Filter abbreviations based on length and alphabetic characters
                if len(structured_treename[0] + structured_treename[i] + structured_treename[j + 1]) == 3
                and (structured_treename[0] + structured_treename[i] + structured_treename[j + 1]).isalpha()
            )

        abbreviations_list.append(abbreviations_n)

    return abbreviations_list

def structure_treename(treename, n):
   
    return treename

def remove_duplicates_from_list(abbreviations):
    """
    Remove duplicates from a list of abbreviations.
    """
    unique_abbreviations = set(abbreviations)
    return list(unique_abbreviations)

def process_file_and_print(file_path, values):
    """
    Process a file, generate abbreviations, and print the results.
    """
    with open(file_path, 'r') as file:
        treename_list = [line.strip() for line in file]

        # Generate abbreviations using the logic from generate_abbreviations
        abbreviations_list = generate_abbreviations_for_treename_list(treename_list, values)

        for i, line in enumerate(treename_list):
            # Print the line, list of abbreviations, and their scores
            print(line)
            best_score = float('inf')
            best_abbreviations = set()
            
            for abbreviation, score in sorted(abbreviations_list[i], key=lambda x: x[1]):
                if score < best_score:
                    best_score = score
                    best_abbreviations = {abbreviation}
                elif score == best_score:
                    best_abbreviations.add(abbreviation)
                else:
                    break  # Abbreviations are sorted, so no need to check further
                    
            if best_abbreviations:
                print(f"{' '.join(best_abbreviations)}")
            else:
                print("") #blank line for names which has no acceptable abbreviation 
            print()

def main_program():
    """
    Main program to execute the abbreviation generation and printing.
    """
    # Get file path and values file from user input
    file_path = r"C:\Users\DELL\Desktop\Sem1\Sem1\Programming language\Python\2543320Python1\trees.txt"
    values_file = r"C:\Users\DELL\Desktop\Sem1\Sem1\Programming language\Python\2543320Python1\values.txt"    
    # Load values from the file
    values = load_values_from_file(values_file)
    
    # Process the file
    process_file_and_print(file_path, values)

if __name__ == "__main__":
    main_program()
