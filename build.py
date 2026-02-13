import markdown
import os

if not os.path.exists('dist'):
    os.makedirs('dist')

with open('templates/base.html', 'r') as f:
    template = f.read()

# 1. New: List to store post info for the homepage
posts_metadata = []

for filename in os.listdir('posts-md'):
    if filename.endswith('.md'):
        with open(f'posts-md/{filename}', 'r') as f:
            content = f.read()
            html_body = markdown.markdown(content)
            
            final_html = template.replace('{{content}}', html_body)
            
            output_filename = filename.replace('.md', '.html')
            output_path = f"dist/{output_filename}"
            
            with open(output_path, 'w') as f:
                f.write(final_html)
            
            # 2. New: Save the filename and a clean title for the index
            clean_title = filename.replace('.md', '').replace('-', ' ').title()
            posts_metadata.append({'title': clean_title, 'url': output_filename})

# 3. New: Generate index.html
links_html = "<h1>My Blog Posts</h1><ul>"
for post in posts_metadata:
    links_html += f'<li><a href="{post["url"]}">{post["title"]}</a></li>'
links_html += "</ul>"

index_html = template.replace('{{content}}', links_html)
with open('dist/index.html', 'w') as f:
    f.write(index_html)

print(f"Build complete! Generated {len(posts_metadata)} posts + index.html")