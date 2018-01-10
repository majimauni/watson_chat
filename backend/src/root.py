import os

from flask import Blueprint, jsonify
from dotenv import load_dotenv
from watson_developer_cloud import ConversationV1

root = Blueprint('root', __name__)

@root.route('/watson/<message>')
def watson_message(message):
    load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))

    conversation = ConversationV1(
        username = os.environ.get('WATSON_USERNAME'),
        password = os.environ.get('WATSON_PASSWORD'),
        version = os.environ.get('WATSON_API_VERSION')
    )

    response = conversation.message(
        workspace_id = os.environ.get('WATSON_WORKSPACE_ID'),
        input = {
            'text': message
        }
    )

    return jsonify(response)
