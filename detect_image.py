import json
import boto3
import urllib.parse

rekognition = boto3.client("rekognition")

def lambda_handler(event, context):

    try:
        # Get image details from S3 event
        bucket = event["Records"][0]["s3"]["bucket"]["name"]

        key = urllib.parse.unquote_plus(
            event["Records"][0]["s3"]["object"]["key"]
        )

        # Detect objects using Amazon Rekognition
        response = rekognition.detect_labels(
            Image={
                "S3Object": {
                    "Bucket": bucket,
                    "Name": key
                }
            },
            MaxLabels=10,
            MinConfidence=75
        )

        # Extract detected labels
        results = []

        for label in response["Labels"]:
            results.append({
                "Object": label["Name"],
                "Confidence": round(label["Confidence"], 2)
            })

        # Print results to CloudWatch
        print(json.dumps({
            "Image": key,
            "DetectedObjects": results
        }))

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Image analyzed successfully",
                "image": key,
                "results": results
            })
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        raise
