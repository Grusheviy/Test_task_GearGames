from GooglePlayAPI.AppInfo import AppInfo
from GooglePlayAPI.AppReviews import AppReviews
from InfoGeters.PrintArtOfWarInfo import PrintArtOfWarInfo
from InfoGeters.PrintTopGames import PrintTopGames

def main():
    try:
        app_info = AppInfo()
        app_reviews = AppReviews()
        print_art_of_war_info = PrintArtOfWarInfo(app_info, app_reviews)

        try:
            print_top_games = PrintTopGames()
            print_top_games.print_top_games_info()

            try:
                user_input_art_of_war = input("Хотите просмотреть информацию для Art Of War 3? (да/нет): ")
                if user_input_art_of_war.lower() == 'да':

                    print_art_of_war_info.print_info_and_reviews(review_count=10)

            except Exception as e:
                print(f"Ошибка при выполнении блока для Art Of War 3: {str(e)}")

        except Exception as e:
            print(f"Ошибка при выполнении топ-3 скрипта: {str(e)}")

    except Exception as e:
        print(f"Ошибка при выполнении основного скрипта: {str(e)}")


if __name__ == "__main__":
    main()