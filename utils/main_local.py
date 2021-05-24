from src.main import yourEntrypoint
from utils.Context import Context

"""
During local development, please adapt and use the code block below accordingly for testing purposes. Create a bucket on 
Google Cloud Storage for development purposes and specify the name in the event-dict. Further please specify your project
name. The bucket specified Bucket is FIXED and is used for cloud functions development. When executing the script locally
we simulate a trigger event.
"""
if __name__ == '__main__':
    """
    The "event" dictionary has different fields within the storage service, which can be viewed at the following link
    https://cloud.google.com/storage/docs/json_api/v1/objects#resource . If necessary, please expand accordingly.
    """
    event = {
        "project": "your-gcp-project",  # Dont change
        "bucket": "YOUR BUCKET",  # DONT change
        "name": "cloud/path/to/file"
    }

    context = Context(event_Id=383104,
                      timestamp="20210521120655",
                      event_type="google.storage.object.finalize",
                      resource="storage")

    yourEntrypoint(event, context)