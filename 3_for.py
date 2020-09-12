"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, 
    {'school_class': '4b', 'scores': [5,4,4,5,5]}, 
    {'school_class': '5a', 'scores': [3,2,2,4,2]},
    {'school_class': '7a', 'scores': [5,4,4,5,5]}]
    sum_scores = 0
    count_scores = 0
    for score in school:
      print(f"Средний балл по классу {score['school_class']}:  {(sum(score['scores']))/(len(score['scores']))}")
      sum_scores = sum_scores+sum(score['scores'])
      count_scores = count_scores+len(score['scores'])
    print(f'Средний балл по всей школе {sum_scores/count_scores}')
if __name__ == "__main__":
    main()
