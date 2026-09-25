# Setup Guide — AICP GitHub Profile + Pages Dashboard

## What's in this package

```
aicp-github/
├── README.md              ← Profile README (renders on github.com/faridbarahimi)
├── assets/                ← 6 custom SVG diagrams used by README.md
│   ├── aicp-hero.svg
│   ├── aicp-architecture.svg
│   ├── aicp-execution.svg
│   ├── aicp-routing.svg
│   ├── aicp-workers.svg
│   └── aicp-worker-continuity.svg
├── docs/
│   ├── index.html          ← Full live-style dashboard (deployed via GitHub Pages)
│   ├── style.css            ← Dark/neon theme styling
│   └── assets/               ← reserved for future icons/images
└── SETUP.md                 ← this file
```

All SVGs are real, rendered assets — every image referenced by `README.md` now exists in `assets/` and has been validated as well-formed, UTF-8 XML.

---

## 1. Deploy from your VPS (matches your current setup)

Your VPS already has `faridbarahimi/faridbarahimi` cloned at
`/home/ubuntu/projects/faridbarahimi`, with `origin` pointed at
`git@github.com:faridbarahimi/faridbarahimi.git` over SSH, authenticated,
and the repo is currently empty on branch `main`. To publish this package:

```bash
# On the VPS
cd /home/ubuntu/projects/faridbarahimi

# Copy every file from this package into the repo root
cp -r /path/to/aicp-github/README.md .
cp -r /path/to/aicp-github/assets .
cp -r /path/to/aicp-github/docs .
cp /path/to/aicp-github/SETUP.md .

git add -A
git commit -m "Add AICP profile README and Pages dashboard"
git push origin main
```

Since the repo is a special "profile" repo (name matches your username),
GitHub automatically renders `README.md` at the top of your profile page
as soon as this push lands — no extra configuration needed for that part.

---

## 2. Enable GitHub Pages (for the full dashboard)

The `docs/` folder holds a richer, full-page version of the dashboard
(the one that most closely mirrors your reference image). To make it live:

1. On GitHub: **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: `main`
4. Folder: `/docs`
5. Save

After a few minutes it will be live at:

```
https://faridbarahimi.github.io/faridbarahimi/
```

`README.md` already links to this URL, so once Pages is enabled the link
on your profile becomes active automatically.

---

## 3. Verify after pushing

- Open `https://github.com/faridbarahimi` and confirm the README renders
  with all 6 diagrams visible (no broken image icons).
- Open the Pages URL above and confirm the dashboard loads with fonts,
  layout and the animated stat glow working.
- If any image looks broken, it is almost always a path/case-sensitivity
  issue — GitHub's filesystem is case-sensitive, so filenames must match
  exactly (`assets/aicp-hero.svg`, not `Assets/AICP-Hero.svg`).

---

## 4. Notes on the design

- Dark navy background with indigo → cyan gradient accents, matching your
  reference image's palette.
- All 6 diagrams are hand-built, real SVG (not screenshots), so they stay
  crisp at any size and load instantly with no external dependencies.
- `docs/index.html` is fully self-contained (Google Fonts + inline CSS/SVG),
  responsive down to mobile, and includes a subtle live-glow animation on
  the stat numbers.
- GitHub stats badges (`github-readme-stats`, streak stats) in `README.md`
  pull live data automatically once the repo is public — no setup required.

---

## 5. If you want further changes

Real-time numbers wired to the GitHub API, a real contribution heatmap,
additional icons, or a different color direction — all are straightforward
follow-ups. Just say the word.

---

**Good luck.**
AICP · AI should work.
