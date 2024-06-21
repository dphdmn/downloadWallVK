import json
from datetime import datetime

# Load the JSON data from the file
with open('wall_posts.json', 'r', encoding='utf-8') as file:
    posts = json.load(file)

# Function to convert Unix timestamp to desired format
def convert_timestamp(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d (%H:%M)')

# Separate posts into two categories and sort them by date (oldest to newest)
sorted_posts = sorted(posts, key=lambda x: x['date'])

# Function to format the post data
def format_post(post, post_id, include_attachments=False):
    formatted_post = f"Post #{post_id}\nDate: {convert_timestamp(post['date'])}\n{post['text']}\n"
    
    photo_attachments = []
    music_attachments = []
    document_attachments = []
    other_attachments = []
    
    if include_attachments:
        for attachment in post['attachments']:
            if attachment['type'] == 'photo':
                photo_url = attachment['photo']['sizes'][-1]['url']
                photo_attachments.append(photo_url)
            elif attachment['type'] == 'audio':
                artist = attachment['audio']['artist']
                title = attachment['audio']['title']
                duration = str(datetime.utcfromtimestamp(attachment['audio']['duration']).strftime('%M:%S'))
                url = attachment['audio'].get('url', 'URL not available')
                music_info = f"{artist} - {title} ({duration}) - {url}"
                music_attachments.append(music_info)
            elif attachment['type'] == 'doc':
                doc_url = attachment['doc']['url']
                document_attachments.append(doc_url)
            else:
                other_attachments.append(attachment)

        if photo_attachments:
            formatted_post += "##Photos##:\n" + '\n'.join(photo_attachments) + '\n'
        if music_attachments:
            formatted_post += "##Music##:\n" + '\n'.join(music_attachments) + '\n'
        if document_attachments:
            formatted_post += "##Documents##:\n" + '\n'.join(document_attachments) + '\n'
        if other_attachments:
            formatted_post += "##Other Attachments##:\n" + json.dumps(other_attachments, indent=4) + '\n'
    formatted_post += "###########################\n\n"
    return formatted_post, photo_attachments, music_attachments, document_attachments

# Variables to store all attachment links
all_photo_links = []
all_music_links = []
all_doc_links = []

# Write the posts to a single file
with open('export.txt', 'w', encoding='utf-8') as export_file:
    for idx, post in enumerate(sorted_posts, start=1):
        formatted_post, photo_links, music_links, doc_links = format_post(post, idx, include_attachments=True if post['attachments'] else False)
        export_file.write(formatted_post)
        
        # Add attachments to the lists
        for link in photo_links:
            all_photo_links.append(f"Post #{idx} Date: {convert_timestamp(post['date'])} - {link}")
        for link in music_links:
            all_music_links.append(f"Post #{idx} Date: {convert_timestamp(post['date'])} - {link}")
        for link in doc_links:
            all_doc_links.append(f"Post #{idx} Date: {convert_timestamp(post['date'])} - {link}")

# Write the attachment links to a separate file
with open('attachment_links.txt', 'w', encoding='utf-8') as attach_file:
    if all_photo_links:
        attach_file.write("##Photo Links##:\n" + '\n'.join(all_photo_links) + '\n\n')
    if all_music_links:
        attach_file.write("##Music Links##:\n" + '\n'.join(all_music_links) + '\n\n')
    if all_doc_links:
        attach_file.write("##Document Links##:\n" + '\n'.join(all_doc_links) + '\n\n')
