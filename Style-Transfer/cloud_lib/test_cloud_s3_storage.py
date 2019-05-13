import unittest
from cloud_s3_storage import CloudS3Storage

class TestCloudS3Storage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s3_cloud = CloudS3Storage()

    @classmethod
    def tearDownClass(cls):
        cls.s3_cloud.close()

    def test_get_all_buckets(self):
        buckets = self.__class__.s3_cloud.get_all_buckets()
        input_bucket = [b for b in buckets if b.name == 'input' ]
        self.assertEqual(len(input_bucket),1)

    def test_read_file(self):
        resulting_str = self.__class__.s3_cloud.read_file_as_string('input','tesla-little.jpg')
        self.assertTrue(bool(resulting_str))

    def test_upload_file(self):
        # First upload
        self.__class__.s3_cloud.upload_file('output','test.txt','sample/test.txt')
        
        #Then test if present
        resulting_str = self.__class__.s3_cloud.read_file_as_string('output','test.txt')
        self.assertEqual(resulting_str.decode('ascii'), 'this is an upload test') 



if __name__ == '__main__':
    unittest.main()