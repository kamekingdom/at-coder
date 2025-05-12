import sys
import subprocess
from colorama import Fore, Style, init
import time
import difflib  # Import difflib to compare and highlight differences
import datetime
import pyperclip

def main():
    problem_file = input("Problem : ").lower()
    problem_name = problem_file + ".py"
    problem_file = list(problem_file)[0]

    init()  # Initialize colorama
    ac_counter = 0

    for i in range(1, 4):
        input_file_name = f"./{problem_file}/input{i}.txt"
        answer_file_name = f"./{problem_file}/answer{i}.txt"
        sample_number = f"#sample{i}"

        try:
            start_time = time.time()  # Start the timer here to ensure timing is always reported

            with open(input_file_name, 'r', encoding='utf-8') as infile:
                input_content = infile.read().strip()
                if input_content == '':
                    print(f"{Fore.YELLOW}{sample_number}[NI]{Style.RESET_ALL}", end=" ")
                    print("-- No Input File.")
                    ac_counter += 1
                    continue

        except FileNotFoundError:
            print(f"{Fore.YELLOW}{sample_number}[FN]{Style.RESET_ALL}", end=" ")
            print("-- File not found.")
            continue
        except UnicodeDecodeError as e:
            execution_time = time.time() - start_time
            print(f"{Fore.RED}{sample_number}[RE]{Style.RESET_ALL}", end=" ")
            print(f" -- {execution_time:.3f} sec Error: {str(e)}")
            continue

        command = f'powershell -Command "Get-Content {input_file_name} | C:/Users/yudai/AppData/Local/Programs/Python/Python310/python.exe {problem_name}"'
        result = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        execution_time = time.time() - start_time  # Calculate the execution time

        if result.returncode != 0:
            error_message = result.stderr.strip() if result.stderr else "Unknown error."
            print(f"{Fore.RED}{sample_number}[RE]{Style.RESET_ALL}", end=" ")
            print(f"-- {execution_time:.3f} sec\n{error_message}")
            continue

        try:
            with open(answer_file_name, 'r', encoding='utf-8') as answerfile:
                expected_answer = answerfile.read().strip()
        except FileNotFoundError:
            print(f"{Fore.YELLOW}{sample_number}[NA]{Style.RESET_ALL} -- No Answer File.")
            continue

        actual_output = result.stdout.strip()
        if actual_output == expected_answer:
            print(f"{Fore.GREEN}{sample_number}[AC]{Style.RESET_ALL}", end="")
            print(f" -- {execution_time:.3f} sec")
            ac_counter += 1
        else:
            diff_output = highlight_differences(expected_answer, actual_output)
            if execution_time > 2.0:
                print(f"{Fore.YELLOW}{sample_number}[TLE]{Style.RESET_ALL}", end="")
            else:
                print(f"{Fore.RED}{sample_number}[WA]{Style.RESET_ALL}", end="")
            print(f" -- {execution_time:.3f} sec")
            print(f"[[Input]]\n{input_content}")
            print(f"[[Output]]\n{diff_output}")
            print(f"[[Expected]]\n{Fore.GREEN}{expected_answer}{Style.RESET_ALL}\n")
        
    if ac_counter == 3:
        current_time = datetime.datetime.now()
        print(f"\n[[ALL ACCEPTED]]")
        print(f"{Fore.GREEN}{current_time.strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}",end="")
        try:
            with open(problem_name, "r", encoding="utf-8") as file:
                content = file.read()
            pyperclip.copy(content)
            print(f"{Fore.BLUE} [Copied!]{Style.RESET_ALL}")
        except:
            print(f"{Fore.RED} [Error: Couldn't copy]{Style.RESET_ALL}")

import difflib

def highlight_differences(correct_text, incorrect_text):
    result = []
    s = difflib.SequenceMatcher(None, correct_text, incorrect_text)
    for tag, i1, i2, j1, j2 in s.get_opcodes():
        if tag == 'replace':
            result.append(f"{Fore.RED}{incorrect_text[j1:j2]}{Style.RESET_ALL}")
        elif tag == 'delete':
            continue
        elif tag == 'insert':
            result.append(f"{Fore.RED}{incorrect_text[j1:j2]}{Style.RESET_ALL}")
        elif tag == 'equal':
            result.append(f"{Fore.GREEN}{incorrect_text[j1:j2]}{Style.RESET_ALL}")

    return ''.join(result)

if __name__ == "__main__":
    main()
