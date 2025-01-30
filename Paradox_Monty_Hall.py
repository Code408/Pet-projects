import tkinter as tk
from tkinter import messagebox
import random
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


class MontyHall:
    def __init__(self):
        self.game = [1, 1, 2]  # 1 - коза; 2 - автомобиль
        self.player_choice = None
        self.goat_door = None
        self.options = []
        self.switched = False  # Флаг смены двери
        self.conn = sqlite3.connect('monty_hall.db')  # подключение к БД
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    result TEXT,
                    switched INTEGER
                )
        ''')
        self.conn.commit()

    def save_result(self, result, switched):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO results (result, switched) VALUES (?, ?)', (result, switched))
        self.conn.commit()

    def init_game(self):
        random.shuffle(self.game)
        self.player_choice = None
        self.goat_door = None
        self.options = []
        self.switched = False

    def choose_door(self, door):
        self.player_choice = door
        self._reveal_goat()

    def _reveal_goat(self):
        self.options = [i for i in range(3) if i != self.player_choice and self.game[i] != 2]
        self.goat_door = random.choice(self.options)
        self.options = [i for i in range(3) if i != self.player_choice and i != self.goat_door]

    def switch_choice(self):
        if self.options:
            self.player_choice = self.options[0]
            self.switched = True

    def get_result(self):
        if self.game[self.player_choice] == 2:
            result = "Поздравляем! Вы выиграли автомобиль 🚗"
        else:
            result = "Неудача, попробуйте еще раз... 🐐"

        # Сохраняем в БД
        self.save_result(result, int(self.switched))
        return result

    def show_statistics(self):
        # Загружаем данные из БД
        df = pd.read_sql_query('SELECT * FROM results', self.conn)

        if len(df) >= 10:
            # Фильтрация
            wins = df[df['result'].str.contains("Поздравляем")]
            losses = df[df['result'].str.contains("Неудача")]

            # Доли выигрышей
            switched_wins = wins[wins['switched'] == 1].shape[0]
            not_switched_wins = wins[wins['switched'] == 0].shape[0]

            # Доли проигрышей
            switched_losses = losses[losses['switched'] == 1].shape[0]
            not_switched_losses = losses[losses['switched'] == 0].shape[0]

            # Данные для диаграммы
            labels = [
                'Выигрыши со сменой двери',
                'Выигрыши без смены двери',
                'Проигрыши со сменой двери',
                'Проигрыши без смены двери'
            ]
            sizes = [switched_wins, not_switched_wins, switched_losses, not_switched_losses]
            colors = ['limegreen', 'lightgreen', 'lightcoral', 'red']
            explode = (0.1, 0, 0.1, 0)  # куски

            # Отрисовка круга
            plt.figure(figsize=(8, 8))
            plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True,
                    startangle=140)
            plt.title('Статистика игр')
            plt.show()
        else:
            messagebox.showinfo("Статистика", "Сыграйте ещё несколько игр для отображения статистики")


class MontyHallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Парадокс Монти Холла")
        self.root.geometry("500x500")
        self.game = MontyHall()
        self.game.init_game()
        self.create_widgets()

    def create_widgets(self):
        # Кнопки для выбора двери
        self.door_buttons = []
        for i in range(3):
            button = tk.Button(self.root, text=f"Дверь {i + 1}", font=("Arial", 14),
                               command=lambda i=i: self.choose_door(i))
            button.pack(pady=5)
            self.door_buttons.append(button)

        # Кнопка для смены выбора
        self.switch_button = tk.Button(self.root, text="Поменять дверь", font=("Arial", 14), command=self.switch_choice,
                                       state=tk.DISABLED)
        self.switch_button.pack(pady=10)

        # Кнопка для отображения результата
        self.result_button = tk.Button(self.root, text="Показать результат", font=("Arial", 14),
                                       command=self.show_result, state=tk.DISABLED)
        self.result_button.pack(pady=10)

        # Кнопка для отображения статистики
        self.stats_button = tk.Button(self.root, text="Показать статистику", font=("Arial", 14),
                                      command=self.show_statistics)
        self.stats_button.pack(pady=10)

        # Кнопка новой игры
        self.new_game_button = tk.Button(self.root, text="Новая игра", font=("Arial", 14),
                                         command=self.new_game)
        self.new_game_button.pack(pady=10)

    def choose_door(self, door):
        self.game.choose_door(door)
        for button in self.door_buttons:
            button.config(state=tk.DISABLED)
        self.switch_button.config(state=tk.NORMAL)
        self.result_button.config(state=tk.NORMAL)

    def switch_choice(self):
        self.game.switch_choice()
        self.switch_button.config(state=tk.DISABLED)

    def show_result(self):
        result = self.game.get_result()
        messagebox.showinfo("Результат", result)
        self.result_button.config(state=tk.DISABLED)

    def show_statistics(self):
        self.game.show_statistics()

    def new_game(self):
        self.game.init_game()
        for button in self.door_buttons:
            button.config(state=tk.NORMAL)
        self.switch_button.config(state=tk.DISABLED)
        self.result_button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = MontyHallApp(root)
    root.mainloop()
