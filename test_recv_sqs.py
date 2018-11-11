import boto3

# Get the service resource
sqs = boto3.resource('sqs',
                     endpoint_url='http://localhost:9324',
                     region_name='elasticmq',
                     aws_secret_access_key='x',
                     aws_access_key_id='x',
                     use_ssl=False)

# Get the queue
queue = sqs.get_queue_by_name(QueueName='queue1')

# Process messages by printing out body and optional author name
for message in queue.receive_messages():

    # Print out the body and author (if set)
    print('Message: {0}!'.format(message.body))
