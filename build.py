import markdown
import frontmatter
import os
import shutil
from datetime import date as date_type

def format_date(d):
    if isinstance(d, date_type):
        return f'<time datetime="{d.isoformat()}">{d.strftime("%B %d, %Y")}</time>'
    return str(d)

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
        raw_category = post.get('category', 'General')
        categories = [raw_category] if isinstance(raw_category, str) else list(raw_category)
        abstract = post.get('abstract', '')
        status = post.get('status', 'visible')

        # MD to HTML
        html_body = markdown.markdown(post.content, extensions=['extra', 'nl2br'])

        tags_html = ''.join(f'<span class="post-tag">{c}</span>' for c in categories)
        post_header = (
            f"<header class='post-title'>"
            f"<h1>{title}</h1>"
            f"<p class='post-header-meta'>{format_date(date)}"
            f"<span class='post-tags'>{tags_html}</span></p>"
            f"</header>"
        )
        full_html = template.replace('{{content}}', post_header + html_body)

        title_and_meta = f'<title>{title} | HMD\'s Dev Terminal</title>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">'
        full_html = full_html.replace('{{title}}', title_and_meta)

        output_name = filename.replace('.md', '.html')
        with open(f'dist/{output_name}', 'w') as f:
            f.write(full_html)

        # Hide unlisted posts
        if status != 'unlisted':
            posts_metadata.append({
                'title': title,
                'date': date,
                'url': output_name,
                'categories': categories,
                'abstract': abstract,
            })

# Sort posts by date, newest first
posts_metadata.sort(key=lambda x: x['date'], reverse=True)

# Generate index.html (homepage)
cards_html = "<h1>Posts</h1><div class='posts-list'>"
for p in posts_metadata:
    tags_html = ''.join(f'<span class="post-tag">{c}</span>' for c in p['categories'])
    abstract_html = f'<p class="post-abstract">{p["abstract"]}</p>' if p['abstract'] else ''
    cards_html += (
        f'<article class="post-card">'
        f'<div class="post-card-meta">'
        f'<span class="post-date">{format_date(p["date"])}</span>'
        f'<span class="post-tags">{tags_html}</span>'
        f'</div>'
        f'<h2><a href="{p["url"]}">{p["title"]}</a></h2>'
        f'{abstract_html}'
        f'</article>'
    )
cards_html += "</div>"

with open('dist/index.html', 'w') as f:
    f.write(template.replace('{{content}}', cards_html).replace('{{title}}', ''))

# Update assets/ into dist/
if os.path.exists('assets'):
    if os.path.exists('dist/assets'):
        shutil.rmtree('dist/assets')
    shutil.copytree('assets', 'dist/assets')
