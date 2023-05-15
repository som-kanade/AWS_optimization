import boto3
import argparse
import logging
import os
import sys


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


parser = argparse.ArgumentParser(description ='Delete objects from given s3 bucket')
parser.add_argument('bucketName', type=str, help='Please enter s3 bucket name')
args = parser.parse_args()

# Check if aws creds exists in env
def checkIfEnvExists():
    try:
        if os.environ["AWS_ACCESS_KEY_ID"] and os.environ["AWS_SECRET_ACCESS_KEY"]:
            return True
        else:
            return False
    except Exception as e:
        logger.error(" Could not find aws creds in env exiting")
        return False


def deleteObjects(bucketName: str):
    try:
        s3_client = boto3.client("s3")
        bucket_name = bucketName
        objects = s3_client.list_objects_v2(Bucket=bucket_name)

        objects_to_delete = []
        for object in objects["Contents"]:
            objects_to_delete.append({"Key": object["Key"]})

        for i in range(0, len(objects_to_delete), 1000):
            batch_objects = objects_to_delete[i:i + 1000]

        s3_client.delete_objects(
            Bucket=bucket_name,
            Delete={"Objects": batch_objects}
        )

        return True
    
    except Exception as e:
        print(str(e))
        return False

def main():
    credEnvCheck = checkIfEnvExists()
    if credEnvCheck:
        logger.info(" Found aws creds in env proceeding further")
    else:
        logger.error(" Could not find aws creds in env exiting")
        sys.exit()
    checkIfObjectsDeleted = deleteObjects(args.bucketName)
    if checkIfObjectsDeleted:
        logger.info("Objects have been deleted from s3 bucket ")
    else:
        logger.error("Unable to delete objects from s3 bucket")
    

if __name__ == "__main__":
    main()
