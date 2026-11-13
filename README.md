# Экспериментальное исследование влияния параметров алгоритмов хранения паролей на вычислительные затраты
## Описание
Данный репозиторий является курсовой работой по предмету "Основы разработки защищённого программного обеспечения и компьютерных сетей". (тип работы: КР-НИ, аналитико-исследовательская).

Целью работы является экспериментальное исследование влияния параметров алгоритмов хранения паролей (bcrypt, PBKDF2, Argon2) на вычислительные затраты (время выполнения и потребление оперативной памяти), а также определение оптимальных конфигураций, обеспечивающих баланс между безопасностью и производительностью системы.

Актуальность исследования обусловлена тем, что неправильный выбор параметров хеширования (например, слишком низкое количество итераций или малый объем памяти) делает систему уязвимой к атакам перебора. С другой стороны, завышенные параметры приводят к недопустимым задержкам при аутентификации пользователей.

В рамках работы были решены следующие задачи:
*   Реализован программный стенд на Python для замера времени и памяти.
*   Проведена серия замеров для трех алгоритмов с различными параметрами (Cost Factor, Iterations, Memory Cost).
*   Выполнена статистическая обработка данных (расчет медианы) для исключения фоновых шумов ОС.
*   Построены графики зависимостей вычислительных затрат от параметров.

Структура репозитория:
*   `experiments/` — Jupyter Notebook с основным кодом исследования, скрипты и папки с результатами (CSV) и графиками (PNG).
*   `report/` — итоговая пояснительная записка и презентация к защите.
*   `requirements.txt` — список необходимых библиотек для воспроизведения эксперимента.

Методология экспериментов, описание аппаратной среды и версии используемых библиотек подробно описаны в [methodology.md](experiments/methodology.md).
## Результаты
...
## Установка
1. Склонируйте репозиторий
```
git clone https://github.com/mosheadd/KR-NI-02.git
```
2. Зайдите в корневую папку
```
cd ../KR-NI-02
```
3. Установите нужные библиотеки
```
pip install -r requirements.txt
```
4. Запустите код
* С воспроизводимостью полученных результатов:
```
python run.py
```
* Можно выставить свой seed:
```
python run.py --seed 'число'
```
* Случайный seed:
```
python run.py --random
```

# Experimental research of impact of password-hashing alogorithms on computational cost.
## Description
This repository contains a term project for the course "Fundamentals of Developing Secure Software and Computer Networks" (project type: analytical-research term project).

The objective of this work is to experimentally investigate the impact of parameters for password-hashing algorithms (bcrypt, PBKDF2, Argon2) on computational costs (execution time and RAM usage), as well as to determine optimal configurations that provide a balance between security and system performance.

The relevance of this research stems from the fact that an improper choice of hashing parameters—such as an insufficient number of iterations or an inadequate amount of memory—renders a system vulnerable to brute-force attacks. Conversely, setting these parameters too high results in unacceptable delays during user authentication.

The following tasks were completed as part of this work:
*   A software testbed was implemented in Python to measure execution time and memory usage.
*   A series of measurements was conducted for three algorithms using various parameters (Cost Factor, Iterations, and Memory Cost).
*   Statistical data processing (calculation of the median) was performed to filter out background OS noise.
*   Graphs illustrating the dependence of computational costs on the parameters were generated.

Repository structure:
*   `experiments/` — Jupyter Notebook containing the core research code, scripts, and folders with results (CSV files) and plots (PNG images).
*   `report/` — final explanatory report and presentation for the defense.
*   `requirements.txt` — a list of the libraries required to reproduce the experiment.

The experimental methodology, description of the hardware environment and versions of the libraries used are described in detail in [methodology.md](experiments/methodology.md).
## Results
...
## Installation
1. Clone the repository
```
git clone https://github.com/mosheadd/KR-NI-02.git
```
2. Head to the root folder
```
cd ../KR-NI-02
```
3. Install the required libraries
```
pip install -r requirements.txt
```
4. Run the code
* To replicate the shown results:
```
python run.py
```
* Set a seed:
```
python run.py --seed 'number'
```
* Random seed:
```
python run.py --random
```