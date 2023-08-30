from bs4 import BeautifulSoup

def modify_html(content):
    soup = BeautifulSoup(content, 'html.parser')

    for text_node in soup.find_all(string=True):
        words = text_node.split()
        modified_words = ['<span class="bold-half">' + word[:len(word) // 2] + '</span>' + word[len(word) // 2:] for word in words]
        text_node.replace_with(' '.join(modified_words))

    css_style = soup.new_tag('style')
    css_style.string = '.bold-half { font-weight: bold; }'
    soup.head.append(css_style)

    return str(soup)
