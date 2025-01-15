import requests
import json

ERROR_FILENAME = "latest_error.json"

def list_pages(api_token, site_id, localeId=None):
  """
  Fetches a list of pages from a Webflow site.

  Args:
    api_token (str): The API key for authentication.
    site_id (str): The ID of the Webflow site.
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
    "Authorization": f"Bearer {api_token}"
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
        f"Status code: {response.status_code}.\n" +
        f"Response saved in \"{ERROR_FILENAME}\".\n"
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

def update_page(api_token, page_id, fields):
  """
  Updates a page metadata on a Webflow site.

  Args:
    api_token (str): The API key for authentication.
    page_id (str): The ID of the page to update.
    fields (dict): A dictionary of fields to update on the page.
  Returns:
    dict: The updated page data.
  Raises:
    requests.exceptions.HTTPError: If the request to the Webflow API fails.
  Notes:
    The function sends a PATCH request to the Webflow API to update the
    specified page with the provided fields. If an error occurs during the
    request, the response is logged to a file specified by ERROR_FILENAME.
  """
  url = f"https://api.webflow.com/v2/pages/{page_id}"
  headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
  }

  response = requests.patch(url, headers=headers, data=json.dumps(fields))

  if response.status_code != 200:
    print(
      f"Error updating page.\n" +
      f"Status code: {response.status_code}.\n" +
      f"Response saved in \"{ERROR_FILENAME}\".\n"
    )
    with open(ERROR_FILENAME, 'w') as f:
      json.dump(response.json(), f)
  response.raise_for_status()

  return response.json()