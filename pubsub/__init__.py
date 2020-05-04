import base64
import json

from google.cloud import pubsub_v1

def decode(msg):
    """ Convert data per pubsub protocol / data format
    Args:
        msg: The msg from Google Cloud
    Returns:
        data: The msg data as a string
    """
    if 'data' in msg:
        data = base64.b64decode(msg['data']).decode('utf-8')
        return data

def extract(msg):
    """Extract msg data as dict
    Args:
        msg: The msg from Google Cloud
    Returns:
        ctx: The msg as a dictionary
    """
    data = decode(msg)
    if data:
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
