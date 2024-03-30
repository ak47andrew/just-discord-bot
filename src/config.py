import xml.etree.ElementTree as ET

elementTree = ET.parse("config.xml")


def get_var(path: str) -> str:
    """Find and return the text value of an element in the XML tree.

    Args:
        path (str): The path to the element in dot notation.

    Raises:
        ValueError: If the element is not found.
        ValueError: If the element does not contain any value.

    Returns:
        str: The text value of the element.
    """
    element = elementTree.find(path.replace(".", "/"))
    if element is None:
        raise ValueError(f"Path {path} is not found!")
    text = element.text
    if text is None:
        raise ValueError(f"Path {path} don't contain any value!"
                         "Use config.elementTree.find() to get other attributes.")
    return text


__all__ = ("get_var",)
