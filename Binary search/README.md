# Бинарный поиск
## A. Двоичный поиск
Имя входного файла: стандартный ввод<br>
Имя выходного файла: стандартный вывод<br>
Ограничение по времени: 1 секунда<br>
Ограничение по памяти: 256 мегабайт<br>
Реализуйте алгоритм бинарного поиска. Вам нужно ответить на несколько вопросов "Присутствует ли элемент x" в отсортированном массиве.

### Формат входных данных
В первой строке содержатся числа n и k (1 <= n, k <= 10^5).<br>
Во второй строке задаются n элементов первого массива, отсортированного по возрастанию, а в
третьей строке — k вопросов. Все элементы целые, в диапазоне [−10^9 ; 10^9].

### Формат выходных данных
Для каждого из k чисел второго массива выведите в отдельную строку «YES», если это число
встречается в первом массиве, и «NO» в противном случае.

### Пример
**input.txt**
````
10 5
1 2 3 4 5 6 7 8 9 10
-2 0 4 9 12
````
**output.txt**
````
NO
NO
YES
YES
NO
````
### Замечание
В массиве чисел от 1 до 10 есть числа 4, 9, но нет чисел -2, 0, 12

## B. Рядом
Имя входного файла: стандартный ввод<br>
Имя выходного файла: стандартный вывод<br>
Ограничение по времени: 1 секунда<br>
Ограничение по памяти: 256 мегабайт<br>
Вам дан отсортированный массив a_n и запросы для поиска элемента, максимально близкого к
запрошенному x (|ai−x| → min). Если есть несколько значений с минимальной разницей по модулю,
надо вывести минимальное.

### Формат входных данных
В первой строке содержатся числа n и k (1 <= n, k <= 10^5).<br>
Во второй строке задаются n элементов первого массива, отсортированного по возрастанию, а в
третьей строке — k вопросов. Все элементы целые, в диапазоне [−2 * 10^9 ; 2 * 10^9].

### Формат выходных данных
Для каждого из k чисел выведите в отдельную строку число из первого массива, наиболее близкое к данному. Если таких несколько, выведите меньшее из них.

### Пример
**input.txt**
````
5 5
1 3 5 7 9
2 4 8 1 6
````
**output.txt**
````
1
3
7
1
5
````
### Замечание
В примере дан массив 1, 3, 5, 7, 9.
Поскольку |2 − 1| = |2 − 3|, то ответ на первый запрос — 1 (как min(1, 3)) Аналогично на 4, 8
ответы 3, 7.
Число 1 присутствует в массиве, поэтому в данном случае мы найдем не просто ближайшее
число, а 1, ведь |1 − 1| = 0

## C. Отгадай число
Имя входного файла: стандартный ввод<br>
Имя выходного файла: стандартный вывод<br>
Ограничение по времени: 1 секунда<br>
Ограничение по памяти: 256 мегабайт<br>
Эта задача немного необычна — в ней вам предстоит реализовать интерактивное взаимодействие с тестирующей системой. Это означает, что вы можете делать запросы и получать ответы в
online-режиме. Обратите внимание, что ввод/вывод в этой задаче — стандартный (то есть с экрана на экран). После вывода очередного запроса обязательно используйте функции очистки потока,
чтобы часть вашего вывода не осталась в каком-нибудь буфере. Например, на С++ надо использовать функцию fflush(stdout), на Java вызов System.out.flush(), на Pascal flush(output) и
stdout.flush() для языка Python.
В этой задаче вам предстоит в интерактивном режиме угадать число x, которое загадала тестирующая система. Про загаданное число x известно, что оно целое и лежит в границах от 1 до n
включительно (значение n известно заранее).
Вы можете делать запросы к тестирующей системе, каждый запрос — это вывод одного целого
числа от 1 до n. Есть два варианта ответа тестирующей системы на запрос:
- строка «<» (без кавычек), если загаданное число меньше числа из запроса;
- строка «>=» (без кавычек), если загаданное число больше либо равно числу из запроса.

В случае, если ваша программа наверняка угадала нужное число x, выведите строку вида «!
x», где x — это ответ, и завершите работу своей программы.
Вашей программе разрешается сделать не более 25 запросов.

### Формат входных данных
Для чтения ответов на запросы программа должна использовать стандартный ввод.
В первой строке входных данных будет содержаться целое положительное число n (1 <= n <= 10^6)
— максимально возможное число, которое может быть загадано.
В следующих строках на вход вашей программе будут подаваться строки вида «<» и «>=». i-я из
этих строк является ответом системы на ваш i-й запрос. После того, как ваша программа угадала
число, выведите «! x» (без кавычек), где x — это ответ, и завершите работу своей программы.
Тестирующая система даст вашей программе прочитать ответ на запрос из входных данных только после того, как ваша программа вывела соответствующий запрос системе и выполнила операцию
flush.

### Формат выходных данных
Для осуществления запросов программа должна использовать стандартный вывод.
Ваша программа должна выводить запросы — целые числа xi (1 6 xi 6 n) по одному в строке (не
забывайте выводить «перевод строки» после каждого значения xi). После вывода каждой строки
программа должна выполнить операцию flush.
Каждое из значений xi обозначает очередной запрос к системе. Ответ на запрос программа
сможет прочесть из стандартного ввода. В случае, если ваша программа угадала число x, выведите
строку вида «! x» (без кавычек), где x — ответ, и завершите работу программы.

### Пример
**input.txt**
````
20

<

>=

>=

````
**output.txt**
````

5

3

4

! 4
````
###  Замечание
Вот заготовка для python
````
import sys
n = int(input())
def query(x):
    print(x)
    sys.stdout.flush()
    return input()
````

## D. Двоичный поиск
Имя входного файла: стандартный ввод<br>
Имя выходного файла: стандартный вывод<br>
Ограничение по времени: 1 секунда<br>
Ограничение по памяти: 256 мегабайт<br>
Найдите такое число x, что x^2 + (x + 1)^(1/2) = C, с точностью не менее 6 знаков после точки.

### Формат входных данных
В единственной строке содержится вещественное число 1 <= C <= 10^10.

### Формат выходных данных
Выведите одно число — искомый x.

### Пример
**input.txt**
````
2.0000000000 
````
**output.txt**
````
0.80926547401163950735
````
**input.txt**
````
18.0000000000 
````
**output.txt**
````
3.97119409286392421876
````

## E. Двоичный поиск
Имя входного файла: стандартный ввод<br>
Имя выходного файла: стандартный вывод<br>
Ограничение по времени: 1 секунда<br>
Ограничение по памяти: 256 мегабайт<br>
Дано кубическое уравнение ax3 +bx2 +cx+d = 0 (a != 0). Известно, что у этого уравнения ровно
один корень. От вас требуется его найти.
Заметьте, что разрешены различные случаи: любой из коэффициентов может быть положительным, отрицательным, или все коэффициенты, кроме a, могут быть равны нулю.

### Формат входных данных
Во входных данных через пробел записаны четыре целых числа: −1000 <= a, b, c, d <= 1000.

### Формат выходных данных
Выведите единственный корень уравнения с точностью не менее 4 знаков после десятичной точки

### Пример
**input.txt**
````
1 -3 3 -1 
````
**output.txt**
````
1 -3 3 -1 1
````