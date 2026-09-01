#!/usr/bin/env python3
"""
Dynamic GitHub Profile README Updater for levi-qiao
Fetches public repositories from GitHub API and updates the Selected Work section in README.md.
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request

USERNAME = os.environ.get("GITHUB_REPOSITORY_OWNER") or os.environ.get("GITHUB_USERNAME") or "levi-qiao"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

# Repositories to exclude from the showcase (e.g. profile repo, empty test/archived repos)
EXCLUDED_REPOS = {
    USERNAME.lower(),
    "levi-qiao",
    "ai-tools",
    "cn-tax-crawler",
    "ai-train",
    "sherlock-qwen",
    "visa-rpa",
    "x-nan-site",
    "cit-workbench",
    "octopus",
}

# Optional custom display emojis for key projects
REPO_EMOJIS = {
    "longgraph-skill": "🐙",
    "herdr-agent-quota": "⚡",
    "obsidian-llm-wiki": "🧠",
    "sherlock-claude": "🔍",
    "dsh-plugin-longgraph": "🧩",
    "agent-ding": "🔔",
}

START_TAG = "<!-- REPOS_START -->"
END_TAG = "<!-- REPOS_END -->"
README_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "README.md")


def fetch_repos():
    url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&type=owner&sort=updated"
    req = urllib.request.Request(url)
    req.add_header("User-Agent", f"{USERNAME}-profile-updater")
    req.add_header("Accept", "application/vnd.github.v3+json")
    if GITHUB_TOKEN:
        req.add_header("Authorization", f"Bearer {GITHUB_TOKEN}")

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data
    except urllib.error.URLError as e:
        print(f"Error fetching repos from GitHub API: {e}", file=sys.stderr)
        return None


def generate_markdown_table(repos):
    # Filter public, non-fork, non-archived, meaningful repos with descriptions
    filtered = []
    for r in repos:
        name = r.get("name", "")
        if r.get("fork") or r.get("archived") or r.get("private"):
            continue
        if name.lower() in EXCLUDED_REPOS:
            continue
        desc = (r.get("description") or "").strip()
        if not desc:
            continue
        filtered.append(r)

    # Sort: First by stargazerCount (descending), then by updated_at (descending)
    filtered.sort(key=lambda x: (x.get("stargazers_count", 0), x.get("updated_at", "")), reverse=True)

    lines = [
        "| Project | Description | Stars |",
        "| :--- | :--- | :---: |",
    ]

    for r in filtered:
        name = r["name"]
        url = r["html_url"]
        desc = r.get("description", "").strip()
        # Clean up whitespace and pipe characters
        desc = re.sub(r"\s+", " ", desc).replace("|", "\\|")
        stars = r.get("stargazers_count", 0)
        emoji = REPO_EMOJIS.get(name, "")
        emoji_str = f" {emoji}" if emoji else ""

        star_str = f"⭐ {stars}" if stars > 0 else "-"

        lines.append(f"| [**{name}**]({url}){emoji_str} | {desc} | {star_str} |")

    return "\n".join(lines)


def update_readme(table_md):
    if not os.path.exists(README_PATH):
        print(f"README.md not found at {README_PATH}", file=sys.stderr)
        sys.exit(1)

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(
        rf"{re.escape(START_TAG)}[\s\S]*?{re.escape(END_TAG)}",
        re.MULTILINE,
    )

    replacement = f"{START_TAG}\n{table_md}\n{END_TAG}"

    if pattern.search(content):
        new_content = pattern.sub(replacement, content)
    else:
        # If tags not found, find '## Selected work' and replace the old table
        old_section_pattern = re.compile(r"## Selected work\s*\n\s*\|[\s\S]*?(?=\n## |\Z)")
        if old_section_pattern.search(content):
            new_content = old_section_pattern.sub(f"## Selected work\n\n{replacement}\n", content)
        elif "## Selected work" in content:
            new_content = content.replace(
                "## Selected work\n",
                f"## Selected work\n\n{replacement}\n",
            )
        else:
            new_content = content + f"\n\n## Selected work\n\n{replacement}\n"

    if new_content != content:
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("README.md updated successfully.")
    else:
        print("README.md is already up to date.")


def main():
    repos = fetch_repos()
    if not repos:
        print("No repository data retrieved.", file=sys.stderr)
        sys.exit(1)

    table_md = generate_markdown_table(repos)
    print("Generated Showcase Table:\n")
    print(table_md)
    print("\nUpdating README.md...")
    update_readme(table_md)


if __name__ == "__main__":
    main()
