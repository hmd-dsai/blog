# Blog

Source code for my GitHub-hosted blog.

## Mechanism
- `posts-md/`: My raw blogposts, written in markdown format with frontmatter (metadata).
- `templates/` Base HTML boilerplate.
- `assets/`: CSS + media files.
- `build.py`: Initiate HTML for landing page + Convert markdowns to HTML format for blogpost pages.
- `.github/`: Deploy using GitHub Actions.

## Tech Stack
- **Language:** Python 3.x
- **Libraries:** `markdown`, `python-frontmatter`
- **Automation:** GitHub Actions (CI/CD)
- **Styling:** new.css (Classless CSS)

## How to build locally
1. Install dependencies: `pip install markdown python-frontmatter`
2. Run the generator: `python build.py`
3. View the result in the `dist/` folder.

## Final Product
View my blog here: <https://hmd-dsai.github.io/blog/>.