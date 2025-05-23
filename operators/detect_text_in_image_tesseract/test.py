import re
import unittest

from feluda.models.media_factory import ImageFactory
from operators.detect_text_in_image_tesseract import detect_text_in_image_tesseract


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # initialize operator
        detect_text_in_image_tesseract.initialize(param={})

    @classmethod
    def tearDownClass(cls):
        # delete config files
        pass

    def test_sample_image_from_disk_hindi(self):
        image_url = "https://github.com/tattle-made/feluda_datasets/raw/main/feluda-sample-media/hindi-text-2.png"
        image_obj = ImageFactory.make_from_url_to_path(image_url)
        image_path = image_obj["path"]
        image_text = detect_text_in_image_tesseract.run(image_path)
        expected_text = "( मेरे पीछे कौन आ रहा है)"
        self.assertEqual(image_text.strip(), expected_text.strip())

    def test_sample_image_from_disk_tamil(self):
        image_url = "https://github.com/tattle-made/feluda_datasets/raw/main/feluda-sample-media/tamil-text.png"
        image_obj = ImageFactory.make_from_url_to_path(image_url)
        image_path = image_obj["path"]
        image_text = detect_text_in_image_tesseract.run(image_path)
        cleaned_image_text = re.sub(r"[\u200c\u200b]", "", image_text)
        expected_text = "காதல் மற்றும் போர்"
        self.assertEqual(cleaned_image_text.strip(), expected_text.strip())

    def test_sample_image_from_disk_telugu(self):
        image_url = "https://github.com/tattle-made/feluda_datasets/raw/main/feluda-sample-media/telugu-text.png"
        image_obj = ImageFactory.make_from_url_to_path(image_url)
        image_path = image_obj["path"]
        image_text = detect_text_in_image_tesseract.run(image_path)
        expected_text = "నేను భూమిని ప్రేమిస్తున్నాను"
        self.assertEqual(image_text.strip(), expected_text.strip())
