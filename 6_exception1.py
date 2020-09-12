"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    words = ask_user_dict()
    try:
      while True:
        user_say = input('Пользователь: ')
        user_input = words.get(user_say)
        if user_input is not None:
          print(f'Программа: {user_input}')
        else:
          break
    except KeyboardInterrupt:
      print("\nПрограмма: Пока!")

def ask_user_dict():
  words = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"}
  return words

if __name__ == "__main__":
    ask_user()
