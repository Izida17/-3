def function_name(search: str, status: bool, args: tuple[int, str], kwargs: dict[str, str]) -> str | list[int]:
    """
    Обрабатывает входные аргументы в зависимости от заданных параметров обработки.
    Поддерживает два режима работы: обработка позиционных аргументов (args) 
    и обработка именованных аргументов (kwargs).

    Параметры:
        search (str): Режим обработки аргументов. Допустимые значения:
            'args': активирует обработку позиционных аргументов
            'kwargs': активирует обработку именованных аргументов
            При любом другом значении вызывает исключение ValueError.

        status (bool): Флаг, определяющий формат вывода при обработке позиционных аргументов:
            True: возвращает только целочисленные значения из args
            False: конкатенирует все аргументы args в строку
            Игнорируется при search='kwargs'.

        args (int | str): Произвольное количество позиционных аргументов. 
            Могут быть как целыми числами (int), так и строками (str).
            Обрабатываются только при search='args'.

        kwargs (str): Произвольное количество именованных аргументов. 
            Все значения должны быть строками (str).
            Обрабатываются только при search='kwargs'.

    Возвращаемое значение:
        str | list[int]: Результат обработки аргументов:
            При search='args' и status=True: список целых чисел, извлеченных из args
            При search='args' и status=False: строка, содержащая все элементы args в одну строку
            При search='kwargs': форматированная строка с перечислением всех пар ключ-значение для всех пар 'kwargs'
           
    Исключения:
        ValueError: Возникает при:
            Некорректном значении параметра search (не 'args' и не 'kwargs')
    """
    

    result: list[int] = []
    result_2: str = ""
    
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += ("Key: {}, Value: {}; ".format(k, v))
        return result_2
    else:
        raise ValueError("Error for search")