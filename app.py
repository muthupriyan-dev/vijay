from flask import Flask, Response
import time
from pathlib import Path

app = Flask(__name__)

FRAMES_FILE = Path(__file__).with_name('frames.txt')
FPS = 30
DELAY = 1 / FPS

with FRAMES_FILE.open('r', encoding='utf-8') as f:
    data = f.read()

frames = data.split('\n---FRAME ')[1:]
frames = ['---FRAME ' + x for x in frames]

# Strip the frame marker and any existing clear-screen escape at the start.
rendered_frames = []
for frame in frames:
    body = frame.split('\n', 1)[1] if '\n' in frame else frame
    body = body.replace('\x1b[H\x1b[2J', '', 1)
    rendered_frames.append(body)


def stream_animation():
    clear = '\x1b[2J\x1b[H'
    while True:
        for body in rendered_frames:
            yield clear + body + '\x1b[H'
            time.sleep(DELAY)


@app.get('/')
def home():
    return 'ASCII animation endpoint: /ascii\n'


@app.get('/ascii')
def ascii_animation():
    return Response(
        stream_animation(),
        mimetype='text/plain; charset=utf-8',
        headers={
            'Cache-Control': 'no-cache',
            'X-Accel-Buffering': 'no',
        },
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)
