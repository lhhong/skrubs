import logging

from flask import request, jsonify;

from codeitsuisse import app, challenge;

logger = logging.getLogger(__name__)

@app.route('/<c>', methods=['POST'])
def evaluate(c):
    print(c)
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    try:
        result = getattr(challenge, c).evaluate(data)
    except AttributeError:
        return jsonify({})

    logging.info("My result :{}".format(result))
    return jsonify(result);

