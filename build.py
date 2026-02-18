import markdown
import frontmatter
import os
import shutil

os.makedirs('dist', exist_ok=True)

with open('templates/base.html', 'r') as f:
    template = f.read()

posts_metadata = []

# Process Markdown files
for filename in os.listdir('posts-md'):
    if filename.endswith('.md'):
        # Extract frontmatter
        post = frontmatter.load(f'posts-md/{filename}')
        
        title = post.get('title', filename.replace('.md', ''))
        date = post.get('date', 'Unknown Date')
        category = post.get('category', 'General')
        status = post.get('status', 'visible')

        # MD to HTML
        html_body = markdown.markdown(post.content, extensions=['extra', 'nl2br'])
        
        post_header = f"<header class='post-title'><h1>{title}</h1><p>{date} | {category}</p></header>"
        full_html = template.replace('{{content}}', post_header + html_body)
        
        output_name = filename.replace('.md', '.html')
        with open(f'dist/{output_name}', 'w') as f:
            f.write(full_html)
        
        # Hide unlisted posts
        if status != 'unlisted':
            posts_metadata.append({'title': title, 'date': str(date), 'url': output_name})

# Sort posts by date, newest first
posts_metadata.sort(key=lambda x: x['date'], reverse=True)

# Generate index.html (homepage)
links_html = "<h1>My Blog Posts</h1><ul>"
for p in posts_metadata:
    links_html += f'<li>{p["date"]} - <a href="{p["url"]}">{p["title"]}</a></li>'
links_html += "</ul>"

with open('dist/index.html', 'w') as f:
    f.write(template.replace('{{content}}', links_html))

# Update assets/ into dist/
if os.path.exists('assets'):
    if os.path.exists('dist/assets'):
        shutil.rmtree('dist/assets')
    shutil.copytree('assets', 'dist/assets')