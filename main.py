from flask import Flask
import os
import pickle

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return 'Hello Bobs'

def is_women_name(username):
    username=username.lower()
    if username in ['никита','илья','муса','мустафа']:
        return False
    if username[-1] in ['я','а']:
        return True
    if username in ['любовь']:
        return True
    return False

@app.route('/<string:username>', methods=['GET'])
def get_epi(username):
    cursors = pickle.load(open("cursors.bin", "rb"))
    greetings = pickle.load(open("greetings.bin", "rb"))
    locked_greetings=pickle.load(open("locked_greetings.bin", "rb"))
    greeting = ''
    print(greetings)
    if username in locked_greetings:
        greeting = locked_greetings[username]
        return 'hello ' + greeting + " " + username
    if not is_women_name(username):
        greeting=greetings[cursors['male']]
        cursors['male']+=1
        cursors['male'] = cursors['male'] % (len(greetings))
    else:
        greeting=greetings[cursors['female']]
        greeting=greetings[cursors['female']][:-2]+"ая"
        cursors['female']+=1
        cursors['female'] = cursors['female'] % (len(greetings))

    pickle.dump(cursors, open("cursors.bin", "wb"))
    locked_greetings[username]=greeting
    pickle.dump(locked_greetings, open("locked_greetings.bin", "wb"))

    return 'hello ' + greeting + " " + username

    # task = filter(lambda t: t['id'] == task_id, tasks)
    # if len(task) == 0:
    #     abort(404)
    # return jsonify({'task': task[0]})


if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)
