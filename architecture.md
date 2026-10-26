# AWS AI Image Recognition Architecture

## Overview

This project uses Amazon Rekognition to detect labels in an image and return confidence scores.

## Architecture Diagram

```text
       +----------------------+
       |         User         |
       +----------+-----------+
                  |
                  | Select image
                  v
       +----------------------+
       |   Python Script      |
       |   detect_image.py    |
       +----------+-----------+
                  |
                  | AWS SDK (Boto3)
                  v
       +----------------------+
       | Amazon Rekognition   |
       |    DetectLabels      |
       +----------+-----------+
                  |
                  | Labels and confidence scores
                  v
       +----------------------+
       |    Python Output     |
       |      JSON Results    |
       +----------------------+
```

## Workflow

1. The user selects an image file.
2. The Python script reads the image.
3. Boto3 sends the image to Amazon Rekognition.
4. Rekognition identifies labels and confidence scores.
5. The script displays the results in JSON format.

## AWS Service

**Amazon Rekognition:** Used for image-label detection.

## Security

- Configure AWS credentials securely.
- Grant only the required Rekognition permissions.
- Never upload AWS access keys or secret keys to GitHub.

## Future Improvements

- Store images in Amazon S3.
- Build a web interface for image uploads.
- Save recognition results to a database.
- Add automated image processing with AWS Lambda.
