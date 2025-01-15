import csv
import json

def pages_to_csv(pages, filename):
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
      page.get('title', ''),
      page.get('slug', ''),
      page.get('archived', ''),
      page.get('draft', ''),
      page.get('localeId', ''),
      page.get('publishedPath', ''),
      page.get('seo', {}).get('title', ''),
      page.get('seo', {}).get('description', ''),
      page.get('openGraph', {}).get('title', ''),
      page.get('openGraph', {}).get('titleCopied', ''),
      page.get('openGraph', {}).get('description', ''),
      page.get('openGraph', {}).get('descriptionCopied', '')
      ])
      
def cms_items_meta_to_csv(items, filename):
  with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([
      'id',
      'cmsLocaleId',
      'isArchived',
      'isDraft'
    ])
    for item in items:
      writer.writerow([
      item['id'],
      item.get('cmsLocaleId', ''),
      item.get('isArchived', ''),
      item.get('isDraft', '')
      ])

def save_json(data, filename):
  with open(filename, 'w') as file:
    json.dump({"data": data}, file, indent=4)