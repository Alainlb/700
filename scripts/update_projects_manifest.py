#!/usr/bin/env python3
"""Auto-generate assets/projects/manifest.json from project folders."""

from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path

VIDEO_EXTENSIONS = {".mp4", ".webm", ".mov", ".m4v"}
POSTER_CANDIDATES = ("poster.jpg", "poster.jpeg", "poster.png", "poster.webp")


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return slug or "project"


def visible(path: Path) -> bool:
    return not any(part.startswith(".") for part in path.parts)


def first_video(project_dir: Path) -> Path | None:
    candidates = [
        p
        for p in project_dir.rglob("*")
        if p.is_file() and p.suffix.lower() in VIDEO_EXTENSIONS and visible(p.relative_to(project_dir))
    ]
    if not candidates:
        return None
    return sorted(candidates, key=lambda p: p.relative_to(project_dir).as_posix().lower())[0]


def poster_path(project_dir: Path) -> Path | None:
    for candidate in POSTER_CANDIDATES:
        p = project_dir / candidate
        if p.is_file():
            return p
    return None


def build_manifest(repo_root: Path, projects_root: Path) -> dict:
    entries = []
    project_dirs = sorted(
        [p for p in projects_root.iterdir() if p.is_dir() and not p.name.startswith(".")],
        key=lambda p: p.name.lower(),
    )

    for project_dir in project_dirs:
        video = first_video(project_dir)
        if not video:
            continue

        folder_rel = project_dir.relative_to(repo_root).as_posix()
        video_rel = video.relative_to(project_dir).as_posix()
        entry = {
            "id": slugify(project_dir.name),
            "folder": folder_rel,
            "file": video_rel,
        }

        poster = poster_path(project_dir)
        if poster:
            entry["poster"] = poster.relative_to(repo_root).as_posix()

        entries.append(entry)

    return {"projects": entries}


def write_manifest(output_path: Path, data: dict) -> bool:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(data, indent=2, ensure_ascii=True) + "\n"
    if output_path.exists() and output_path.read_text(encoding="utf-8") == text:
        return False
    output_path.write_text(text, encoding="utf-8")
    return True


def signature(projects_root: Path, output_path: Path) -> tuple:
    items = []
    output_resolved = output_path.resolve()

    for p in sorted(projects_root.rglob("*"), key=lambda x: x.as_posix().lower()):
        if not visible(p.relative_to(projects_root)):
            continue
        if p.resolve() == output_resolved:
            continue
        stat = p.stat()
        items.append((p.relative_to(projects_root).as_posix(), stat.st_mtime_ns, stat.st_size, p.is_dir()))

    return tuple(items)


def run_once(repo_root: Path, projects_root: Path, output_path: Path) -> bool:
    manifest = build_manifest(repo_root, projects_root)
    changed = write_manifest(output_path, manifest)
    status = "updated" if changed else "no changes"
    print(f"[manifest] {status}: {output_path.relative_to(repo_root).as_posix()} ({len(manifest['projects'])} projects)")
    return changed


def run_watch(repo_root: Path, projects_root: Path, output_path: Path, interval: float) -> None:
    print(f"[manifest] watching: {projects_root.relative_to(repo_root).as_posix()}")
    run_once(repo_root, projects_root, output_path)
    prev = signature(projects_root, output_path)

    while True:
        time.sleep(interval)
        current = signature(projects_root, output_path)
        if current == prev:
            continue
        run_once(repo_root, projects_root, output_path)
        prev = current


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate manifest.json from project folders.")
    parser.add_argument("--root", default="assets/projects", help="Projects root folder.")
    parser.add_argument("--output", default="assets/projects/manifest.json", help="Manifest output file.")
    parser.add_argument("--watch", action="store_true", help="Watch folders and regenerate on change.")
    parser.add_argument("--interval", type=float, default=1.0, help="Watch polling interval in seconds.")
    args = parser.parse_args()

    repo_root = Path.cwd()
    projects_root = (repo_root / args.root).resolve()
    output_path = (repo_root / args.output).resolve()

    if not projects_root.exists():
        raise SystemExit(f"Projects root does not exist: {projects_root}")

    if args.watch:
        run_watch(repo_root, projects_root, output_path, args.interval)
    else:
        run_once(repo_root, projects_root, output_path)


if __name__ == "__main__":
    main()
