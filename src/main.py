from google.cloud import storage
from google.cloud import bigquery


def yourEntrypoint(event, context):  # Change the name of the function
    """
    Trigger function for individual processing of a file
    :param event: Contains all meta information like bucket name, filename etc.
    :param context: Context-Object contains context.event_id, context.timestamp, context.event_type, context.resource
    :return: None
    """
    # Client-Initialization
    storageClient = storage.Client()
    bigqueryClient = bigquery.Client()

    # Rename for Readability
    file = event

    # Path to file in Bucket
    uriFilePath = "gs://{}/{}".format(file["bucket"], file["name"])