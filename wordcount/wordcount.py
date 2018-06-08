from flask import Flask, url_for
from flask_restplus import Resource, Api, fields
from collections import Counter
import string

app = Flask(__name__)


class WrappedAPI(Api):
    """This class wraps the flask_restplus API class in order to change the 
    behavior of the specs_url method. When _external=True, it tries to load
    swagger.json over HTTP.
    more info: https://github.com/noirbizarre/flask-restplus/issues/223"""

    @property
    def specs_url(self):
        """
        The Swagger specifications absolute url (ie. `swagger.json`)

        :rtype: str
        """
        return url_for(self.endpoint("specs"), _external=False)


api = WrappedAPI(
    app, description="Count words in text.", version="1.0", title="WordCount"
)

wordcount_input = api.model(
    "Resource",
    {
        "words": fields.String(
            required=True,
            description="Words to be counted",
            example="Text to be counted.",
        ),
        "strip_chars": fields.String(
            required=False,
            example=string.punctuation,
            description="Characters to strip from input",
        ),
    },
)


def count_words(words, strip_chars=None, word_delimiter=" ", make_lower=True):
    """count_words returns a Counter object built on `words` after stripping
    selected characters and tokenizing words with a chosen delimeter."""
    if make_lower:
        words = words.lower()
    if strip_chars:
        char_strip_map = "".maketrans(dict.fromkeys(strip_chars))
        words = words.translate(char_strip_map)
    word_counts = Counter(w for w in words.split(word_delimiter) if w)
    return word_counts


@api.route("/wordcount")
class WordCount(Resource):
    @api.expect(wordcount_input, validate=True)
    def post(self):
        """Accepts text and returns the total count of words and a 
        case-insensitive count of the occurrence of each word in the text. 
        ASCII punctuation is stripped by default, but this can be 
        overridden by including the optional strip_chars parameter."""
        words = api.payload["words"]
        if "strip_chars" not in api.payload:
            strip_chars = string.punctuation
        else:
            strip_chars = api.payload["strip_chars"]
        word_counts = count_words(words, strip_chars)
        total_count = sum(word_counts.values())
        return {"count": total_count, "words": word_counts}
