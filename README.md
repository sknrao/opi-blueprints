# OPI Blueprint Tracking

This folder contains the blueprint registry and dashboard for the OPI Project.

## Files

| File | Purpose |
|------|---------|
| `blueprints.yaml` | **The source of truth.** Edit this to add or update blueprints. |
| `index.html` | GitHub Pages dashboard — reads `blueprints.yaml` live in the browser. |
| `BLUEPRINTS.md` | Auto-generated Markdown summary (updated by GitHub Actions on every push). |
| `.github/workflows/update-blueprints.yml` | Workflow that regenerates `BLUEPRINTS.md` when `blueprints.yaml` changes. |
| `.github/scripts/generate_blueprints_md.py` | Python script used by the workflow. |

## How to add a blueprint

1. Open `blueprints.yaml`
2. Copy an existing entry as a template
3. Fill in your blueprint's details (use the next `BP-NNN` ID)
4. Set `stage: proposed`
5. Open a PR — the dashboard will update automatically when merged

## Stages

```
proposed → tsc_review → build → validate → published
```

## GitHub Pages setup

1. Go to **Settings → Pages** in the `opiproject/opi` repo
2. Set source to **Deploy from a branch**
3. Select branch `main`, folder `/blueprints`
4. The dashboard will be live at `https://opiproject.github.io/opi/blueprints/`
