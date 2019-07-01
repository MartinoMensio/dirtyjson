# dirty-json python wrapper

A python wrapper for this amazing NodeJS application https://github.com/RyanMarcus/dirty-json

## Installation

1. Be sure to have node installed on your machine (otherwise go to https://nodejs.org/en/download/)
2. Install the node requirements: `npm install`
3. Install the Python requirements: `pip install -r requirements.txt`

## Running python wrapper

```python
import py_wrapper
import json

# ... have the broken string
string = '{something: ""very" broken"}'
fixed_string = py_wrapper.fix_json(string)

json.loads(fixed_string)
```

## Docker container

It would be nice to run as a REST webservice, to avoid language dependency.

This needs some few files / prebuilt docker image

`docker build -t martinomensio/dirtyjson .`

`docker run -dit --name dirtyjson-rest -p 12345:12345 martinomensio/dirtyjson`

Or from the docker hub (same command)

`docker run -dit --name dirtyjson-rest -p 12345:12345 martinomensio/dirtyjson`

Run a request to the microservice:

```bash
curl -X POST \
  http://localhost:12345 \
  -H 'Content-Type: text/plain' \
  -d '{broken:json}'
```

or in python:

```
import requests
requests.post('http://localhost:12345', data='{broken:json}', headers={'content-type': 'text/plain'}).json()
```

## Suggestion

This has a bit of latency, just run the requested when you are sure your JSON is broken (e.g. in the catch/except).
