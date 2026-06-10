import requests
from joblib import Memory, expires_after
import dir_paths

"""
basic api client for retrieving overview related info from esi api
"""

client_version = "1.1.0"
api_base_url = "https://esi.evetech.net"
api_timeout = 10
api_headers = {
    'User-agent' : 'overview/'+client_version+' github.com/iridiumops/overview iridiumops@gmail.com',
    'Cache-Control' : 'no-cache',
    'Accept-Encoding' : 'gzip',
    'Accept' : 'application/json',
}
cache_location = dir_paths.temp_dir / "cache"
cache_memory = Memory(cache_location, verbose=0)


@cache_memory.cache(cache_validation_callback=expires_after(hours=23))
def get_category_ids():
    """Fetch all category IDs"""
    try:
        response = requests.get(
            f"{api_base_url}/universe/categories/",
            timeout=api_timeout, 
            headers={**api_headers, 'X-Compatibility-Date':'2026-06-09'}
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching categories: {e}")
        return None


@cache_memory.cache
def get_category(category_id: int):
    """Fetch category details for a given category ID."""
    try:
        response = requests.get(
            f"{api_base_url}/universe/categories/{category_id}/",
            timeout=api_timeout, 
            headers={**api_headers, 'X-Compatibility-Date':'2026-06-09'}
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching category {category_id}: {e}")
        return None


@cache_memory.cache(cache_validation_callback=expires_after(hours=23))
def get_group_ids():
    """Fetch all group IDs, handling multi-page responses"""
    try:
        response = requests.get(
            f"{api_base_url}/universe/groups/",
            timeout=api_timeout, 
            headers={**api_headers, 'X-Compatibility-Date':'2026-06-09'}
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
                    headers={**api_headers, 'X-Compatibility-Date':'2026-06-09'}
                )
                response.raise_for_status()
                groups.extend(response.json())
        
        return groups
    except Exception as e:
        print(f"Error fetching groups: {e}")
        return None


@cache_memory.cache
def get_group(group_id: int):
    """Fetch group details for a given group ID."""
    try:
        response = requests.get(
            f"{api_base_url}/universe/groups/{group_id}/",
            timeout=api_timeout, 
            headers={**api_headers, 'X-Compatibility-Date':'2026-06-09'}
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching group {group_id}: {e}")
        return None
