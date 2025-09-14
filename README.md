# MiniDyno (repo-ready)
MiniDyno is a full-featured Discord moderation system (bot + REST API + Dashboard) packaged to be ready-to-publish to GitHub.

## What this repo contains
- Python bot (py-cord) with automod, escalation, temp punishments, scheduler
- FastAPI dashboard (Jinja2 templates + Chart.js stub)
- SQLite DB schema and helpers (`core/`)
- Full builder support: Make, Ninja, Meson, CMake, Bazel, Buck, Docker, Nix, Guix
- Language wrappers: Node/Go/Rust (simple launchers that call the API)
- .gitignore, LICENSE, config.example.json and run instructions

## Quickstart (local)
1. Copy `config.example.json` → `config.json` and fill in your Discord bot token and secrets. (just skip this step because I renamed the file)
2. Create and activate Python 3.13.7 venv:
   ```bash
   python3.13 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run the bot (starts bot and API):
   ```bash
   python bot.py
   ```
4. Open Dashboard: http://127.0.0.1:8000/

## How to publish
```bash
git init
git add .
git commit -m "Initial MiniDyno import"
# create repo on GitHub and push to it
git remote add origin https://github.com/<your-user>/MiniDyno.git
git branch -M main
git push -u origin main
```

## Notes
- This repo is intended to be a starting point. Review config and secure secrets before deploying publicly.
