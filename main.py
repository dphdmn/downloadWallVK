import requests
import json
import time
import argparse

def get_wall_posts(access_token, domain, count, offset, version):
    url = 'https://api.vk.com/method/wall.get'
    params = {
        'access_token': access_token,
        'domain': domain,
        'count': count,
        'offset': offset,
        'v': version
    }
    response = requests.get(url, params=params)
    return response.json()

def download_wall_posts(access_token, domain, version, count=100):
    offset = 0
    all_posts = []

    while True:
        response = get_wall_posts(access_token, domain, count, offset, version)
        posts = response.get('response', {}).get('items', [])

        if not posts:
            break

        all_posts.extend(posts)
        offset += count
        print(f'Downloaded {len(posts)} posts, total posts: {len(all_posts)}')
        
        # Sleep to avoid hitting rate limits
        time.sleep(1)

    return all_posts

def save_posts_to_file(posts, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download VK wall posts.')
    parser.add_argument('--access_token', type=str, required=True, help='VK access token')
    parser.add_argument('--domain', type=str, required=True, help='VK group domain name')
    args = parser.parse_args()

    posts = download_wall_posts(args.access_token, args.domain, '5.199')
    save_posts_to_file(posts, 'wall_posts.json')
    print(f'Saved {len(posts)} posts to wall_posts.json')
