# Gazprom

## Task 1
[![Build Status](https://github.com/ONEPANTSU/gazprom/actions/workflows/test_task1.yml/badge.svg?branch=main)](https://github.com/ONEPANTSU/gazprom/actions/workflows/test_task1.yml/)


### Description
Получение длины кратчайшего четкого пути в матрице 
с учётом сетки двоичной матрицы n x n. 
Если четкого пути нет, возвращается -1.
Четкий путь в двоичной матрице - это путь 
от верхней левой ячейки (т.е. (0, 0)) к
нижней правой ячейке (т.е. (n - 1, n - 1)) такой, что:
- Все посещенные ячейки пути равны 0.
- Все соседние ячейки контура соединены в 8 направлениях 
(т.е. они разные и имеют общее ребро или угол).
- Длина открытого пути - это количество посещенных ячеек этого пути.

Поиск реализован с помощью алгоритма BFS:
 - Время: O(V + E), где V - количество вершин, E - количество рёбер. 
 - Память: O(V), где V - количество вершин.


### Run
```bash
python3 -m venv venv
. ./venv/bin/activate
cd task1
pip install -r requirements.txt
python3 src/path_search.py
```

### Test
```bash
cd task1
pytest . -vs
```

## Task 2
[![Build Status](https://github.com/ONEPANTSU/gazprom/actions/workflows/test_task2.yml/badge.svg?branch=main)](https://github.com/ONEPANTSU/gazprom/actions/workflows/test_task2.yml/)

### Description
Небольшой API-сервис на Python, который выполняет поиск 
по иерархической структуре с вложенностью элементов N, 
где у каждого элемента есть айди и список детей. 
На вход функции поступает uuid нужного элемента, 
а на выходе - путь до этого элемента во вложенной структуре.

Поиск реализован с помощью алгоритма DFS:
 - Время: O(V + E), где V - количество вершин, E - количество рёбер. 
 - Память: O(V), где V - количество вершин.

### Run
```bash
cd task2
docker-compose build
docker-compose up
```

Или

```bash
python3 -m venv venv
. ./venv/bin/activate
cd task2
pip install -r requirements.txt
python3 src/run.py
```
Приложение будет доступно по `http://localhost:8000`

### Test
```bash
cd task2
pytest . -vs
```