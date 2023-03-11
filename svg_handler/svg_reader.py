from bs4 import BeautifulSoup
from lxml import etree

def get_preety_numpy_svg(svg_input: str, main_id_new_name: str='1') -> bool:
    '''Numpy outputs svg that has several flaws: bad background patch, bad names of svg lines
    This function optimizes svg files for further purposes with vpype, inkscape etc.'''

    xml_parser = etree.XMLParser
    with open(svg_input, 'r') as f:
        content = f.read()
        soup = BeautifulSoup(content, 'xml', parser=xml_parser)
        if not soup:
            return False
        # Removing a background patch, a standard  background figure produced by numpy
        try:
            background_patch = soup.select_one("g#patch_1")
            background_patch.extract()
        except AttributeError as e:
            print(e)
        
        # Renaming a standard axes_1#id attribute of a tag, so it can be pipelined to vpype
        try:
            axes_tag = soup.select_one("g#axes_1")
            axes_tag['id'] = main_id_new_name
        except TypeError as e:
            print(e)
        
        # Deleting figure_1 tag without affecting children tags
        try:
            figure = soup.select_one("g#figure_1")
            figure.unwrap()
        except AttributeError as e:
            print(e)

    with open(svg_input, 'w') as f:
        f.write(soup.prettify())
    
    return True


if __name__ == '__main__':
    svg_input = 'svg_handler/circles.svg'
    get_preety_numpy_svg(svg_input, '1-circles')
    print('Hello world!')