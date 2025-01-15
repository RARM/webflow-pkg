import webflow_utils
import dotenv
import os
import argparse
import saving_utils

dotenv.load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
SITE_ID = os.getenv('SITE_ID')

# Main program logic.
def print_setup_info():
  print('Webflow keys being used:')
  print(f"- API key: {API_TOKEN}")
  print(f"- Site ID: {SITE_ID}\n")

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

  # Sub-command for saving CMS items metadata to CSV
  save_cms_meta_parser = subparsers.add_parser(
    'save_cms_items_meta',
    help='Save Webflow CMS items metadata to a CSV file.'
  )
  save_cms_meta_parser.add_argument(
    '-o', '--output',
    type=str,
    required=True,
    help='The output CSV file path.'
  )
  save_cms_meta_parser.add_argument(
    '-c', '--collection',
    type=str,
    required=True,
    help='The collection ID to fetch CMS items metadata from.'
  )

  # Placeholder for other sub-commands
  # other_parser = subparsers.add_parser(
  #   'other_command',
  #   help='Other command description.'
  # )

  args = parser.parse_args()

  if args.command == 'save_pages':
    pages = webflow_utils.list_pages(API_TOKEN, SITE_ID)
    saving_utils.pages_to_csv(pages, args.output)
    print(f"A total of { len(pages) } pages were saved to \"{args.output}\".")
  elif args.command == 'save_cms_items_meta':
    cms_items = webflow_utils.get_live_CMS_items(API_TOKEN, args.collection)
    saving_utils.cms_items_meta_to_csv(cms_items, args.output)
    print(f"A total of { len(cms_items) } CMS items metadata were saved to \"{args.output}\".")
  else:
    parser.print_help()