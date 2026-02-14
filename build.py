import markdown
import frontmatter
import os
import shutil

# Ensure directories exist
os.makedirs('dist', exist_ok=True)

with open('templates/base.html', 'r') as f:
    template = f.read()

posts_metadata = []

# Process Markdown files
for filename in os.listdir('posts-md'):
    if filename.endswith('.md'):
        # Parse the file with frontmatter
        post = frontmatter.load(f'posts-md/{filename}')
        
        # Access metadata (using .get() to avoid errors if a field is missing)
        title = post.get('title', filename.replace('.md', ''))
        date = post.get('date', 'Unknown Date')
        category = post.get('category', 'General')
        
        # Convert content to HTML (added 'extra' for tables/fenced code)
        html_body = markdown.markdown(post.content, extensions=['extra'])
        
        # Combine metadata + body for the post page
        post_header = f"<header><h1>{title}</h1><p>{date} | {category}</p></header>"
        full_html = template.replace('{{content}}', post_header + html_body)
        
        output_name = filename.replace('.md', '.html')
        with open(f'dist/{output_name}', 'w') as f:
            f.write(full_html)
            
        posts_metadata.append({'title': title, 'date': str(date), 'url': output_name})

# Sort posts by date (newest first)
posts_metadata.sort(key=lambda x: x['date'], reverse=True)

# Generate index.html (Homepage)
links_html = "<h1>Blog Posts</h1><ul>"
for p in posts_metadata:
    links_html += f'<li>{p["date"]} - <a href="{p["url"]}">{p["title"]}</a></li>'
links_html += "</ul>"

with open('dist/index.html', 'w') as f:
    f.write(template.replace('{{content}}', links_html))

# Copy the assets folder into dist
if os.path.exists('assets'):
    # If dist/assets exists from a previous run, delete it first to stay fresh
    if os.path.exists('dist/assets'):
        shutil.rmtree('dist/assets')
    shutil.copytree('assets', 'dist/assets')