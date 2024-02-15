class FileWriter:
    @staticmethod
    def top_write_to_file(app_info, app_reviews):
        """
        Статический метод для записи информации о приложении и отзывов в файл 'TOP_3.txt'.
        :param app_info: Информация о приложении, представленная в виде словаря.
        :param app_reviews: Список отзывов о приложении.
        """
        try:
            with open('TOP_3.txt', 'a', encoding='utf-8') as file:  # изменено w на a
                # Запись информации о приложении в файл
                file.write("Информация об TOP_3:\n")
                file.write(f"Название: {app_info['title']}\n")
                file.write(f"Наименования разработчиков: {app_info['developer']}\n")
                file.write(f"Описания игр: {app_info['description']}\n")
                file.write(f"Средний балл игры: {app_info['score']}\n")
                file.write(f"Количество установок: {app_info['installs']}\n\n")

                # Запись отзывов в файл
                file.write("Отзывы:\n")
                for i, review in enumerate(app_reviews, start=1):
                    file.write(f"Отзыв #{i}:\n")
                    file.write(f"  Имя пользователя: {review['userName']}\n")
                    file.write(f"  Дата отзыва: {review['at']}\n")
                    file.write(f"  Текст сообщения: {review['content']}\n")
                    file.write(f"  Оценка: {review['score']}\n")
                    file.write("---\n")

            print("Информация успешно записана в файл 'TOP_3.txt'")

        except Exception as e:
            print(f"Ошибка при записи информации в файл: {str(e)}")
