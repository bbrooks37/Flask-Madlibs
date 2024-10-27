from flask import Flask, render_template, request
from stories import stories

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('select_story.html', story_titles=stories.keys())

@app.route('/form')
def form():
    story_id = request.args.get('story')
    if not story_id:
        return "No story ID provided", 400
    story = stories.get(story_id)
    if not story:
        return "Invalid story ID", 404
    return render_template('form.html', title=story.title, words=story.words, story_id=story_id)

@app.route('/story')
def story():
    story_id = request.args.get('story_id')
    if not story_id:
        return "No story ID provided", 400
    story = stories.get(story_id)
    if not story:
        return "Invalid story ID", 404
    user_inputs = {word: request.args.get(word) for word in story.words}
    story_text = story.generate(user_inputs)
    return render_template('story.html', story=story_text)

if __name__ == '__main__':
    app.run(debug=True)
