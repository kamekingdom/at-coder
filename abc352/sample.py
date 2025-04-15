import os

def get_multiline_input(prompt):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    return '\n'.join(lines)

def create_or_update_files(directory):
    # フォルダが存在しない場合は作成
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # 指定されたファイル名でファイルを生成または書き換え
    filenames = [
        "input1.txt", "input2.txt", "input3.txt",
        "answer1.txt", "answer2.txt", "answer3.txt"
    ]
    
    for filename in filenames:
        # フォルダ内のファイルへのパス
        file_path = os.path.join(directory, filename)
        # ファイルが存在しない場合、または内容をリセットする
        with open(file_path, 'w') as file:
            file.write('')  # 新しくファイルを作る場合は空の内容で作成

def main():
    # ユーザーからディレクトリ名を入力
    dir_name = input('Problem : ')[0].lower()
    
    # ファイルを生成または更新
    create_or_update_files(dir_name)

    for i in range(1, 4):  # 3セットの入力と回答を求める
        # ユーザーに複数行の入力を求める
        user_input = get_multiline_input(f'Input {i} (空行で終了):')
        user_answer = get_multiline_input(f'Answer {i} (空行で終了):')
        
        # 入力値をファイルに書き込む
        with open(os.path.join(dir_name, f'input{i}.txt'), 'w') as input_file:
            input_file.write(user_input)
        
        # 回答をファイルに書き込む
        with open(os.path.join(dir_name, f'answer{i}.txt'), 'w') as answer_file:
            answer_file.write(user_answer)

if __name__ == "__main__":
    main()
