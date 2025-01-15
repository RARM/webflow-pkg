import requests
import json

ERROR_FILENAME = "latest_error.json"

def list_pages(site_id, api_key, localeId=None):
  """
  Fetches a list of pages from a Webflow site.
  
  Args:
    site_id (str): The ID of the Webflow site.
    api_key (str): The API key for authentication.
    localeId (str, optional): Locale identifier (when using localization).
  Returns:
    list: A list of pages from the Webflow site.
  Raises:
    requests.exceptions.HTTPError: If the request to the Webflow API fails.
  Notes:
    The function paginates through all available pages using the limit and
    offset Webflow parameters. If an error occurs during the request,
    the response is logged to a file specified by ERROR_FILENAME.
  """
  url = f"https://api.webflow.com/v2/sites/{site_id}/pages"
  headers = {
    "Authorization": f"Bearer {api_key}"
  }

  all_pages = []
  offset = 0
  limit = 100

  while True:
    params = {
      "limit": limit,
      "offset": offset
    }
    if localeId:
      params["localeId"] = localeId

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 200:
      print(
        f"Error fetching pages.\n" +
        f"Status code: {response.status_code}." +
        f"Response logged in {ERROR_FILENAME}."
      )
      with open(ERROR_FILENAME, 'w') as f:
        json.dump(response.json(), f)
      response.raise_for_status()

    pages = response.json()['pages']
    all_pages.extend(pages)

    if len(pages) < limit:
      break

    offset += limit

  return all_pages