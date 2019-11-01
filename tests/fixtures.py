from asynctest import CoroutineMock

import os


def getpage_content() -> CoroutineMock:
    current_dir = os.path.dirname(__file__)
    with open(os.path.join(current_dir, "pages/getpage.html"), "r") as f:
        file_content = f.read()
    
        return CoroutineMock(side_effect=[file_content])

def postpage_content() -> CoroutineMock:
    current_dir = os.path.dirname(__file__)
    with open(os.path.join(current_dir, "pages/postpage.html"), "r") as f:
        file_content = f.read()
    
        return CoroutineMock(side_effect=[file_content])
