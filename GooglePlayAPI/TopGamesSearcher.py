from google_play_scraper import search

class TopGamesSearcher:
    def search_top_games(self, query, n_hits=3):
        try:
            search_results = search(query, n_hits=n_hits)
            return search_results
        except Exception as e:
            raise RuntimeError(f"Ошибка при поиске топовых игр: {str(e)}")
