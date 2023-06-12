from bs4 import BeautifulSoup

# HTML document to be parsed
html_doc = """
<html>
<head>
	<title>Sample HTML document</title>
</head>
<body>
	<h1>Heading</h1>
	<p>This is a paragraph</p>
	<ul>
		<li>Item 1</li>
		<li>Item 2</li>
	</ul>
</body>
</html>
"""

# Create a BeautifulSoup object from the HTML document
soup = BeautifulSoup(html_doc, 'html.parser')

# Find the first h1 tag and print its text
heading = soup.find('h1')
print(heading.text)

# Find all li tags and print their text
items = soup.find_all('li')
for item in items:
    print(item.text)
