from google_play_scraper import app

class AppInfo:
    def get_app_info(self, app_id):
        try:
            """
            Получение информации о приложении с использованием библиотеки google_play_scraper.
            :param app_id: Идентификатор приложения.
            :return: Информация о приложении.
            """
            app_info = app(app_id)
            return app_info

        except Exception as e:
            raise RuntimeError(f"Ошибка при получении информации о приложении {app_id}: {str(e)}")
