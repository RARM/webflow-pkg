import webflow_utils
import dotenv
import os

dotenv.load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
SITE_ID = os.getenv('SITE_ID')

# Main program logic.
def main():
  print('Webflow keys:')
  print(f"- API key: {API_TOKEN}")
  print(f"- API key: {SITE_ID}\n")
  
  print('Getting all pages from Webflow...')
  pages = webflow_utils.list_pages(SITE_ID, API_TOKEN)
  
  print(f"Total pages: {len(pages)}.")

if __name__ == "__main__":
  main()