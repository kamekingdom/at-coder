import sys
import subprocess

def main():
    if len(sys.argv) != 3:
        print("Usage: python atcoder.py <script_name> <input_file_name>")
        sys.exit(1)
    
    script_name = sys.argv[1] + '.py'
    input_file_name = "input" + sys.argv[2] + '.txt'
    
    # Windowsの場合
    command = f'Get-Content .\\{input_file_name} | C:/Python312/python.exe ./{script_name}'
    command = f'powershell -Command "Get-Content {input_file_name} | C:/Python312/python.exe {script_name}"'

    # コマンドを実行
    result = subprocess.run(command, check=True, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # 結果を出力
    print(result.stdout)
    if result.stderr:
        print("Error:", result.stderr, file=sys.stderr)

if __name__ == "__main__":
    main()
