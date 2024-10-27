class Story:
    def __init__(self, title, words, template):
        self.title = title
        self.words = words
        self.template = template

    def generate(self, user_inputs):
        return self.template.format(**user_inputs)

stories = {
    "park_day": Story(
        title="A Day at the Park",
        words=["adjective", "noun", "verb", "adverb"],
        template="It was a {adjective} day at the park. The {noun} decided to {verb} {adverb}."
    ),
    "ocean_adventure": Story(
        title="Ocean Adventure",
        words=["adjective", "noun", "verb", "adverb"],
        template="The {noun} {verb} {adverb} in the {adjective} ocean."
    )
}
