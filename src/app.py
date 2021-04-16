from flask import Flask, request

app = Flask(__name__)

arr_invites = ['gwirejk8947', 'ownvio3', '32few34w', 'slcndie', 'owkcdijfewq']

@app.route('/hi')
def hi():
    return 'Ok!'

@app.route('/check_invite', methods=['GET'])
def check_invite():
    invite = request.args.get('code')

    if invite in arr_invites:
        return 'Ok!'
    else:
        return 'Not Ok!'

@app.route('/generate_invite', methods=['POST'])
def generate_invite():

    return True

if __name__ == '__main__':
    app.run(debug=True)