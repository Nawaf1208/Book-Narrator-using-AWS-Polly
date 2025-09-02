import boto3
import os

s3 = boto3.client('s3')
polly = boto3.client('polly')

def lambda_handler(event, context):
    # Get bucket and file details from event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    # Download text file from S3
    download_path = f"/tmp/{os.path.basename(object_key)}"
    s3.download_file(bucket_name, object_key, download_path)
    
    # Read text content
    with open(download_path, 'r') as file:
        text = file.read()
    
    # Send text to Polly
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Joanna'  # you can change to 'Matthew', 'Amy', 'Aditi', etc.
    )
    
    # Save audio to /tmp
    audio_file = "/tmp/output.mp3"
    with open(audio_file, 'wb') as f:
        f.write(response['AudioStream'].read())
    
    # Upload audio to S3 output folder
    output_key = f"output/{os.path.basename(object_key).replace('.txt', '.mp3')}"
    s3.upload_file(audio_file, bucket_name, output_key)
    
    return {
        'statusCode': 200,
        'body': f"Converted {object_key} to {output_key}"
    }
