from boto.s3.key import Key
from boto.s3.connection import S3Connection
from boto.s3.connection import OrdinaryCallingFormat
import os 

class CloudS3Storage:

    def __init__(self):
        self.apikey=os.getenv("CELLAR_ADDON_KEY_ID")
        self.secretkey=os.getenv("CELLAR_ADDON_KEY_SECRET")
        self.host=os.getenv("CELLAR_ADDON_HOST")

        cf=OrdinaryCallingFormat()  # This mean that you _can't_ use upper case name

        print('New connection to',self.host)
        self.connection=S3Connection(aws_access_key_id=self.apikey, aws_secret_access_key=self.secretkey, host=self.host, is_secure=False, calling_format=cf)

    def __get_bucket_object__(self, bucket_name, object_id):
        b = self.connection.get_bucket(bucket_name)
        k = Key(b)
        k.key = object_id

        return k

    def get_all_buckets(self):
        return self.connection.get_all_buckets()

    def upload_file(self, bucket_name, object_id, file_path):
        k = self.__get_bucket_object__(bucket_name, object_id)
        k.set_contents_from_filename(file_path)

    def upload_file_from_str(self, bucket_name, object_id, str_to_upload):
        k = self.__get_bucket_object__(bucket_name, object_id)
        k.set_contents_from_string(str_to_upload)
       
    def read_file_as_string(self, bucket_name, object_id):
        k = self.__get_bucket_object__(bucket_name, object_id)
        return k.get_contents_as_string()


    def close(self):
        print('End connection to',self.host)
        self.connection.close()