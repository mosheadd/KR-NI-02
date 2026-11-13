
import argparse
import secrets
import os
from pathlib import Path

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

from experiments.generate_passwords import generate, create_folder_and_file


def main():
    parser = argparse.ArgumentParser(description="Запуск эксперимента")

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        '-s', '--seed',
        type=int,
        default=42,
        help='Seed для генерации паролей (по умолчанию 42)'
    )

    group.add_argument(
        '--random',
        action='store_true',
        help='Использовать случайный seed'
    )

    args = parser.parse_args()

    seed = secrets.randbits(64) if args.random else args.seed

    root = Path(__file__).resolve().parent
    os.chdir(root)

    print(f"Генерация паролей (seed={seed})...")

    create_folder_and_file()
    generate(seed)

    print("Запуск эксперимента...")

    notebook_path = root / 'experiments' / 'experiment.ipynb'

    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)

    executor = ExecutePreprocessor(timeout=None, kernel_name='python3')

    executor.preprocess(notebook, {'metadata': {'path': str(root / 'experiments')}})

    print("Эксперимент завершён успешно!")


if __name__ == '__main__':
    main()
