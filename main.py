import os
import subprocess

def open_src_and_run_dino():
    # Определяем путь к папке src относительно текущего скрипта
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_folder_path = os.path.join(current_dir, 'src')
    
    if not os.path.exists(src_folder_path):
        print(f"Папка {src_folder_path} не найдена.")
        return
    
    # Переходим в папку src
    os.chdir(src_folder_path)
    
    # Запускаем файл dino.py
    try:
        subprocess.run(['python', 'dino.py'], check=True)
    except Exception as e:
        print(f"Ошибка при выполнении dino.py: {e}")

if __name__ == "__main__":
    open_src_and_run_dino()
