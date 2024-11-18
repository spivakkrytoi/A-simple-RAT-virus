import subprocess
import sys
import os

# Список необхідних бібліотек
REQUIRED_PACKAGES = [
    'flask',
    'psutil'
]

def install_packages():
    """
    Встановлює всі необхідні бібліотеки.
    """
    for package in REQUIRED_PACKAGES:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"Пакет {package} успішно встановлено.")
        except subprocess.CalledProcessError:
            print(f"Помилка при встановленні пакета {package}.")

def run_main_script():
    """
    Запускає основний код.
    """
    main_script = 'main.py'  # Ім'я основного файлу
    if os.path.exists(main_script):
        try:
            subprocess.run([sys.executable, main_script])
        except Exception as e:
            print(f"Помилка при запуску {main_script}: {e}")
    else:
        print(f"Файл {main_script} не знайдено. Переконайтеся, що він знаходиться у цій же папці.")

if __name__ == "__main__":
    print("Встановлення необхідних бібліотек...")
    install_packages()
    print("\nЗапуск основного коду...")
    run_main_script()
