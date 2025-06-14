import re
print("Name: Rahul G \n USN:1AY24AI088\n Section: 'O'")
def mad_libs(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        text = file.read()
    placeholders = re.findall(r'\b(ADJECTIVE|NOUN|VERB|ADVERB)\b', text)
    replacements = []
    for word in placeholders:
        article = 'an' if word[0] in 'AEIOU' else 'a'
        user_input = input(f"Enter {article} {word.lower()}: ")
        replacements.append(user_input)
    def replace_match(match):
        return replacements.pop(0)

    result_text = re.sub(r'\b(ADJECTIVE|NOUN|VERB|ADVERB)\b', replace_match, text)
    print("\n--- Final Story ---\n")
    print(result_text)
    with open(output_filename, 'w') as file:
        file.write(result_text)
    print(f"\nStory saved to '{output_filename}'")
if __name__ == "__main__":
    mad_libs('madlibs_input.txt', 'madlibs_output.txt')
