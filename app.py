from flask import Flask
app = Flask(__name__)

@app.route('/segment-generator')
def segment_generator():  # put application's code here
    return 'Segment generator'


if __name__ == '__main__':
    app.run()
