from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    answers = {
        "q1": request.form.get('q1'),
        "q2": request.form.get('q2'),
        "q3": request.form.get('q3'),
    }
    hacker_type = ''
    explanation = ''

    if answers['q1'] == 'Python' and answers['q2'] == 'Изучаю новые технологии':
        hacker_type = 'Этичный хакер'
        explanation = 'Этичный хакер использует свои знания для защиты систем и сетей, выявляет уязвимости и помогает улучшать безопасность.'
    elif answers['q1'] == 'JavaScript' and answers['q2'] == 'Играю в игры':
        hacker_type = 'Геймер-хакер'
        explanation = 'Геймер-хакер использует свои навыки для модификации игр или создания уникальных игровых механик и модов.'
    elif answers['q1'] == 'C++':
        hacker_type = 'Технический хакер'
        explanation = 'Технический хакер разрабатывает программы и инструменты для тестирования безопасности систем.'
    elif answers['q1'] == 'Java':
        hacker_type = 'Черный хакер'  # Добавьте соответствующую проверку
        explanation = 'Черный хакер использует свои навыки для незаконных действий, таких как взлом систем и кража данных.'
    else:
        hacker_type = 'Белый хакер'
        explanation = 'Белый хакер работает на стороне законного бизнеса и использует свои навыки для защиты от киберугроз.'

    return render_template('result.html', hacker_type=hacker_type, explanation=explanation)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
