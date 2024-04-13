class GameStatistics:
    number_kill_player1 = 0
    number_kill_player2 = 0
    death_time_player1 = None
    death_time_player2 = None
    death_time_enemy = None
    @staticmethod
    def reset_kill():
        GameStatistics.number_kill_player1 = 0
        GameStatistics.number_kill_player2 = 0
    def reset_death_time():
        GameStatistics.death_time_player1 = None
        GameStatistics.death_time_player2 = None
        GameStatistics.death_time_enemy = None