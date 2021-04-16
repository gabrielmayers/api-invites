from flask import Flask, request

app = Flask(__name__)

invites_list = ['7v[9cpv&:8-bNL)x', '%&NPmm2;7.AjCKWv', 'ySUb^Cfz.9EPh~Kt', 'PLbeBADA.+_)3<Uj', '3S2ykS4`$7#M&3KB',
                '9t:/3D/Tgq!,NP:"', 'q5UY45g,xS,ER;2n', 'hJPWfsDuJx9Mcnpv', 'd2tFugWsVkmwPuC9', 'kaKJSwzKSPy9VrEP',
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

@app.route('/generate_invite', methods=['POST'])
def generate_invite():

    return True

if __name__ == '__main__':
    app.run(debug=True)