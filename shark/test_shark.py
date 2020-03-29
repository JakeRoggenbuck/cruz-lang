import unittest

class testShark (unittest.TestCase):
    def test_file_read_class(self):
        import shark
        reader = shark.ReadFile()
        self.assertTrue(reader, "Reader class exists")

    def test_file_exists(self):
        import shark
        reader = shark.ReadFile()
        result = reader.read('test.cz')
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
