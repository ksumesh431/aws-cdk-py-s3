from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as s3,
    CfnOutput,
    aws_cloudfront as cf
)
from constructs import Construct

class StaticSiteStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        bucket = s3.Bucket(self, "siteBucket",
                           bucket_name="uniquenamesumesh2364746887",
                           public_read_access=True,
                           website_index_document="index.html")
        
        #Cloudformation Outputs
        CfnOutput(self, "siteBucketName", value=bucket.bucket_name)
        CfnOutput(self, "siteBucketWebsite", value=bucket.bucket_website_url)
