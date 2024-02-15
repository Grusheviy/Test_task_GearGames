def print_review(app_reviews, count=100):
    """
    Функция для вывода отзывов на экран.

    :param app_reviews: Список отзывов приложения.
    :param count: Количество отзывов для вывода (по умолчанию 100).
    """
    try:
        if isinstance(app_reviews, list):
            if not app_reviews:
                print("Отзывы отсутствуют.")
            else:
                for i, review in enumerate(app_reviews[:count], start=1):
                    if isinstance(review, dict):
                        user_name = review.get('userName', 'Не указано')
                        date_of_review = review.get('at', 'Не указана')
                        text_of_review = review.get('content', 'Отсутствует')
                        score_of_review = review.get('score', 'Не указана')

                        print(f"Отзыв #{i}:")
                        print(f"  Имя пользователя: {user_name}")
                        print(f"  Дата отзыва: {date_of_review}")
                        print(f"  Текст сообщения: {text_of_review}")
                        print(f"  Оценка: {score_of_review}")
                        print("---")
        else:
            print("Отзывы не будут отображены.")

    except Exception as e:
        print(f"Ошибка при выводе отзывов: {str(e)}")
