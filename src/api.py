#imports
import requests
from joblib import Memory, expires_after
from dir_paths import temp_dir

"""extremely basic interface for some eve esi rest api routes"""

cache_location = temp_dir / "cache"
cache_memory = Memory(cache_location, verbose=0)

api_base_url = "https://esi.evetech.net"
api_timeout = 10


@cache_memory.cache(cache_validation_callback=expires_after(hours=23))
def api_get_category_ids():
    """Fetch all category IDs"""
    try:
        response = requests.get(f"{api_base_url}/universe/categories/", timeout=api_timeout)
        response.raise_for_status()
        categories = response.json()
    except Exception as e:
        print(f"Error fetching categories: {e}")
    return categories


@cache_memory.cache
def api_get_category(category_id: int):
    """Fetch category details for a given category ID."""
    try:
        response = requests.get(f"{api_base_url}/universe/categories/{category_id}/", timeout=api_timeout)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching category {category_id}: {e}")
        return None


@cache_memory.cache(cache_validation_callback=expires_after(hours=23))
def api_get_group_ids():
    """Fetch all group IDs, handling multi-page responses"""
    try:
        response = requests.get(f"{api_base_url}/universe/groups/", timeout=api_timeout)
        response.raise_for_status()
        groups = response.json()
        
        # handle pagination
        total_pages = int(response.headers.get('X-Pages', 1)) # total pages, default 1
        if total_pages > 1:
            for page in range(2, total_pages + 1, 1): # loop over all remaining pages
                response = requests.get(f"{api_base_url}/universe/groups/?page={page}", timeout=api_timeout)
                response.raise_for_status()
                groups.extend(response.json())
        
        return groups
    except Exception as e:
        print(f"Error fetching groups: {e}")
        return None


@cache_memory.cache
def api_get_group(group_id: int):
    """Fetch group details for a given group ID."""
    try:
        response = requests.get(f"{api_base_url}/universe/groups/{group_id}/", timeout=api_timeout)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching group {group_id}: {e}")
        return None
