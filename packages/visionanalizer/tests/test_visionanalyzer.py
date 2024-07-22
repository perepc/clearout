from visionanalizer.vision_analyzer import VisionAnalyzer
from dotenv import load_dotenv
load_dotenv()


def test_recognize_objects():
    """ recognize_objects method test """
    va = VisionAnalyzer()
    image_url = "https://trashhero.org/wp-content/uploads/2017/08/17425951_1864190273860688_6937369437897271107_n.jpg"
    print(va.recognize_objects(image_url))
