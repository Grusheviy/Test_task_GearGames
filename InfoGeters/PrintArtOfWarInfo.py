from FileWriters.AOWFileWriter import FileWriter


class PrintArtOfWarInfo:
    def __init__(self, app_info, app_reviews):
        """
        Конструктор класса PrintArtOfWarInfo.
        Инициализирует экземпляры классов для работы с информацией о "Art Of War 3" и отзывах.
        :param app_info: Экземпляр класса AppInfo для получения информации об "Art Of War 3".
        :param app_reviews: Экземпляр класса AppReviews для получения отзывов об "Art Of War 3".
        """
        self.app_info = app_info
        self.app_reviews = app_reviews

    def print_info_and_reviews(self, package_name='com.geargames.aow', review_count=10):
        try:
            # Получение информации об Art Of War 3
            art_of_war_3_info = self.app_info.get_app_info(package_name)
            # Вывод информации о приложении
            print("Информация об Art of War 3:")
            print(f"Версия приложения: {art_of_war_3_info['version']}")
            print(f"Количество установок: {art_of_war_3_info['installs']}")
            print(f"Средний балл игры: {art_of_war_3_info['score']}")
            print(f"Количество оценок: {art_of_war_3_info['ratings']}")
            print("\n")

            # Получение отзывов для Art Of War 3
            art_of_war_3_reviews = self.app_reviews.get_app_reviews(package_name, count=review_count)
            for i, review in enumerate(art_of_war_3_reviews, start=1):
                print(f"Отзыв #{i}:")
                print(f"  Имя пользователя: {review['userName']}")
                print(f"  Дата отзыва: {review['at']}")
                print(f"  Текст сообщения: {review['content']}")
                print(f"  Оценка: {review['score']}")
                print("---")

            # Запись информации в файл
            FileWriter.aow_write_to_file(art_of_war_3_info, art_of_war_3_reviews)

        except Exception as e:
            print(f"Ошибка при выводе информации и отзывов для Art Of War 3: {str(e)}")
