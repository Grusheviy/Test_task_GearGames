from FileWriters.TOPFileWriter import FileWriter
from GooglePlayAPI.AppInfo import AppInfo
from GooglePlayAPI.AppReviews import AppReviews
from GooglePlayAPI.TopGamesSearcher import TopGamesSearcher
from InfoGeters.Print_app_info import print_app_info
from InfoGeters.PrintReviews import print_review


class PrintTopGames:
    def __init__(self):

        """
        Конструктор класса PrintTopGames.
        Инициализирует экземпляры классов для работы с информацией о приложениях, отзывах и поиске топовых игр.
        """
        self.app_info = AppInfo()
        self.app_reviews = AppReviews()
        self.top_games_searcher = TopGamesSearcher()

    def print_top_games_info(self):
        try:
            # Блок 1: Поиск "Art Of War 3" среди результатов запроса "best strategy game"
            try:
                top_games = self.top_games_searcher.search_top_games('best strategy game', n_hits=3)

                art_of_war_3_in_results = any(game['title'] == 'Art Of War 3' for game in top_games)

                if art_of_war_3_in_results:
                    print("Игра 'Art Of War 3' найдена в результате запроса 'best strategy game'.")

                    # Получение информации об Art Of War 3
                    art_of_war_3_info = self.app_info.get_app_info(top_games[0]['appId'])
                    print_app_info(art_of_war_3_info)

                    # Вывод отзывов к приложению "Art Of War 3"
                    user_input_info = input("Хотите просмотреть отзывы к этой игре? (да/нет): ")
                    if user_input_info.lower() == 'да':
                        print_review(self.app_reviews.get_app_reviews(top_games[0]['appId'], count=3))

                # Если "Art Of War 3" не найдена в результате запроса
                else:
                    print("Игра 'Art Of War 3' не найдена в результате запроса 'best strategy game'.\n")

                    # Вывод информации о каждой из топ-3 игр
                    for i, game in enumerate(top_games, start=1):
                        print(f"\nИнформация о {i}-й игре:")

                        # Получение информации о каждой игре из результатов поиска
                        game_info = self.app_info.get_app_info(game['appId'])
                        print_app_info(game_info)

                        # Запрос пользователя
                        user_input_review = input(f"Хотите просмотреть отзывы к {i}-й игре? (да/нет): ")
                        if user_input_review.lower() == 'да':
                            # Получение отзывов
                            game_reviews = self.app_reviews.get_app_reviews(game['appId'], count=5)

                            # Вывод отзывов к каждой игре
                            print_review(game_reviews)

                            # Запись информации в файл
                            FileWriter.top_write_to_file(game_info, game_reviews)

            except Exception as e:
                print(f"Ошибка при выполнении блока 1: {str(e)}")

        except Exception as e:
            print(f"Ошибка при выполнении основного скрипта: {str(e)}")
