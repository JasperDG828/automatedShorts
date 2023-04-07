from selenium import webdriver
from selenium.webdriver.edge.options import Options
from PIL import Image
from io import BytesIO

def screenPost(url, id):
    print("Screenshotting post "+id)
    options = Options()
    options.add_argument("--headless")
    options.add_argument("window-size=650,1400")
    driver = webdriver.Edge(options=options)
    driver.get(url)
    element = driver.find_element("id", 't3_'+id)
    location = element.location
    size = element.size
    png = driver.get_screenshot_as_png()
    driver.quit()
    im = Image.open(BytesIO(png))
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    im = im.crop((left, top, right, bottom))
    im.save("./screenshots/post_"+id+".png")

def screenComments(url, commentIds):
    print("Screenshotting comments: "+str(commentIds))
    options = Options()
    options.add_argument("--headless")
    options.add_argument("window-size=2160,5000")
    driver = webdriver.Edge(options=options)
    driver.get(url)
    for commentId in commentIds:
        element = driver.find_element("id", 't1_'+commentId)
        location = element.location
        size = element.size
        png = driver.get_screenshot_as_png()
        im = Image.open(BytesIO(png))
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        im = im.crop((left, top, right, bottom))
        im.save("./screenshots/comment_"+commentId+".png")
    driver.quit()
    
