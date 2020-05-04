import base64
import json

from google.cloud import pubsub_v1

def handle(msg, load_json=True):
    """Convert msg per pubsub protocol / data format
    Args:
        msg: The msg from Google Cloud
        load_json: If True will treat data as json
    Returns:
        ctx: The msg converted to a string
    """
    if 'data' in msg:
        ctx = base64.b64decode(msg['data']).decode('utf-8')
        if load_json:
            ctx = json.loads(ctx)
        return ctx

def publish(topic, data, project_id=None):
    """Publish data to topic
    Args:
        topic: The name of the topic
        data (dict): A dictionary of data
        project_id: The Google project ID
    Returns:
        None
    """
    publisher = pubsub_v1.PublisherClient()
    data_str = json.dumps(data)
    topic_path = publisher.topic_path(project_id, topic)
    return publisher.publish(topic_path, 
            data=data_str.encode('utf-8'))
