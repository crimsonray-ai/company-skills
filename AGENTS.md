# Working in this repository

These instructions extend your coding agent's existing safety and approval rules.

- Read `README.md` and the relevant guide in `docs/` first.
- Keep this repository a small skill library, not an application or a publishing framework.
- Edit skill instructions directly. Use `scripts/manage.py` for scaffolding, listing, and removal; edit `company-skills.json` for membership or default changes.
- Each skill is self-contained under `skills/<name>/`; only selected skill folders are installed. Root-level docs and helpers are for maintainers.
- Use lowercase letters, numbers, and hyphens for names. Keep the frontmatter name equal to the folder name and descriptions at most 60 characters.
- A scaffold is a draft, not finished instructions. Write a concrete procedure and expected result before publishing. Do not invent successful execution.
- Before deletion, review local changes and get the user's approval. The helper's `--yes` confirms deletion, not permission to discard someone else's work.
- Run `python3 scripts/validate_library.py` and `python3 -m unittest discover -s tests -v`, then inspect `git diff`. Do not add GitHub Actions or generated PDFs.
- Use branches and pull requests for changes. Do not commit, push, merge, change repository visibility, or modify access unless the user asked.
- Never commit credentials, customer material, or machine-specific paths. Keep dependencies and documentation small.
