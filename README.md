# Company Skills

A small starter repository for sharing skills with Crimson Ray. Manage the files with a coding agent or text editor; use GitHub for access and pull requests.

This repository is **one library**, containing an `example` collection and a [`hello-world`](skills/hello-world/SKILL.md) skill. Collections group skills; they are not separate permissions. Use a separate repository when a library needs different access.

## Try it

In Crimson Ray, open **Skills → Company** on a local profile:

1. Enter `https://github.com/crimsonray-ai/company-skills` and leave the ref blank for the default branch.
2. Preview the `example` collection, review the files, and approve installation.
3. Start a new conversation and ask the agent to use `hello-world`.

Or run the example directly from a clone:

```sh
python3 skills/hello-world/scripts/hello.py
```

Output: `Hello, world!` No packages or credentials are needed to run it.

## Maintain it

Use Python 3.10+ for the management helpers. Their only dependency is PyYAML, used to read skill frontmatter correctly.

```sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements-dev.txt
python3 scripts/manage.py list
python3 scripts/validate_library.py
python3 -m unittest discover -s tests -v
```

On Windows, create the environment with `py -3 -m venv .venv`, activate `.venv\Scripts\Activate.ps1`, and use `python` for the remaining commands. The Bash convenience runner, `scripts/run_tests.sh`, runs the same validation and tests.

- [Author a skill](docs/authoring.md)
- [Manage the library and collections](docs/managing.md)
- [Coding-agent instructions](AGENTS.md)

There is no in-app authoring workflow, GitHub automation, or publishing service. Edit, validate, inspect `git diff`, and submit a pull request. Users explicitly review and install updates.

## Layout

```text
company-skills.json       Library name, collections, and default selection
skills/hello-world/      One self-contained example skill
scripts/                Local management and validation helpers
requirements-dev.txt    Maintainer-only YAML dependency
docs/                   Short authoring and management guides
tests/                  Local checks; no GitHub Actions
```

The original security examples are preserved on [`library-demo`](https://github.com/crimsonray-ai/company-skills/tree/library-demo). Older tags and releases also refer to that demo, not this minimal starter.

## License

[MIT](LICENSE). Keep secrets, customer data, and generated reports out of every branch, tag, and release. Making a repository public exposes its retained history too.
