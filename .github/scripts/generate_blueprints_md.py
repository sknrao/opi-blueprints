#!/usr/bin/env python3
"""
Generate BLUEPRINTS.md from blueprints/blueprints.yaml.
Run by GitHub Actions whenever blueprints.yaml changes.
"""

import yaml
from pathlib import Path
from datetime import date

YAML_PATH = Path("blueprints/blueprints.yaml")
OUT_PATH  = Path("BLUEPRINTS.md")

STAGE_LABELS = {
    "proposed":   "📋 Proposed",
    "tsc_review": "🔍 TSC Review",
    "build":      "🔨 Build & Document",
    "validate":   "🧪 Validate",
    "published":  "✅ Published",
}

STAGE_ORDER = ["proposed", "tsc_review", "build", "validate", "published"]

DELIVERABLE_KEYS = [
    "reference_architecture",
    "bill_of_materials",
    "deployment_guide",
    "use_case_narrative",
    "validation_results",
]

def progress_bar(done: int, total: int) -> str:
    filled = round(done / total * 10) if total else 0
    return "█" * filled + "░" * (10 - filled) + f" {done}/{total}"

def partner_names(partners: list) -> str:
    return ", ".join(p.get("name", "") for p in partners) if partners else "—"

def main():
    with open(YAML_PATH) as f:
        data = yaml.safe_load(f)

    blueprints = data.get("blueprints", [])

    # Stats
    total      = len(blueprints)
    published  = sum(1 for b in blueprints if b.get("stage") == "published")
    in_progress = sum(1 for b in blueprints if b.get("stage") in {"tsc_review", "build", "validate"})
    partners   = {p["name"] for b in blueprints for p in b.get("partners", [])}

    lines = [
        "<!-- AUTO-GENERATED — do not edit manually. Edit blueprints/blueprints.yaml instead. -->",
        "",
        "# OPI Blueprint Dashboard",
        "",
        f"> Last updated: {date.today().isoformat()}",
        "",
        "## Summary",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Total blueprints | {total} |",
        f"| Published | {published} |",
        f"| In progress | {in_progress} |",
        f"| Partners involved | {len(partners)} |",
        "",
        "---",
        "",
        "## Pipeline",
        "",
    ]

    # Group by stage
    by_stage = {s: [] for s in STAGE_ORDER}
    for b in blueprints:
        stage = b.get("stage", "proposed")
        if stage in by_stage:
            by_stage[stage].append(b)

    for stage in STAGE_ORDER:
        items = by_stage[stage]
        label = STAGE_LABELS[stage]
        lines.append(f"### {label} ({len(items)})")
        lines.append("")

        if not items:
            lines.append("_No blueprints in this stage._")
            lines.append("")
            continue

        lines.append("| ID | Title | Category | Partners | Progress | Updated |")
        lines.append("|----|-------|----------|----------|----------|---------|")

        for b in items:
            delivs = b.get("deliverables", {})
            done   = sum(1 for k in DELIVERABLE_KEYS if delivs.get(k))
            total_d = len(DELIVERABLE_KEYS)
            bar    = progress_bar(done, total_d)
            issue  = b.get("links", {}).get("github_issue", "")
            id_str = f"[{b['id']}]({issue})" if issue else b["id"]

            lines.append(
                f"| {id_str} "
                f"| {b['title']} "
                f"| {b.get('category','—')} "
                f"| {partner_names(b.get('partners',[]))} "
                f"| `{bar}` "
                f"| {b.get('updated','—')} |"
            )
        lines.append("")

    # Full detail section
    lines += [
        "---",
        "",
        "## Blueprint Details",
        "",
    ]

    for b in blueprints:
        delivs  = b.get("deliverables", {})
        issue   = b.get("links", {}).get("github_issue", "")
        docs    = b.get("links", {}).get("documentation", "")
        links   = []
        if issue: links.append(f"[GitHub Issue]({issue})")
        if docs:  links.append(f"[Documentation]({docs})")

        lines += [
            f"### {b['id']} — {b['title']}",
            "",
            f"**Stage:** {STAGE_LABELS.get(b.get('stage','proposed'), b.get('stage',''))}  ",
            f"**Category:** {b.get('category','—')}  ",
            f"**Submitted:** {b.get('submitted','—')}  ",
            f"**Updated:** {b.get('updated','—')}  ",
            "",
            f"**Use case:** {b.get('use_case','').strip()}",
            "",
            f"**Target persona:** {b.get('target_persona','—')}",
            "",
            "**Partners:**",
            "",
        ]
        for p in b.get("partners", []):
            role = f" — {p['role']}" if p.get("role") else ""
            lines.append(f"- {p['name']}{role}")

        lines += [
            "",
            "**Hardware:** " + ", ".join(b.get("hardware", [])),
            "",
            "**OPI components:** " + ", ".join(b.get("opi_components", [])),
            "",
            "**Deliverables:**",
            "",
        ]
        for k in DELIVERABLE_KEYS:
            status = "✅" if delivs.get(k) else "⬜"
            label  = k.replace("_", " ").title()
            lines.append(f"- {status} {label}")

        if b.get("notes"):
            lines += ["", f"**Notes:** {b['notes']}"]

        if links:
            lines += ["", "**Links:** " + " · ".join(links)]

        lines += ["", "---", ""]

    OUT_PATH.write_text("\n".join(lines))
    print(f"✓ Written {OUT_PATH} ({len(blueprints)} blueprints)")

if __name__ == "__main__":
    main()
