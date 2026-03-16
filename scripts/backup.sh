#!/usr/bin/env bash
# Local backup of WEB_700 project (excludes .git, _backups, node_modules, .DS_Store)

set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
BACKUPS_DIR="$PROJECT_DIR/_backups"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
BACKUP_NAME="WEB_700_$TIMESTAMP"
BACKUP_PATH="$BACKUPS_DIR/$BACKUP_NAME"

mkdir -p "$BACKUPS_DIR"

rsync -a \
  --exclude='.git' \
  --exclude='_backups' \
  --exclude='.DS_Store' \
  --exclude='node_modules' \
  "$PROJECT_DIR/" "$BACKUP_PATH/"

# Count backups and remove oldest if more than 10
BACKUP_COUNT=$(ls -1d "$BACKUPS_DIR"/WEB_700_* 2>/dev/null | wc -l | tr -d ' ')
MAX_BACKUPS=10

if [ "$BACKUP_COUNT" -gt "$MAX_BACKUPS" ]; then
  REMOVE_COUNT=$((BACKUP_COUNT - MAX_BACKUPS))
  ls -1d "$BACKUPS_DIR"/WEB_700_* | head -n "$REMOVE_COUNT" | while read -r old; do
    rm -rf "$old"
    echo "[backup] removed old: $(basename "$old")"
  done
fi

echo "[backup] created: $BACKUP_NAME ($BACKUP_COUNT total)"
