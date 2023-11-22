from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def shuffle_numbers():
    # Generate an array of numbers from 1 to 100
    numbers = list(range(1, 70))

    # Shuffle the array
    random.shuffle(numbers)

    # Get the first ten numbers
    first_5 = sorted(numbers[:5])
    
    pballs = list(range(1, 27))

    # Shuffle the array
    random.shuffle(pballs)

    # Get the first ten numbers
    pball = pballs[:1]

    mega_nums = list(range(1,71))
    random.shuffle(mega_nums)
    meg5 = sorted(mega_nums[:5])
    mballs = list(range(1,26))
    random.shuffle(mballs)
    mball = mballs[:1]

    # Render them on a simple HTML page
    return render_template('index.html', pball_picks=first_5, pball=pball,mball_picks=meg5, mball=mball)

if __name__ == '__main__':
    app.run(debug=True)
