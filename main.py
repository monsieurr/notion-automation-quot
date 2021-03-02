import os
from os.path import join, dirname
#from dotenv import load_dotenv
from notion.client import NotionClient
from notion.block import PageBlock
from md2notion.upload import upload
from datetime import date

def get_current_date():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    return current_date

if __name__ == "__main__":

 #   dotenv_path = join(dirname(__file__), '.env')
 #   load_dotenv(dotenv_path)
    
    # token_v2 value obtained by insepcting the browser's cookies on a logged in session on Notion.so
    client = NotionClient(token_v2 = os.getenv('TOKEN_V2'))
    
    # URL of the page to edit
    page = client.get_block(os.getenv('PAGE_URL'))

    # Access a database using the URL of the database page or the inline block
    cv = client.get_collection_view(
        "https://www.notion.so/imonsieur/40223918171644b3bdeb7848f61132e6?v=db28b0ff77654e44801debef6938c9fd")

    #row = cv.collection.add_row()

    #print("The old title is:", page.title)

    #page.title = "Aujourd'hui " + "[" + get_current_date() + "]"

    with open("quoti.md", "r", encoding="utf-8") as mdFile:
        row = cv.collection.add_row()
        row.name = "Aujourd'hui " + "[" + get_current_date() + "]"
        #newPage = cv.children.add_new(
        #    PageBlock, title="Aujourd'hui " + "[" + get_current_date() + "]")
        # Appends the converted contents of TestMarkdown.md to newPage
        upload(mdFile, row)
