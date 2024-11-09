import os # Подключение системы(Windows)
import sys # Подключение переменных и системных операций
import subprocess # Позволяет управлять процессами системы
import random # Подключение рандомайзера
import speech_recognition # Требуется для прослушки команд пользователя
import webbrowser # Требуется для открытия браузера
import wikipediaapi # Поиск определений в Wikipedia
from pydub import AudioSegment # Требуется для воспроизведения аудио ответа от помощника
from pydub.playback import play # Воспроизводит аудио ответ от помощника

class Lilith():
    addWords = ''
    isStarted = False

while True:
    sr = speech_recognition.Recognizer()
    sr.pause_threshold = 0.5
    commands_dict = { # Все команды прописываются тут 
        'commands': {         
            'greeting': ['привет лилит', 'привет лили', 'лилит привет', 'лили привет', 'приветик', 'приветик лилит', 'приветик лили', 'привет', 'здравуйствуй', 'я дома', 'доброе утро'],
            'brouser': ['запусти браузер', 'открой браузер', 'браузер', 'лилит открой браузер', 'лили открой браузер', 'лили включи браузер', 'лилит включи браузер', 'лилит запусти браузер', 'лили запусти браузер'],
            'music': ['лили включи музыку', 'лилит включи музыку', 'лилит запусти музыку', 'лили запусти музыку', 'музыка', 'включи музыку', 'запусти музыку'],
            'bye': ['лилит уйди', 'лили уйди', 'уйди', 'пока', 'пока лили', 'пока лилит', 'выключись', 'лилит выключайся', 'лили выключайся', 'до завтра', 'до завтра лили', 'до завтра лилит'], 
            'mood': ['как дела', 'как настроение', 'как ты себя чувствуешь', 'лилит как дела', 'лили как дела'],
            'thanks': ['молодец', 'молодец лили', 'молодец лилит', 'спасибо', 'спасибо лилит', 'спасибо лили'],
            'ender': ['лилит выключи компьютер', 'лили выключи компьютер', 'лилит выключай компьютер', 'лили выключай компьютер', 'выключи компьютер', 'выключай компьютер'],
            'google_search': ['лилит найди', 'лили найди', 'найди'],
            'youtube_search': ['лилит покажи', 'лили покажи', 'покажи', 'видео', 'включи видео'],
            'wikipedia_search': ['лилит что такое', 'лили что такое', 'что такое', 'определение'],
            'open_word':['включи word', 'запусти word', 'word', 'включи текстовый редактор', 'запусти текстовый редактор'],
            'open_excel':['включи excel', 'запусти excel', 'excel', 'открой таблицы', 'включи таблицы', 'включи таблицу', 'открой таблицу', 'таблица', 'таблицы', 'таблицу'],
            'open_powerpoint':['включи powerpoint', 'запусти powerpoint', 'powerpoint', 'открой презентацию', 'открой презентации', 'презентация', 'презентации'],
            'close_word':['закрой word', 'выключи word', 'закрой текстовый редактор', 'выключи текстовый редактор'],
            'close_excel':['закрой excel', 'выключи excel', 'закрой таблицу', 'закрой таблицы', 'выключи таблицу', 'выключи таблицы', 'выключи таблицу'],
            'close_powerpoint':['закрой powerpoint', 'выключи powerpoint', 'закрой презентацию', 'выключи презентацию'],
        }
    }

    commands_enter = {
        'enter_commands': {
              'start': ['лилит', 'лили'],
         }
    }

    def listen_command():# Распознает слова в тексте
        try:
            with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                audio = sr.listen(source=mic)
                query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
                print(query)
            return query
        
        except speech_recognition.UnknownValueError:
            return ' '

    def greeting():# Отвечает на приветствие 
        hello_files = ['C:/Program Files/Lilith/voice/hello.wav', 'C:/Program Files/Lilith/voice/hello1.wav', 'C:/Program Files/Lilith/voice/hello2.wav']
        selected_hello = random.choice(hello_files)
        sound_audio = AudioSegment.from_wav(selected_hello)
        play(sound_audio)

    def mood():# Отвечает на вопрос как дела
        ans_files = ['C:/Program Files/Lilith/voice/mood.wav', 'C:/Program Files/Lilith/voice/mood1.wav', 'C:/Program Files/Lilith/voice/mood2.wav', 'C:/Program Files/Lilith/voice/mood3.wav', 'C:/Program Files/Lilith/voice/mood4.wav']
        selected_ans = random.choice(ans_files)
        sound_audio = AudioSegment.from_wav(selected_ans)
        play(sound_audio)

    def thanks():# Отвечает на похвалу
        ans_files = ['C:/Program Files/Lilith/voice/thanks.wav', 'C:/Program Files/Lilith/voice/thanks1.wav', 'C:/Program Files/Lilith/voice/thanks2.wav']
        selected_ans = random.choice(ans_files)
        sound_audio = AudioSegment.from_wav(selected_ans)
        play(sound_audio)
        Lilith.isStarted = False

    def brouser():# Открывает браузер
        webbrowser.open('https://', new=1)
        song = AudioSegment.from_wav('C:/Program Files/Lilith/voice/browser.wav')
        play(song)
        Lilith.isStarted = False

    def google_search(): # Поиск в Google
        temp = Lilith.addWords.replace(' ', '+')
        url = "https://google.com/search?q=" + temp # Поиск заданной командой информации в Google
        webbrowser.open(url)
        Lilith.addWords = ''
        song = AudioSegment.from_wav('C:/Program Files/Lilith/voice/ethernet.wav')
        play(song)
        Lilith.isStarted = False
    
    def youtube_search(): # Поиск в Youtube
        temp = Lilith.addWords.replace(' ', '+')
        url = "https://www.youtube.com/results?search_query=" + ''.join(temp) # Поиск заданной командой информации в youtube
        webbrowser.open(url)
        Lilith.addWords = ''
        song = AudioSegment.from_wav('C:/Program Files/Lilith/voice/ethernet.wav')
        play(song)
        Lilith.isStarted = False

    def wikipedia_search(): # Поиск в Wikipedia
        wiki = wikipediaapi.Wikipedia(user_agent = 'zoze25@mail.ru', language = "ru")
        wiki_page = wiki.page(Lilith.addWords)
        if wiki_page.exists():
            webbrowser.open(wiki_page.fullurl)
            song = AudioSegment.from_wav('C:/Program Files/Lilith/voice/ethernet.wav')
            play(song)
        else: 
            google_search() # Перенаправление на поиск заданной командой информации в Google
        Lilith.addWords = ''
        Lilith.isStarted = False

    def music(): # Включает музыку в браузере
        webbrowser.open('https://www.youtube.com/live/jfKfPfyJRdk?feature=share', new=2)
        song = AudioSegment.from_wav('C:/Program Files/Lilith/voice/music.wav')
        play(song)
        Lilith.isStarted = False

    def open_word(): # Запускает приложение Microsoft Word
        ans_files = ['C:/Program Files/Lilith/voice/run.wav', 'C:/Program Files/Lilith/voice/run_word.wav', 'C:/Program Files/Lilith/voice/run_word1.wav']
        selected_ans = random.choice(ans_files)
        sound_audio = AudioSegment.from_wav(selected_ans)
        play(sound_audio)
        subprocess.call("C:/Program Files/Lilith/bat_files/word.bat", shell=True)
        Lilith.isStarted = False
    
    def close_word(): # Отключает приложение Microsoft Word
        ans_files = ['C:/Program Files/Lilith/voice/close.wav', 'C:/Program Files/Lilith/voice/ender.wav']
        selected_ans = random.choice(ans_files)
        sound_audio = AudioSegment.from_wav(selected_ans)
        play(sound_audio)
        microsoft_word = "WINWORD.EXE"
        os.system(f"taskkill /f /im {microsoft_word}")
        Lilith.isStarted = False

    def open_excel(): # Запускает приложение Microsoft Excel
        ans_files = ['C:/Program Files/Lilith/voice/run.wav', 'C:/Program Files/Lilith/voice/run_excel.wav', 'C:/Program Files/Lilith/voice/run_excel1.wav']
        selected_ans = random.choice(ans_files)
        sound_audio = AudioSegment.from_wav(selected_ans)
        play(sound_audio)
        subprocess.call("C:/Program Files/Lilith/bat_files/excel.bat", shell=True)
        Lilith.isStarted = False

    def close_excel(): # Отключает приложение Microsoft Excel
        ans_files = ['C:/Program Files/Lilith/voice/close.wav', 'C:/Program Files/Lilith/voice/ender.wav']
        selected_ans = random.choice(ans_files)
        sound_audio = AudioSegment.from_wav(selected_ans)
        play(sound_audio)
        microsoft_excel = "EXCEL.EXE"
        os.system(f"taskkill /f /im {microsoft_excel}")
        Lilith.isStarted = False

    def open_powerpoint(): # Запускает приложение Microsoft Powerpoint
        ans_files = ['C:/Program Files/Lilith/voice/run.wav', 'C:/Program Files/Lilith/voice/run_powerpoint.wav', 'C:/Program Files/Lilith/voice/run_powerpoint1.wav']
        selected_ans = random.choice(ans_files)
        sound_audio = AudioSegment.from_wav(selected_ans)
        play(sound_audio)
        subprocess.call("C:/Program Files/Lilith/bat_files/powerpoint.bat", shell=True)
        Lilith.isStarted = False

    def close_powerpoint(): # Отключает приложение Microsoft Powerpoint
        ans_files = ['C:/Program Files/Lilith/voice/close.wav', 'C:/Program Files/Lilith/voice/ender.wav']
        selected_ans = random.choice(ans_files)
        sound_audio = AudioSegment.from_wav(selected_ans)
        play(sound_audio)
        microsoft_powerpoint = "POWERPNT.EXE"
        os.system(f"taskkill /f /im {microsoft_powerpoint}")
        Lilith.isStarted = False

    def ender(): # Выключает компьютер
        song = AudioSegment.from_wav('C:/Program Files/Lilith/voice/ender.wav')
        play(song)
        os.system('shutdown /s /f /t 0')
        
    def bye(): # Выключает голосового помощника
        song = AudioSegment.from_wav('C:/Program Files/Lilith/voice/bye.wav')
        play(song)
        sys.exit()

    def start(): # Запускает выполнение функций после ввода команды для старта
        ans_files = ['C:/Program Files/Lilith/voice/start.wav', 'C:/Program Files/Lilith/voice/start1.wav']
        selected_ans = random.choice(ans_files)
        sound_audio = AudioSegment.from_wav(selected_ans)
        play(sound_audio)
        Lilith.isStarted = True

    def main():
        # Сравнивает команды с командами в списке
        query = listen_command()
        words = query.split()
        word = ''
        for i in range(len(words)):
            word += words[i]
            if Lilith.isStarted == False:
                for v in commands_enter['enter_commands'].get('start'):
                    if word in v:
                        print(globals()['start']())
            else:
                for k, v in commands_dict['commands'].items():
                    if word in v:
                        for wordIndex in range(i+1, len(words)):
                            Lilith.addWords += words[wordIndex]
                            Lilith.addWords += ' '
                        print(globals()[k]())
                word += ' '
            
    if __name__ == '__main__':
        main()