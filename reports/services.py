import requests
from django.conf import settings

BASE_URL = settings.NODE_API_BASE_URL
TIMEOUT = 5

def fetch_users():
    r = requests.get(f"{BASE_URL}/users",headers={"Content-Type": "application/json","Accept": "application/json","X-USER-TYPE":"admin"}, timeout=TIMEOUT)
    r.raise_for_status()
    return r.json()

def fetch_videos(search=None, category=None):
    params = {}
    if search: params["search"] = search
    if category: params["category"] = category
    r = requests.get(f"{BASE_URL}/videos", params=params, headers={"Content-Type": "application/json","Accept": "application/json","X-USER-TYPE":"admin"}, timeout=TIMEOUT)
    r.raise_for_status()
    return r.json()

def fetch_user_by_id(user_id: int):
    # If Node doesn’t have /users/:id, filter locally
    users = fetch_users()
    for u in users['users']:
        if u.get("id") == user_id:
            return u
    return None

def fetch_user_videos(user_id: int):
    videos = fetch_videos()
    return [v for v in videos['videos'] if v.get("userId") == user_id]