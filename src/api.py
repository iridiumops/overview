import requests
from datetime import datetime, timezone, timedelta
from joblib import Memory, expires_after
import dir_paths

"""
basic api client for retrieving overview related info from esi api
"""

client_version = "1.1.1"
api_base_url = "https://esi.evetech.net"
api_timeout = 10
api_headers = {
    'User-agent' : 'overview/'+client_version+' github.com/iridiumops/overview iridiumops@gmail.com',
    'Cache-Control' : 'no-cache',
    'Accept-Encoding' : 'gzip',
    'Accept' : 'application/json',
    'Accept-Language' : 'en',
    'X-Compatibility-Date' : '2026-07-21',
}
cache_location = dir_paths.temp_dir / "cache"
cache_location.mkdir(parents=True, exist_ok=True)
cache_memory = Memory(cache_location, verbose=0)
logs_location = dir_paths.temp_dir / "logs"
logs_location.mkdir(parents=True, exist_ok=True)
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')  # noqa: DTZ005
error_log_file = logs_location / f"error_{timestamp}.log"


def expire_at_downtime(metadata):
    """Better alternative to expires_after(hours=23, minutes=59) for daily data"""

    # calculate cutoff (invalidation) time relative to current time from specific time
    now_utc = datetime.now(timezone.utc)
    cutoff_utc = now_utc.replace(hour=11, minute=5, second=0, microsecond=0) # eve downtime time as per esi api specs
    if now_utc < cutoff_utc:
        cutoff_utc = cutoff_utc - timedelta(days=1)
        
    # ensure joblib metadata timestamp is UTC based
    cached_time_utc = datetime.fromtimestamp(metadata["time"], tz=timezone.utc)
    
    # compare time (true means valid cache)
    return cached_time_utc > cutoff_utc


def clean_cache():
    """Trigger cache garbage collection to prevent accumulation of cached data in temp dir"""
    cache_memory.reduce_size()


def handle_request_error(e, context_msg):
    """Helper to display errors and log them"""
    
    if isinstance(e, requests.exceptions.HTTPError) and \
    isinstance(e.response, requests.Response) and \
    isinstance(e.request, requests.Response):
        status_code = e.response.status_code
        error_text = e.response.text
        headers = dict(e.response.headers)

        if status_code == 429:
            retry_after = headers.get('Retry-After', 'unknown')
            error_message = f"{context_msg} ({e.request.url}): Rate limited (HTTP 429). Retry after: {retry_after}s"
        else:
            error_message = f"{context_msg} ({e.request.url}): HTTP Error {status_code}: {error_text}"
            error_message += f"\nHeaders: {headers}"

    elif isinstance(e, requests.exceptions.RequestException) and \
    isinstance(e.request, requests.Response):
        error_message = f"{context_msg} ({e.request.url}): Request Error: {e}"
    else:
        error_message = f"{context_msg}: Unexpected Error: {e}"

    print(error_message)

    with open(error_log_file, 'a') as file:
        file.write(error_message + "\n")


@cache_memory.cache(cache_validation_callback=expire_at_downtime)
def get_category_ids():
    """Fetch all category IDs"""
    try:
        response = requests.get(
            f"{api_base_url}/universe/categories/",
            timeout=api_timeout, 
            headers=api_headers
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        handle_request_error(e, "Error fetching categories")
        return None

@cache_memory.cache
def get_category(category_id: int):
    """Fetch category details for a given category ID."""
    try:
        response = requests.get(
            f"{api_base_url}/universe/categories/{category_id}/",
            timeout=api_timeout, 
            headers=api_headers
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        handle_request_error(e, f"Error fetching category {category_id}")
        return None


@cache_memory.cache(cache_validation_callback=expire_at_downtime)
def get_group_ids():
    """Fetch all group IDs, handling multi-page responses"""
    try:
        response = requests.get(
            f"{api_base_url}/universe/groups/",
            timeout=api_timeout, 
            headers=api_headers
        )
        response.raise_for_status()
        groups = response.json()
        
        # handle pagination
        total_pages = int(response.headers.get('X-Pages', 1)) # total pages, default 1
        if total_pages > 1:
            for page in range(2, total_pages + 1, 1): # loop over all remaining pages
                response = requests.get(
                    f"{api_base_url}/universe/groups/?page={page}",
                    timeout=api_timeout, 
                    headers=api_headers
                )
                response.raise_for_status()
                groups.extend(response.json())
        
        return groups
    except Exception as e:
        handle_request_error(e, "Error fetching groups")
        return None


@cache_memory.cache
def get_group(group_id: int):
    """Fetch group details for a given group ID."""
    try:
        response = requests.get(
            f"{api_base_url}/universe/groups/{group_id}/",
            timeout=api_timeout, 
            headers=api_headers
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        handle_request_error(e, f"Error fetching group {group_id}")
        return None
