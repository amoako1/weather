from bs4 import BeautifulSoup

html_doc = """
<html>
 <head>
  <title>Hello world</title>
 </head>
 <body>
  <p>i like python</P>
  </body>
  </html>
  """
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.title.text)