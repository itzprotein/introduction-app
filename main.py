from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    responses1to5 = [
        request.form.get('name'),
        request.form.get('location'),
        request.form.get('trait'),
        request.form.get('party'),
        request.form.get('change')
    ]

    responses6to16 = [
        request.form.get('god'),
        request.form.get('karma'),
        request.form.get('reincarnation'),
        request.form.get('kidney'),
        request.form.get('morality'),
        request.form.get('life_fair'),
        request.form.get('education'),
        request.form.get('heartbreak'),
        request.form.get('regret'),
        request.form.get('humanity'),
        request.form.get('morning')
    ]

    yes_count = sum(1 for ans in responses6to16 if ans == 'yes')

    if yes_count >= 7:
        result = "Congratulations, welcome to the crew!"
    else:
        result = "Sorry, you do not qualify. Try again later."

    return render_template('result.html', responses1to5=responses1to5, responses6to16=responses6to16, result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
