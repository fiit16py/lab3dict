# ЛР3: Словари

### 1. Права доступа

Известны права доступа к некоторым файлам:

* запись W,
* чтение R,
* запуск X.
Для каждой из заданных попыток доступа к ним вывести результат.

В первой строке содержится число N — количество файлов содержащихся в данной файловой системе. В следующих N строчках содержатся имена файлов и допустимых с ними операций, разделенные пробелами. Далее указано чиcло M — количество запросов к файлам. В последних M строках указан запрос вида Операция Файл. К одному и тому же файлу может быть применено любое количество запросов.

Вам требуется ответить на каждый запрос в соответствии с заданными правами доступа к файлам (ваша программа для каждого запроса должна будет возвращать OK, если над файлом выполняется допустимая операция, или же Access denied, если операция недопустима).

#### Example Input

    1
    abacaba R X
    3
    read abacaba
    write abacaba
    execute abacaba

#### Example Output
    OK
    Access denied
    OK


### 2. Права доступа
Вводятся положительные целые числа, количество заранее неизвестно, ввод завершается нулем. Вывести максимальное из чисел, которые встречаются минимальное число раз.

#### Example Input

    6 8 6 8 6 3 3 8 3 3 8 6 6 6 9 9 9 9 9

#### Example Output
    8
