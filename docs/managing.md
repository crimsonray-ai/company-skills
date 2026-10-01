# Manage a library

One repository is one library. `company-skills.json` gives it a name, groups skills into collections, and sets the default selection:

```json
{
  "version": 1,
  "name": "Example library",
  "collections": {"example": ["hello-world"]},
  "defaults": ["example"]
}
```

`version` is the manifest format, not a release number. Collections can overlap; they do not restrict access. GitHub access applies to the entire repository. For another library or a different audience, copy this starter into a separate repository and change its name and content. There is no multi-library registry to maintain.

## Local helpers

Run these from a clone with the environment described in the [README](../README.md). They affect that clone only—no network, installed profiles, commits, or GitHub permission changes.

```sh
python3 scripts/manage.py list
python3 scripts/manage.py add-skill summarize-notes --collection example --description "Summarize supplied meeting notes."
python3 scripts/manage.py add-collection writing summarize-notes
```

Edit skill text directly. To change collection membership or defaults, edit `company-skills.json` and validate it. Every skill must remain in at least one collection; defaults must name existing collections. Names use 1–64 lowercase letters, numbers, or hyphens, excluding reserved device names such as `con`.

### Remove something

Review `git status` and `git diff` first. Deletion removes local files, including uncommitted edits inside the selected skill. Commit or separately preserve work you want to keep.

```sh
python3 scripts/manage.py remove-collection writing --yes
python3 scripts/manage.py remove-skill summarize-notes --yes
```

Removing a collection never deletes skill folders. Removing a skill deletes its whole folder and removes it from all collections. Operations that would leave an empty collection, no defaults, no skills, or an unassigned skill are refused **before changing files**. Adjust memberships/defaults first; the helper never silently chooses replacements.

Use one helper/editor at a time. The scripts are local conveniences, not a concurrent transaction service. Manifest writes use atomic replacement, and ordinary write failures roll back skill creation/removal. A killed process or failed recovery can leave a `.removed-skill-*` recovery folder; inspect and restore it before continuing. Do not delete that folder blindly or commit it. Use Git for durable recovery.

## Review and share

1. Create a branch and make the change.
2. Run validation and tests, then inspect the complete diff.
3. Commit and submit a pull request using normal Git/GitHub tools. GitHub controls who can read, write, and merge.
4. After merge, users preview and approve the updated library in Crimson Ray. Existing conversations and installed copies do not update automatically.

A branch follows future commits when users check for updates; a tag or full commit can pin a version. Do not move existing release tags. `library-demo` and `v0.1.0` preserve the older security examples. The default branch is the minimal starter.

## Before making a fork public

Review all branches, tags, commit history, and release attachments—not just the latest files—for secrets, private content, and third-party licensing. The starter is MIT-licensed; keep the license and use only content you have permission to share. Changing visibility is an explicit owner action, not something these scripts do.
