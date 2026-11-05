# foodserv.az

Static, dependency-free one-page website for GitHub Pages. AZ / EN / RU switch instantly in place (no reload).

## Deploy
1. Upload everything in this folder to the root of your GitHub repository (branch `main`).
2. Settings → Pages → Source: *Deploy from a branch* → `main` / `(root)`.
3. `CNAME` already points to `foodserv.az`.

## Edit text, phone, links
All copy and contact details live in `build/build.py` (`TEXT`, `PHONE`, `WA`, `REQUEST`).
After editing run `python3 build/build.py` — it regenerates `index.html` (all three languages are inside it) and `sitemap.xml`.

## Structure
- `assets/css/style.css`, `assets/js/main.js`: styling and interaction
- `assets/favicon.svg`: icon (replace with your real logo if you have one)

## Logo
Save your logo as `assets/logo.png` (transparent background, at least 400 px wide). The site uses it automatically in the header and footer; without the file it shows a text wordmark.
On the dark hero and footer the logo is shown in white automatically. If your logo has several colors you want to keep, delete the line with `filter:brightness(0) invert(1)` in `assets/css/style.css`.

## Photos
Add your photos to `assets/img/` using the names in `assets/img/README.txt`. Missing photos are hidden automatically.
