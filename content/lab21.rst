Практика: Pygame, шарики и ООП
##############################

:date: 2018-04-03 09:00
:status: draft

.. raw:: html

    <style>
    fieldset {
        border: 2px dashed gray;
        padding: 2px 5px;
        display: inline-block;
        border-top: 10px solid gray;
    }
    legend {
        padding: 0 5px;
    }
    fieldset table {
        border: 1px solid black
    }
    fieldset td {
        border: 1px solid black
    }
    </style>

.. contents:: Содержание

Общая информация
================

"Веб-программирование" включает в себя огромное множество различных понятий, языков и инструментов. Цель данной лабораторной - знакомство с основными из них.

HTML
====
.. default-role:: code

HTML - HyperText Markup Language - язык разметки гипертекста. HTML - это язык, на котором пишутся привычные нам веб-страницы. Документ на HTML состоит из тегов. Теги могут быть парные и одинарные.

- Одинарные теги имеет вид `<тег>`, например тег `<br>` - перевод строки и тег `<input>` - поле ввода для html-форм. Выглядит он так:

  .. raw:: html

      <fieldset>
      <legend>html</legend>
      <input>
      </fieldset>

- Парные теги имеют вид `<тег>содержание</тег>`, например тег `<b>`, задающий жирный шрифт, используется так: `обычный шрифт<b>жирный шрифт</b>`, а выглядит так:

  .. raw:: html

      <fieldset>
      <legend>html</legend>
      обычный шрифт<b>жирный шрифт</b>
      </fieldset>

Теги также могут иметь атрибуты - дополнительные параметры, задающие поведение и отображение соответствующего элемента. Атрибуты имеют вид `имя="значение"` и задаются вместе с именем тега, через пробел, в виде `<тег аттрибут1="значение1" аттрибут2="значение2">`, например

- `<input type="password">` - это будет уже не обычное поле ввода, а поле ввода пароля, где вместо букв будут отображаться звездочки.

  .. raw:: html

      <fieldset>
      <legend>html</legend>
      <input type="password">
      </fieldset>

- `<a href="http://ya.ru">яндекс</a>` - тег `<a>`, ссылка. Аттрибут `href` задает адрес ссылки.

  .. raw:: html

      <fieldset>
      <legend>html</legend>
      <a href="http://ya.ru">яндекс</a>
      </fieldset>

Теги можно вкладывать друг в друга: `<a href="http:ya.ru">это <b>яндекс</b></a>`.

.. raw:: html

    <fieldset>
    <legend>html</legend>
    <a href="http:ya.ru">это <b>яндекс</b></a>
    </fieldset>



CSS
===

Многообразие вебстраниц порождается многообразием стилей оформления элементов, начиная с выбора размера шрифта и заканчивая цветом рамочек, закругленными углами кнопок а также размерами и положением всех элементов. Изначально, стили задавались различными атрибутами тегов, например так:

.. code:: html

    <font size="2" color="blue"><b>This is some text!</b></font>

.. raw:: html

    <fieldset>
    <legend>html</legend>
    <font size="2" color="blue"><b>This is some text!</b></font>
    </fieldset>

Такой подход перегружает текст документа. Становится сложно что-то найти, что-то изменить. Например, если у нас все заголовки оформлены как указано выше, то, чтобы заменить цвет заголовков на красный, нам придется пройтись по всем заголовкам и все исправить. CSS - Cascading Style Sheets — каскадные таблицы стилей, призваны решить эту проблему. А именно, будем описывать стили элементов (и даже, отчасти, расположение) отдельно от основного документа. Синтаксис следующий:

.. code:: css

    селектор, селектор {
        свойство: значение;
        свойство: значение;
        свойство: значение;
    }

С помощью различных селекторов, мы выбираем множество html-элементов, для которых мы хотим задать значения свойств.

Пример:

css:

.. code:: css

    h1 {
        font-size: small;
        color: blue;
        font-weight: bold;
    }

html:

.. code:: html

    <h1> Заголовок 1 </h1>
    Какой-то текст

    <h1> Заголовок 2 </h1>
    Какой-то другой текст


.. raw:: html

    <style>
    h1.x {
        font-size: small;
        color: blue;
        font-weight: bold;
    }
    </style>
    <fieldset>
    <legend>html</legend>
    <h1 class="x"> Заголовок 1 </h1>
    Какой-то текст

    <h1 class="x"> Заголовок 2 </h1>
    Какой-то другой текст
    </fieldset>

Теперь мы легко можем поменять стиль всех заголовков. CSS можно задавать как и в отдельном файле, тогда он подключается в HTML тегом `<link rel="stylesheet" type="text/css" href="theme.css">`, либо прямо в html-документе, в теге `<style>...</style>`. Оба тега должны использоваться в секции `<head>...</head>`.

Javascript
==========

Красивые заголовки и кнопочки - это замечательно. Но кто позаботится об обработке кликов по этим самым кнопочкам? Скрипты на языке javascript могут использоваться в html страницах и выполняются непосредственно браузером. Javascript похож на python своей ссылочной моделью. Блоки кода выделяются парами фигурных скобок, а не отступами. Рассмотрим несколько примеров.

.. code:: html

    <div onclick="if (this.style.color=='red') { this.style.color='green'; this.innerText='Green' } else { this.style.color='red'; this.innerText='Red' }">Кликните по мне</div>

.. raw:: html

    <fieldset>
    <legend>html</legend>
    <div onclick="if (this.style.color=='red') { this.style.color='green'; this.innerText='Green' } else { this.style.color='red'; this.innerText='Red' }">Кликните по мне</div>
    </fieldset>

Атрибут `onclieck` задает код, который выполнится при клике мышью. При этом `this` - будет ссылкой на тот элемент, который кликнули. `this.style` - объект, предстваляющий стиль элемента, тот самый который мы можем задавать с помощью CSS. Конечно, задавать код непосредственно внутри тегов крайне не удобно. Перепишем пример, используя функцию:

.. code:: html

    <script>
    var flag = true;
    function toggle(self) {
        if (flag) {
            self.style.color = 'red';
            self.innerText = 'Red';
        } else {
            self.style.color = 'green';
            self.innerText = 'Green';
        }
        flag = !flag;
    }
    </script>

    <div onclick="toggle(this)">Green</div>

.. raw:: html

    <script>
    var flag = true;
    function toggle(self) {
        if (flag) {
            self.style.color = 'red';
            self.innerText = 'Red';
        } else {
            self.style.color = 'green';
            self.innerText = 'Green';
        }
        flag = !flag;
    }
    </script>

    <fieldset>
    <legend>html</legend>
    <div onclick="toggle(this)">Green</div>
    </fieldset>

Итак, скрипты можно писать в теге `<script>`. Можно и подключать отдельные файлы со скриптами, так: `<script src="http://address-of-script.js"></script>`. Заметьте, тег `<script>`  парный, закрывающий тег `</script>` обязателен, даже если внутри тега ничего нет. А вот тот же пример, но уже с использованием CSS:

.. code:: html

    <style>
    .one {
        color: red;
        font-weight: 'bold';
        border: 1px solid black;
    }
    .two {
        color: green;
        font-style: 'italics';
        border: 3px dashed red;
    }
    </style>

    <script>
    var flag = true;
    function toggle(self) {
        if (flag) {
            self.className = 'one';
            self.innerText = 'Red';
        } else {
            self.className = 'two';
            self.innerText = 'Green';
        }
        flag = !flag;
    }
    </script>

    <span onclick="toggle(this)">Green</span>

.. raw:: html

    <style>
    .one {
        color: red;
        font-weight: 'bold';
        border: 1px solid black;
    }
    .two {
        color: green;
        font-style: 'italics';
        border: 3px dashed red;
    }
    </style>

    <script>
    var flag = true;
    function toggle1(self) {
        if (flag) {
            self.className = 'one';
            self.innerText = 'Red';
        } else {
            self.className = 'two';
            self.innerText = 'Green';
        }
        flag = !flag;
    }
    </script>

    <fieldset>
    <legend>html</legend>
    <div class="two" onclick="toggle1(this)">Green</div>
    </fieldset>

Селектор CSS вида `.класс` выбирает элементы по "классу". Класс можно задавать в html, с помощью атрибута `class` или в javascript, в атрибут `className` элемента.

Вот пример, где мы изменяем наш документ с помощью javascript.

.. code:: html

    <script>

    function click() {
        document.getElementById('my-div').innerHTML += '<br><a href="ya.ru">ya.ru</a>';
    }

    </script>

    <button onclick="click()">кнопка</button>
    <div id="my-div"></div>

.. raw:: html

    <script>

    function click1() {
        document.getElementById('my-div').innerHTML += '<div><a href="ya.ru">ya.ru</a></div>';
    }

    </script>

    <fieldset>
    <legend>html</legend>
    <button onclick="click1(this)">кнопка</button>
    <div id="my-div"></div>
    </fieldset>

Базовая объектная модель html документа достаточно громоздка. Чего только стоит `document.getElementById('my-div').innerHTML`. Для упрощения жизни существует библиотека jQuery. Библиотека определяет одну единственную функцию `$` (да, javascript разрешает такие имена), в которой содержится вся функциональность. Вот пример ее использования, в котором html-код свободен уже не только от стилей но и от событий, а занимается исключительно версткой элементов и их содержимым.

.. code:: html

    <script src="http://judge.mipt.ru/mipt_cs_on_python3/jslib/jquery-3.3.1.min.js"></script>

    <style>
    .one {
        color: red;
        font-weight: 'bold';
        border: 1px solid black;
    }
    .two {
        color: green;
        font-style: 'italics';
        border: 3px dashed red;
    }
    </style>

    <script>
    $(function() {
        $('#one').click(function() {
            $('#one').toggleClass('one');
            $('#one').toggleClass('two');
            $('#another').append('<br><a href="ya.ru">ya.ru</a>');
      })
    })
    </script>

    <span id="one" class="one">Green</span><br>
    <span id="another">Another</span>

.. raw:: html

    <script src="http://judge.mipt.ru/mipt_cs_on_python3/jslib/jquery-3.3.1.min.js"></script>

    <style>
    .one {
        color: red;
        font-weight: 'bold';
        border: 1px solid black;
    }
    .two {
        color: green;
        font-style: 'italics';
        border: 3px dashed red;
    }
    </style>

    <script>
    $(function() {
        $('#one').click(function() {
            $('#one').toggleClass('one');
            $('#one').toggleClass('two');
            $('#another').append('<a href="ya.ru">ya.ru</a>');
      })
    })
    </script>

    <fieldset>
    <legend>html</legend>
    <span id="one" class="one">Green</span><br>
    <span id="another">Another</span>
    </fieldset>

Flask
=====

Как же сделать сайт? Оказывается одних только html, css и js не достаточно. Сайты, да и многие другие сетевые приложения используют модель клиент-сервер. Это значит, что у нас есть две отдельные части: сервер - приложение, которое, в случае сайта, запускается на машине хозяина сайта и клиент - часть приложения, которая работает непосредственно на машине пользователя. В случае с сайтом, клиентская часть представлена браузером, а также всеми html, css, js и прочим содержимым, которое браузер скачивает и выполняет на машине пользователя. Существует множество способов написать web-сервер. Один из них - модуль Flask для Python.

Рассмотрим такой пример

.. code:: python

    from flask import Flask
    from flask import render_template_string
    from flask import request
    app = Flask(__name__)

    log = ''

    templ = """
    <!DOCTYPE html>
    <div>
    {{ log }}
    </div>
    <form action="/" method="POST">
    <input name="msg">
    <input type="submit" value="send">
    </form>
    """

    @app.route('/', methods=['GET', 'POST'])
    def hello_world():
        global log
        if request.method == 'POST':
            log += request.form['msg'] + '<br>'

        return render_template_string(templ, log=log)


    if __name__ == '__main__':
        app.run()


Еще пример.

.. code:: python 

    from flask import Flask
    from flask import request
    from flask import url_for
    app = Flask(__name__)

    log = ''

    @app.route('/')
    def index():
        return app.send_static_file('client2.html')


    @app.route('/log')
    def get_log():
        global log
        return log

    @app.route('/send', methods=['POST'])
    def send():
        global log
        print request.form
        log += request.form['msg'] + '<br>'
        return log

    if __name__ == '__main__':
        app.run()

static/script2.js

.. code:: js

    function update() {
      $.get('log', function(data) {
        $('#chat').html(data);
      });
    }

    $(function() {
      $('#send').click(function() {
        $.post('/send', {'msg': $('#msg').val()}, update);
      })

      setInterval(update, 1000);
    })

static/client2.html

.. code:: html

    <!DOCTYPE html>

    <script src="http://judge.mipt.ru/mipt_cs_on_python3/jslib/jquery-3.3.1.min.js"></script>
    <script src="static/script2.js"></script>

    <div id="chat"></div>
    <input id="msg">
    <button id="send">send</button>

Pubnub
======

Сервер это здорово. Но иногда нет большой нужды писать его. Допустим, хотим написать чат на Python. Можно написать простенький сервер на Flask, но что дальше? Можно запустить его в локальной сети, тогда будет чат по локальной сети. А как на счет чата через интернет? Тут уже нужна машина с белым ip, т.е. доступная из интернета. Придется искать хостинг для вашего сервера, грузить его туда.. Вместо этого, можно использовать BAAS. BAAS - Backend As A Service. Это значит, что кто предоставляет нам бэк-энд (т.е. серверную часть приложения) как сервис, как услугу. Сервер уже есть и работает, можно испльзовать! Один из примеров таких BAAS - Pubnub.com. Этот бэкенд позволяет создавать каналы передачи сообщений. Простое api позволяет писать в канал и получать данные из канала. Все, сервер писать уже не придется. Рассмотрим пример.

a.py

.. code:: python

    from pubnub import Pubnub

    PUB_KEY = 'pub-c-bab40884-15d8-42a3-8675-21d381efc60e'
    SUB_KEY = 'sub-c-d3ff6da6-faa9-11e5-8180-0619f8945a4f'

    pubnub = Pubnub(publish_key=keys.PUB_KEY, subscribe_key=keys.SUB_KEY)

    def _callback(message, channel):
        print(message)

    def _error(message):
        print(message)

    pubnub.subscribe(channels="my_channel_sf23", callback=_callback, error=_error)

    while True:
        pass

Это приложение подписывается на канал `"my_channel_sf23"` в рамках аккаунта, заданного ключами PUB_KEY и SUB_KEY, и печатает все ошибки и сообщения, которые через него получает. Чтобы получить свои ключи, необходимо зарегистрироваться на pubnub.com.

.. code:: python

    import keys
    from pubnub import Pubnub

    PUB_KEY = 'pub-c-bab40884-15d8-42a3-8675-21d381efc60e'
    SUB_KEY = 'sub-c-d3ff6da6-faa9-11e5-8180-0619f8945a4f'

    pubnub = Pubnub(publish_key=keys.PUB_KEY, subscribe_key=keys.SUB_KEY)

    def callback(message):
        print(message)

    pubnub.publish('my_channel_sf23', 'Hello from PubNub Python SDK!', callback=callback, error=callback)

    while True:
        pubnub.publish('my_channel_sf23', input(), callback=callback, error=callback)

Это приложение отправляет в канал `"my_channel_sf23"` различные сообщения, в основном те, которые пользователь вводит с клавиатуры. По pubnub каналам можно передавать не только строки но и другие json-сериализуемые объекты.
