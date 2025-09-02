# Book-Narrator-using-AWS-Polly
![](AWS%20Polly.png)

1.Choose the suitable book, article, newsletter etc to be translated from text-to-speech. 

2.A lambda function to retrieve the text and send it to Amazon Polly for synthesis 

3.Choose the required language and a voice model provided. Amazon Polly converts the text-to-speech and sends it to AWS Lambda. 

4.The AWS Lambda function stores this audio file retrieved from Polly in Simple Storage Service (S3) 

5.The S3 bucket consists of the final text-to-speech audio.
