"""
5 у вас есть текст разбейте текст по предложениям. В качестве результата вы должны получить список из предложений.
"""
import re
text = """Многие думают, что Lorem Ipsum - взятый с потолка псевдо-латинский набор слов, но это не совсем так.
Его корни уходят в один фрагмент классической латыни 45 года н.э., то есть более двух тысячелетий назад.
Ричард МакКлинток, профессор латыни из колледжа Hampden-Sydney, штат Вирджиния, взял одно из самых странных 
слов в Lorem Ipsum, "consectetur", и занялся его поисками в классической латинской литературе. В результате 
он нашёл неоспоримый первоисточник Lorem Ipsum в разделах 1.10.32 и 1.10.33 книги "de Finibus Bonorum et Malorum" 
("О пределах добра и зла"), написанной Цицероном в 45 году н.э. Этот трактат по теории этики был очень популярен 
в эпоху Возрождения.
Первая строка Lorem Ipsum, "Lorem ipsum dolor sit amet..", происходит от одной из строк в разделе 1.10.32!"""
text = re.sub(r'\s+', ' ', text, flags=re.M)
for _, sent in enumerate(re.split(r'(?<=[.!?…])\s+', text), 1):
    sent = sent.replace('\n', ' ')
    print(f"{sent}")
