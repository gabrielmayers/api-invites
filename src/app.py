from flask import Flask, request

app = Flask(__name__)

invites_list = ['e9LGYg4yvT7jHzME', 'xvbZwaCjC4UrGKmG', 'xhyBaWmENMe6a5DZ', 'qJxhV33Pu7hpDVM6', '4PEcFf6jCxvumPmB',
                'wMkSD9Yke4eSRCnm', 'Lef55KYdKWd9djcK', 'hJPWfsDuJx9Mcnpv', 'd2tFugWsVkmwPuC9', 'kaKJSwzKSPy9VrEP',
                'tKFxKDHvUbue4rws', 'cFFJ79rLDJe3mr7k', 'HnL6KXayYJkXHeeV', '3gxm4ZvUJHBwPpBD', 'gF4vFxQjV2Z9fx2W',
                'fhcMbk6B6LNWa2wY', '222LBNeE6gdSeYMM', '3XEz38HsybJu6V88', 'mAPpFnn94DpsLZLn', 'cB2mvzeE8aZTasWb']

@app.route('/hi')
def hi():
    return 'Ok!'

@app.route('/check_invite', methods=['GET'])
def check_invite():
    invite = request.args.get('code')

    if invite in invites_list:
        return 'Ok!'
    else:
        return 'Not Ok!'

## TODO
@app.route('/generate_invite', methods=['POST'])
def generate_invite():

    return True

if __name__ == '__main__':
    app.run(debug=True)