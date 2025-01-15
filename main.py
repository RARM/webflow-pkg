import webflow_utils
import dotenv
import os
import argparse
import csv

dotenv.load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
SITE_ID = os.getenv('SITE_ID')

# Main program logic.
def print_setup_info():
  print('Webflow keys being used:')
  print(f"- API key: {API_TOKEN}")
  print(f"- Site ID: {SITE_ID}\n")

def save_pages_to_csv(pages, filename):
  with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([
      'id',
      'title',
      'slug',
      'archived',
      'draft',
      'localeId',
      'publishedPath',
      'seo_title',
      'seo_description',
      'openGraph_title',
      'openGraph_titleCopied',
      'openGraph_description',
      'openGraph_descriptionCopied'
    ])
    for page in pages:
      writer.writerow([
      page['id'],
      page['title'],
      page['slug'],
      page['archived'],
      page['draft'],
      page.get('localeId', ''),
      page.get('publishedPath', ''),
      page.get('seo', {}).get('title', ''),
      page.get('seo', {}).get('description', ''),
      page.get('openGraph', {}).get('title', ''),
      page.get('openGraph', {}).get('titleCopied', ''),
      page.get('openGraph', {}).get('description', ''),
      page.get('openGraph', {}).get('descriptionCopied', '')
    ])

if __name__ == "__main__":
  print_setup_info()
  parser = argparse.ArgumentParser(description='Webflow utility tool.')
  subparsers = parser.add_subparsers(dest='command', help='Sub-command help')

  # Sub-command for saving pages to CSV
  save_parser = subparsers.add_parser(
    'save_pages',
    help='Save Webflow pages basic info to a CSV file.'
  )
  save_parser.add_argument(
    '-o', '--output',
    type=str,
    required=True,
    help='The output CSV file path.'
  )

  # Placeholder for other sub-commands
  # other_parser = subparsers.add_parser(
  #   'other_command',
  #   help='Other command description.'
  # )

  args = parser.parse_args()

  if args.command == 'save_pages':
    pages = webflow_utils.list_pages(API_TOKEN, SITE_ID)
    save_pages_to_csv(pages, args.output)
    print(f"A total of { len(pages) } pages were saved to \"{args.output}\".")
  else:
    parser.print_help()