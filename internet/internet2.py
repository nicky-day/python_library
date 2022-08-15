import base64


def img_to_string(filename):
    """
    파일명(filename)을 입력으로 받아 Base64로 인코딩한 문자열을 반환한다.
    """
    with open(filename, "rb") as f:
        return base64.b64encode(f.read())


def string_to_img(s, filename):
    """
    Base64로 인코딩된 문자열(s)과 파일명(filename)을 입력으로 받아 문자열을 파일로 저장한다.
    """
    with open(filename, "wb") as f:
        f.write(base64.b64decode(s))


img_to_string = img_to_string("test.jpg")
string_to_img(img_to_string, "result.jpg")
