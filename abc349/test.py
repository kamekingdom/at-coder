import difflib

def highlight_differences(correct_text, incorrect_text):
    # ANSI escape codes for highlighting
    RED = '\033[91m'   # Red text for differences
    BLUE = '\033[94m'  # Blue text for similarities
    RESET = '\033[0m'  # Reset to default

    # Prepare the highlighted result
    result = []
    # Use SequenceMatcher to compare the texts
    s = difflib.SequenceMatcher(None, correct_text, incorrect_text)
    for tag, i1, i2, j1, j2 in s.get_opcodes():
        if tag == 'replace':
            result.append(RED + incorrect_text[j1:j2] + RESET)
        elif tag == 'delete':
            # Do not include deleted parts in the result
            continue
        elif tag == 'insert':
            result.append(RED + incorrect_text[j1:j2] + RESET)
        elif tag == 'equal':
            result.append(BLUE + incorrect_text[j1:j2] + RESET)

    return ''.join(result)

# Example usage
correct_text = "こんにちは\nおはよう\nこんばんは"
incorrect_text = "こんにちは\nおやすみ\nこんばんわ"

highlighted_diff = highlight_differences(correct_text, incorrect_text)
print(highlighted_diff)
