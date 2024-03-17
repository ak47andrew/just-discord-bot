import xml.etree.ElementTree as ET

elementTree = ET.parse("config.xml")

def get_var(path: str) -> str:
    element = elementTree.find(path.replace(".", "/"))
    if element is None:
        raise ValueError(f"Path {path} is not found!")
    text = element.text
    if text is None:
        raise ValueError(f"Path {path} don't contain any value!"
                         "Use config.elementTree.find() to get other attributes.")
    return text

__all__ = ("get_var",)
