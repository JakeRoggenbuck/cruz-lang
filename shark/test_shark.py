import unittest


class testShark(unittest.TestCase):
    def test_file_read_class(self):
        import shark
        reader = shark.readFile()
        self.assertTrue(reader, "Created an instance of readFile")

    def test_file_exists(self):
        import shark
        reader = shark.readFile()

        result = reader.read('test.cz')
        self.assertEqual(result, 'test.cz', "expected the filename test.cz")



if __name__ == "__main__":
    unittest.main() 
