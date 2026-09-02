# Publishing the NE 630 site

The intended public URL is <https://robertsj.github.io/ne630/>. Source remains
on the course-development branch; generated HTML is published from the root of
an orphan `gh-pages` branch, matching the NE 415 arrangement.

The branch was initialized on September 2, 2026. GitHub Pages is serving it at
the URL above. Publishing changes Git history and pushes to GitHub, so it is
deliberately not part of `make check`.

## Before every publication

From the repository root:

```bash
python -m pip install -r site/requirements.txt
make check
git status --short
```

Inspect the site at `_build/html/index.html`, verify the Git diff, and make sure
the intended canonical handout inputs and generated `site/_static/handouts/`
exports are committed on the source branch before publishing.

## First publication procedure (reference)

The initial branch was created in a temporary linked worktree so generated
files never entered the source branch:

```bash
pages_worktree=$(mktemp -d /tmp/ne630-pages.XXXXXX)
rmdir "$pages_worktree"

git worktree add --detach "$pages_worktree" HEAD
git -C "$pages_worktree" switch --orphan gh-pages
rsync -a --delete --exclude='/.git' _build/html/ "$pages_worktree"/

git -C "$pages_worktree" add -A
git -C "$pages_worktree" commit -m "Publish NE 630 course materials"
git -C "$pages_worktree" push -u origin gh-pages

git worktree remove "$pages_worktree"
```

The `--exclude='/.git'` safeguard is essential: a linked worktree stores its
Git metadata in a `.git` file, and `rsync --delete` must not remove it.

Then configure the repository in GitHub under **Settings > Pages**:

- Source: **Deploy from a branch**
- Branch: **gh-pages**
- Folder: **/ (root)**

## Later publications

After `gh-pages` exists locally, use a fresh temporary worktree:

```bash
git fetch origin gh-pages

pages_worktree=$(mktemp -d /tmp/ne630-pages.XXXXXX)
rmdir "$pages_worktree"
git worktree add "$pages_worktree" gh-pages

rsync -a --delete --exclude='/.git' _build/html/ "$pages_worktree"/
git -C "$pages_worktree" add -A
git -C "$pages_worktree" commit -m "Publish updated NE 630 course materials"
git -C "$pages_worktree" push origin gh-pages

git worktree remove "$pages_worktree"
```

In a fresh clone where only `origin/gh-pages` exists, create the local tracking
branch once with `git branch --track gh-pages origin/gh-pages` before adding the
worktree.
