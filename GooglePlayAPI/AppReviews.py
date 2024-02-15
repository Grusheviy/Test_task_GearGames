from google_play_scraper import reviews

class AppReviews:
    def get_app_reviews(self, app_id, count=100):

        """
        Получение отзывов для приложения с использованием пагинации.
        :param app_id: Идентификатор приложения.
        :param count: Количество отзывов для получения (по умолчанию 100).
        :return: Список отзывов, ограниченный заданным количеством.
        """
        try:
            all_reviews = []
            continuation_token = None

            while len(all_reviews) < count and (continuation_token is None or len(all_reviews) < count):
                app_reviews, continuation_token = reviews(app_id, count=count, continuation_token=continuation_token)
                all_reviews.extend(app_reviews)

            return all_reviews[:count]
        except Exception as e:
            raise RuntimeError(f"Ошибка при получении отзывов для приложения {app_id}: {str(e)}")
