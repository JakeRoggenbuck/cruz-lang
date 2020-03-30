import unittest


class testShark(unittest.TestCase):
    def test_file_read_class(self):
        import cshark
        parser = cshark.Parse()
        self.assertTrue(parser, "Created an instance of Parse")


    def test_file_content(self):
        import cshark
        parser = cshark.Parse()
        
        files = [
            'a.cz',
            'code.cz',
            'test.cz'
        ]

        textList = [
            ['yeet\n'],
            ['lol\n'],
            ['hello world\n','hey\n']
        ]
        for x in range(len(textList)):
            result = parser.read(f'testFiles/{files[x]}')
            self.assertEqual(result, textList[x], 'Text was not read correctly')

if __name__ == "__main__":
    unittest.main()
