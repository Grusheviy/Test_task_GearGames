
def print_app_info(app_info):
    """
    Функция для вывода информации о приложении на экран.
    :param app_info: Информация о приложении, представленная в виде словаря.
    """
    try:
        # Вывод информации о приложении
        print("Название:", app_info['title'])
        print("Наименования разработчиков:", app_info['developer'])
        print("Описания игр:", app_info['description'])
        print("Средний балл игры:", app_info['score'])
        print("Количество установок:", app_info['installs'])
        print("----")

    except Exception as e:
        print(f"Ошибка при получении информации приложении: {str(e)}")
