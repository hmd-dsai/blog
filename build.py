import markdown
import os

# Create an 'output' directory if it doesn't exist
if not os.path.exists('dist'):
    os.makedirs('dist')

# Load the HTML template
with open('templates/base.html', 'r') as f:
    template = f.read()

# Convert all posts
for filename in os.listdir('posts-md'):
    if filename.endswith('.md'):
        with open(f'posts-md/{filename}', 'r') as f:
            content = f.read()
            # Convert Markdown to HTML
            html_body = markdown.markdown(content)
            
            # Fill the template
            final_html = template.replace('{{content}}', html_body)
            
            # Save to the dist folder (rename .md to .html)
            output_path = f"dist/{filename.replace('.md', '.html')}"
            with open(output_path, 'w') as f:
                f.write(final_html)

print("Build complete! Files are in /dist")