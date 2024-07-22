import replicate


class VisionAnalyzer:
    """ Vision Analyzer class """

    llm: str
    """ Model to be used by the Vision Analyzer component.

    Obviusly it should be a image processing one.
    
    Defauts to "yorickvp/llava-13b:80537f9eead1a5bfa72d5ac6ea6414379\
        be41d4d4f6679fd776e9535d1eb58bb" """
    prompt: str
    """ Prompt to be used by the Vision Analyzer component.
    
    Defaults to "Name the objects in the image" """

    def __init__(self,
                 llm="yorickvp/llava-13b:80537f9eead1a5bfa72d5ac6ea6414379be41d4d4f6679fd776e9535d1eb58bb",
                 prompt="Name the objects in the image"):
        self.llm = llm
        self.prompt = prompt

    def recognize_objects(self, image_url: str) -> str:
        """ Recognizes objects from image in the URL image_url 

        Args:
            image_url (str): Image URL. 
            Example: https://trashhero.org/wp-content/uploads/2017/08/17425951_1864190273860688_6937369437897271107_n.jpg

        Returns:
            result (str): String with the name and description of the objects
        """
        _input = {
            "image": image_url,
            "prompt": self.prompt
        }

        output = replicate.run("yorickvp/llava-13b:80537f9eead1a5bfa72d5ac6ea6414379be41d4d4f6679fd776e9535d1eb58bb",
                               input=_input)

        result = ""
        for r in output:
            result += r

        return result
