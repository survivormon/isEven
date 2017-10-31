def isEven(n):
    import xml.etree.ElementTree as ET
    import requests
    question = "is {} even".format(n)
    response = requests.get("http://api.wolframalpha.com/v2/query?input={}&appid={}".format(question, "secret"))
    result = ET.fromstring(response.text).findall("./pod[@id='Result']")[0].find("subpod").find("plaintext").text
    if "not" not in result.split():
        return True
    else:
        return False
      
