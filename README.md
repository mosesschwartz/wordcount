# wordcount
wordcount is a toy app implementing an API endpoint to count words in text using Flask and Swagger.

# Installation
```python setup.py install```

# Running
Run `python run_wordcount_dev.py` to start the app in the Flask development server.

# Try it out!
View the Swagger documentation and test interactively by pointing yourweb browser at http://localhost:5000. 

Or give it a try with CURL:
```bash
$ curl -X POST "http://localhost:5000/wordcount" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"words\": \"Text text text! to be counted.\"}"

{
    "total_count": 6,
    "by_word": {
        "text": 3,
        "to": 1,
        "be": 1,
        "counted": 1
    }
}
```

# Testing
Run `pytest` from this directory to run tests. These tests only cover the backend logic, not the Flask or Flask-Restplus components that implement the API.
 
`wordcount` was developed and tested with Python 3.6. 