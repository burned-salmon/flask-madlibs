"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a code, a title, a list of prompts,
    and the text of the template.

        >>> s = Story(
        ...     "simple",
        ...     "A Simple Tale",
        ...     ["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code, title, words, text):
        """Create story with words and template text."""

        self.code = code
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    "eyes",
    "The Eyes",
    ["place", "adjective", "past_tense_verb",
        "profession", "bad_body_part_to_have_an_eye_on"],
    """Once upon a time, in the old {place}, there was a {adjective} secret. Everyone in the {place} {past_tense_verb} it to each other. The horrible secret was that the local {profession} had an eye on their {bad_body_part_to_have_an_eye_on}."""
)

story2 = Story(
    "teeth",
    "Lots of Teeth",
    ["innocent_sounding_name", "number", "adjective", "monster"],
    """Little {innocent_sounding_name} had {number} too many teeth. {innocent_sounding_name} did everything to be rid of these excess teeth, but no matter how many were pulled out, they'd just grow back, like a {adjective} {monster}."""
)

story3 = Story(
    "doors",
    "The Hallway",
    ["your_hometown", "adjective", "number_below_100", "scary_synonym", "second_adjective"],
    """Residents of {your_hometown} suffer from an {adjective} fate. {number_below_100}% of all residents dream of The Hallway. In these {scary_synonym} dreams, they see a {second_adjective} hallway full of countless doors, each leading to a mistake from their life."""
)

# Make dict of {code:story, code:story, ...}
stories = {s.code: s for s in [story1, story2, story3]}
