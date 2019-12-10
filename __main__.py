from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
def main(dict_res=None):
    if dict_res is None:
        dict_res = [
            {'description': 'Абстрактная фабрика',
             'href': 'abstract_factory'},
            {'description': 'Компоновщик',
             'href': 'composite'},
            {'description': 'Наблюдатель',
             'href': 'observer'},
            {'description': 'Строитель(Сдал)',
             'href': 'builder'},
            {'description': 'Декоратор(Сдал)',
             'href': 'decorator'},
            {'description': 'Одиночка',
             'href': 'singleton'},
            {'description': 'Фабрика',
             'href': 'factory'},
            {'description': 'Адаптер(Сдал)',
             'href': 'adapter'},
            {'description': 'Фасад',
             'href': 'facade'},
            {'description': 'Мост',
             'href': 'bridge'}
        ]
    for item in dict_res:
        f = open('include/descriptions/'+item['href']+'.txt', 'a', encoding='utf-8')
        f.close()
        f = open('include/field_area/' + item['href'] + '.txt', 'a', encoding='utf-8')
        f.close()
    return render_template('main.html', dict_res=dict_res)


@app.route('/patterns/<pattern_called>')
def patterns(pattern_called, dict_res=None):

    try:
        exec('from patterns.' + pattern_called + ' import get_data as get_' + pattern_called)
    except ImportError:
        return 'Такого паттерна нет в системе <a href=' + url_for('main') + \
           '> Вернитесь на главную страницу и выберите из доступных </a>'
    try:
        code_file = open('patterns/' + pattern_called + '.py', encoding='utf-8').read()
    except FileNotFoundError:
        return 'Такого паттерна нет в системе <a href=' + url_for('main') + \
               '> Вернитесь на главную страницу и выберите из доступных </a>'
    try:
        result = eval('get_' + pattern_called)()
    except SyntaxError or NameError:
        return 'Такого паттерна нет в системе <a href=' + url_for('main') + \
               '> Вернитесь на главную страницу и выберите из доступных </a>'
    if dict_res is None:
        dict_res = {
            'page_title': pattern_called.capitalize().replace('_', ' '),
            'code': '\n' + code_file,
            'result': '\n' + result,
            'description': open('include/descriptions/' + pattern_called+'.txt', encoding='utf-8').read(),
            'field_area': open('include/field_area/' + pattern_called + '.txt',encoding='utf-8').read()
        }
    return render_template('pattern_page.html', dict_res=dict_res)


if __name__ == '__main__':
    app.run()
