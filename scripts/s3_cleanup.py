import boto3
def delete_s3_bucket(bucket_name):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    try:
        # Delete all objects in the bucket
        bucket.objects.all().delete()
        print(f"Deleted all objects in bucket: {bucket_name}")

        # Delete all versioned objects (if versioning is enabled)
        if bucket.object_versions:
            bucket.object_versions.all().delete()
            print(f"Deleted all versioned objects in bucket: {bucket_name}")

        # Delete the bucket
        bucket.delete()
        print(f"Deleted bucket: {bucket_name}")
    except Exception as e:
        print(f"Error deleting bucket {bucket_name}: {e}")

if __name__ == "__main__":
    bucket_name = input("my-test-bucket-47")
    delete_s3_bucket(bucket_name)

