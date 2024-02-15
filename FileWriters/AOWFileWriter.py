class FileWriter:
    @staticmethod
    def aow_write_to_file(app_info, app_reviews):
        """
        Статический метод для записи информации о приложении Art of War 3 и отзывов в файл 'art_of_war_3_info.txt'.
        :param app_info: Информация о приложении, представленная в виде словаря.
        :param app_reviews: Список отзывов о приложении.
        """
        try:
            with open('art_of_war_3_info.txt', 'w', encoding='utf-8') as file:
                # Запись информации о приложении в файл
                file.write("Информация об Art of War 3:\n")
                file.write(f"Версия приложения: {app_info['version']}\n")
                file.write(f"Количество установок: {app_info['installs']}\n")
                file.write(f"Средний балл игры: {app_info['score']}\n")
                file.write(f"Количество оценок: {app_info['ratings']}\n\n")

                # Запись отзывов в файл
                file.write("Отзывы:\n")
                for i, review in enumerate(app_reviews, start=1):
                    file.write(f"Отзыв #{i}:\n")
                    file.write(f"  Имя пользователя: {review['userName']}\n")
                    file.write(f"  Дата отзыва: {review['at']}\n")
                    file.write(f"  Текст сообщения: {review['content']}\n")
                    file.write(f"  Оценка: {review['score']}\n")
                    file.write("---\n")

            print("Информация успешно записана в файл 'art_of_war_3_info.txt'")

        except Exception as e:
            print(f"Ошибка при записи информации в файл: {str(e)}")