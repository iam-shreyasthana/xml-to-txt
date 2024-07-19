from lxml import etree

def extract_text_from_element(element):
    text = element.text if element.text else ""
    for child in element:
        text += extract_text_from_element(child)
        if child.tail:
            text += child.tail
    return text

def xml_to_plaintext(xml_file, output_file):
    context = etree.iterparse(xml_file, events=('end',), tag='*')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for event, elem in context:
            text_content = extract_text_from_element(elem)
            f.write(text_content + "\n")
            elem.clear()

# Example usage
xml_file = 'xml_file.xml'
output_file = 'output_xml_file.txt'
xml_to_plaintext(xml_file, output_file)
