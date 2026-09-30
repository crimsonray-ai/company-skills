# Company Skills Handbook

## Crimson Ray Security Playbooks

**Company setup, skill publishing, authoring, and employee onboarding**

**Library edition:** v0.1.0<br>
**Prepared:** 30 September 2026<br>
**Repository:** https://github.com/crimsonray-ai/company-skills

This handbook explains how a company can maintain one reviewed security-skill library and help employees use the right workflows without copying files manually. It covers the supplied starter skills, company responsibilities, publishing and updating content, creating new skills, employee installation, and individual skill enablement.

The starter library contains **16 skills, 8 collections, and 48 installable Markdown files**. It is an analysis and planning library: it does not configure integrations, grant access to business systems, supply credentials, or automatically execute changes.

> **Application prerequisite:** Company Skills support is introduced by [Crimson Ray PR #794](https://github.com/crimsonray-ai/crimsonray/pull/794). Use an approved application build containing that feature and confirm that **Skills → Company Skills** is present. A library tag such as `v0.1.0` does not mean that a Desktop version containing the feature has been published. Check the application release separately; an open PR or unsigned test artifact is not a customer release.

## Contents

1. [The feature and its boundaries](#1-the-feature-and-its-boundaries)
2. [Roles, access, and versioning](#2-roles-access-and-versioning)
3. [Company setup from the beginning](#3-company-setup-from-the-beginning)
4. [Choose the right collections](#4-choose-the-right-collections)
5. [New-user onboarding](#5-new-user-onboarding)
6. [Enable, disable, and use individual skills](#6-enable-disable-and-use-individual-skills)
7. [Add an existing skill to the company library](#7-add-an-existing-skill-to-the-company-library)
8. [Create a new skill](#8-create-a-new-skill)
9. [Review, validate, and publish a release](#9-review-validate-and-publish-a-release)
10. [Manage updates, conflicts, retirement, and rollback](#10-manage-updates-conflicts-retirement-and-rollback)
11. [Security and data-handling expectations](#11-security-and-data-handling-expectations)
12. [Troubleshooting and support](#12-troubleshooting-and-support)
13. [The starter skill catalog](#13-the-starter-skill-catalog)
14. [Command-line reference](#14-command-line-reference)
15. [Rollout checklists and ongoing ownership](#15-rollout-checklists-and-ongoing-ownership)

## 1. The feature and its boundaries

### The simple model

A company writes and reviews skills in GitHub. Employees select a library and collection in Crimson Ray, preview the proposed installation, and explicitly approve it. The installed skills then become available in the selected profile.

```text
Company authors and reviewers
             ↓
Reviewed GitHub skill library
             ↓
Employee selects collections and reviews a pinned preview
             ↓
Skills installed into the selected local profile
             ↓
Employee chooses which skills are enabled
             ↓
New conversations use those skills with supplied evidence
```

A **skill** is a reusable workflow: instructions, evidence requirements, a procedure, and supporting files. For example, the incident-triage skill helps an analyst distinguish confirmed observations from hypotheses and prepare a response handoff.

A skill is **not** an integration or a source of truth. It cannot make a missing connector appear, grant GitHub or cloud access, turn an alert into proof, or certify a control. It still needs evidence and the capabilities already available to the user.

### What this first version supports

- Libraries hosted on **github.com**.
- Installation into **local Crimson Ray profiles** through a local gateway.
- Shared and team-oriented collections, including overlapping membership.
- Complete skill folders, including templates and reference documents.
- Commit-pinned previews, explicit approval, recorded source/version information, updates, and removal.
- Protection against silently overwriting locally changed files or existing skills with conflicting names.

It does not provide a new GitHub sign-in wizard, GitHub Enterprise Server support, automatic push of local edits, silent background rollout, mandatory policy enforcement, connector setup, or whole-profile synchronization.

### Why there is no gateway setup chapter here

This library does not require a **shared company gateway**. Crimson Ray still uses its normal local backend, but skill distribution is independent of shared business-system connectivity. The current Company Skills management surface is unavailable on shared hosted gateways.

If a skill needs evidence from a connected system, that system must already be configured and authorized through a separate process. Every starter workflow also accepts supplied records or exports; it does not assume that a particular vendor integration is present.

## 2. Roles, access, and versioning

### Who owns what?

| Role | Responsibility |
| --- | --- |
| Company owner | Decides the baseline library, approved use, rollout policy, and accountable maintainers. |
| Skill maintainer | Authors content, keeps collection membership correct, runs checks, and prepares releases. |
| Domain reviewer | Checks whether the workflow is useful, accurate, bounded, and appropriate for its intended users. |
| IT or GitHub administrator | Grants repository access, supports authentication, and distributes an approved Crimson Ray application. |
| Employee | Chooses a profile and collection, reviews installation, sets enabled skills, and supplies authorized evidence. |

A small company can assign several responsibilities to one person. The responsibilities should still be explicit: an application administrator is not automatically the domain reviewer for every security procedure.

### Three controls that are easy to confuse

| Control | What it changes | What it does not change |
| --- | --- | --- |
| Repository access | Whether an identity can read or publish the GitHub source | Business-system permissions or whether a downloaded skill remains on a device |
| Collection selection | Which skill files are installed from the library | Who is authorized to see other content in the same repository |
| Per-skill enabled switch | Whether an installed skill is available in the selected profile's skill experience | File ownership, GitHub membership, or connector permissions |

**Collections are not an access-control boundary.** A user with read access to this repository can read its contents, including collections they did not install. If some procedures must be restricted to a smaller audience, use a separately permissioned repository rather than relying on collection checkboxes.

Profiles keep configuration and user state organized. They are not a substitute for operating-system security or the tenant/access controls of business systems.

### Four different version identifiers

| Identifier | Example | Meaning |
| --- | --- | --- |
| Manifest format version | `"version": 1` in `company-skills.json` | The collection file's schema version—not a release number |
| Individual skill version | `version: 0.1.0` in frontmatter | The maintainer's content version for that skill |
| Library release/ref | `v0.1.0`, `main`, or a full commit SHA | The source employees request when previewing the library |
| Crimson Ray application version | The company's approved Desktop build | The software that provides the Company Skills feature |

GitHub tags can technically be moved. The company should adopt an immutable-release policy and protect release tags. Use a full commit SHA for a strict source pin. Regardless of the requested ref, a preview records a resolved commit and apply uses the exact staged bytes reviewed in that preview.

## 3. Company setup from the beginning

### Step 1 — Confirm the application prerequisite

Choose the approved Crimson Ray build for the rollout. Verify that it contains Company Skills and that a local user can open **Skills → Company Skills**. Normal model/provider setup must already work; installing a library does not configure model access or billing.

Check the application release that contains the feature, not just the library release. If the feature is still in a development PR, keep testing in a controlled development environment rather than telling employees it is already available in the normal release.

### Step 2 — Choose the library and maintainers

This starter repository is:

```text
https://github.com/crimsonray-ai/company-skills
```

The company can use it directly if it has access, or maintain a company-controlled copy. Assign at least one content owner and a review path for changes. Keep routine employee access read-only; publishing access belongs to maintainers.

Choose the recommended initial collection. `essentials` is the default and installs four workflows. Add role collections only where the employees need them.

### Step 3 — Configure GitHub access

Invite the intended users or GitHub teams to the private repository. Confirm that an employee—not just an administrator—can open it while signed in with the intended work account.

Company Skills reuses existing GitHub authentication on the machine running the local gateway. The supported existing mechanisms include GitHub CLI login and configured GitHub token credentials. For most employees, IT-assisted GitHub CLI sign-in avoids handling a token manually:

```bash
gh auth login --hostname github.com
gh auth status --hostname github.com
```

Use the organization's approved authentication method and complete any required SSO authorization. Authentication status alone does not prove access to this repository; the library preview exercises the actual read path.

For a fine-grained token, restrict it to the intended repository and read-only Contents access. Follow company credential policy. Never place a token in a repository URL, chat message, skill file, screenshot, or handbook. The feature does not add a new token store or distribute shared credentials.

**Important:** GitHub CLI identity is associated with the machine/user account. Selecting a different Crimson Ray profile does not automatically switch that GitHub identity. Profile-specific installation and external GitHub authentication are separate concepts.

### Step 4 — Review the starter content

Before an organization-wide rollout, a domain owner should review the procedures, evidence requirements, and report templates. The library's automated validation and security scanner are useful checks, not proof that every analytical conclusion will be correct.

Confirm which workflows fit company policy, which require additional context, and which should remain disabled for a particular role. Do not insert real customer records into the skill library to make examples realistic; use clearly labelled synthetic examples.

### Step 5 — Pilot with a non-administrator

Use a clean local profile and a normal employee account. Test:

1. Opening the private repository and previewing the library.
2. Selecting the recommended collections and approving installation.
3. Finding the installed skills and changing an individual enabled switch.
4. Starting a new conversation and invoking a skill with sanitized evidence.
5. Receiving a useful report with references, uncertainty, and no invented completed actions.
6. Previewing an update and confirming that local modifications block replacement.

### Step 6 — Put publishing controls in place

Recommended controls include pull-request review, the **Library contract and tests** GitHub check, restricted write access, and protected release tags. Configure those controls through the company's normal GitHub administration process; this starter repository does not silently change organization policy.

### Step 7 — Send employees an onboarding packet

Include the repository URL, the approved library ref, their recommended collections, the approved Crimson Ray build, authentication instructions, and a support contact. A complete example is:

```text
Library: https://github.com/crimsonray-ai/company-skills
Ref: v0.1.0
Collections: essentials + soc
Application: use the company-approved build containing Company Skills
Support: your company's named IT/security support channel
```

The ref `v0.1.0` identifies this starter library release. It does not select an application version.

## 4. Choose the right collections

The library provides eight collections. Membership can overlap; a skill selected by two collections is installed only once.

| Collection | Recommended audience | Included workflows |
| --- | --- | --- |
| `essentials` | New users and cross-functional teams | Evidence brief; incident triage; remediation plan; executive brief |
| `soc` | SOC and incident response | Evidence brief; triage; timeline; detection gaps; hunt planning |
| `exposure-management` | Vulnerability and exposure teams | Vulnerability prioritization; asset coverage; cloud posture; remediation |
| `cloud-identity` | Cloud, IAM, and IT security | Cloud posture; identity access; SaaS exposure; asset coverage |
| `application-security` | AppSec and platform reviewers | Secure change review; software supply chain; vulnerability prioritization; remediation |
| `assurance` | GRC and third-party-risk teams | Supplier review; compliance evidence map; evidence brief |
| `leadership` | Security leaders and decision owners | Executive brief; evidence brief; remediation plan |
| `all` | Maintainers and deliberate full-library users | All 16 skills; not selected by default |

### Suggested starting combinations

- **New SOC analyst:** `essentials` plus `soc`.
- **Cloud security engineer:** `essentials` plus `cloud-identity`.
- **Vulnerability program owner:** `essentials` plus `exposure-management`.
- **Application security reviewer:** `essentials` plus `application-security`.
- **GRC analyst:** `assurance`; add `leadership` if preparing executive updates.
- **Security leader:** `leadership`, with other skills enabled only where useful.

Do not install `all` just to avoid making a choice. The skill index is part of the agent's working context, and a smaller relevant set makes it easier to choose the intended workflow.

### Example: overlapping collections

Both `essentials` and `soc` include `cr-incident-triage`. Selecting both creates one installed copy. Later removing `soc` does not remove triage while `essentials` remains selected. The update preview shows which files would actually be removed.

Collection selection applies to a library in a particular profile. It is not an organization-wide assignment system, a permission grant, or automatic enrollment for every employee.

## 5. New-user onboarding

### Before the employee starts

The employee needs an approved Crimson Ray installation with normal model access, a local profile, the company-provided repository URL/ref, and GitHub read access if the repository is private. There is no new Desktop GitHub sign-in wizard in this first version; authentication may require a one-time IT-assisted setup.

### Step 1 — Choose the intended profile

Open the profile where company skills should be installed. An existing work profile is sufficient; Company Skills does not require creating another profile or replacing personal settings.

If a separate work profile is desirable, create it through the normal profile workflow before installation. For service providers working with multiple customers, keep customer evidence and access boundaries separate; a shared skill repository must not become a storage location for customer investigations.

### Step 2 — Open Company Skills

Open **Skills → Company Skills**. If the app is connected to a shared hosted gateway, switch to a local gateway before managing this library. If the tab is missing, verify the application prerequisite with IT rather than editing configuration files to force it on.

### Step 3 — Enter the source

Paste:

```text
https://github.com/crimsonray-ai/company-skills
```

Use the repository root URL—not a `/tree/…` or `/blob/…` page. Enter the company-approved branch, tag, or commit in the separate ref field. For the starter release, use `v0.1.0`; blank means the repository's default branch.

### Step 4 — Preview and select collections

Select **Preview library**. The initial preview selects the repository's recommended collection, `essentials`.

Select any additional role collection, then preview again. Changing the collection selection invalidates approval of the earlier preview. The preview is not an installation and does not execute scripts.

### Step 5 — Review the proposed content

Check:

- The repository and resolved commit are the ones you expect.
- The selected collections are correct.
- Added, changed, and removed files make sense.
- The skill instructions and scanner results are acceptable.
- Supporting scripts and files, if present in a future library version, have been reviewed too.

A clean scan is not a guarantee of safety. Only install a source you trust. A blocked skill cannot be approved around through a force-overwrite option.

### Step 6 — Approve installation

Check the explicit approval box, then choose **Apply reviewed changes**. Crimson Ray applies the staged files from that preview, not a fresh download of a moving branch. A preview expires after 30 minutes; if it expires, create and review a new one.

### Step 7 — Confirm the installed record

The installed-library card shows its source, commit, and collections. Keep that information when reporting a problem. The installation is scoped to the chosen profile; other profiles are not automatically updated.

### Step 8 — Set individual enabled skills

Open the **Skills** tab and review the installed `cr-…` skills. Choose which should be enabled for this profile using the normal per-skill switch. The next chapter explains the difference between disabling a skill and uninstalling it.

### Step 9 — Start a new conversation

Use the app's normal new-conversation action. The workflow preserves existing conversation prefixes rather than rebuilding a conversation that is already in progress. Start a new conversation after installation, updates, or enablement changes to use the intended skill inventory reliably.

## 6. Enable, disable, and use individual skills

### Find the installed skill

In **Skills → Skills**, search for an exact name such as `cr-incident-triage` or use `cr-` to find the starter workflows. Search for the skill name, not the collection name: `soc` is a collection and is not itself a skill.

Use the **All** filter if a skill is not visible under another source filter. Company-managed skills reuse the external-install provenance protections and may appear with a **hub** badge in the installed list. The **Company Skills** tab remains the place to manage the library and its collections.

### Enable or disable

Use the switch on the skill's row to enable or disable it in the selected profile. New skills are normally available after installation unless profile policy, platform filtering, or an existing disabled preference says otherwise. Review the installed list rather than assuming that every new skill has the state you want.

Disabling a skill:

- Does not delete its files.
- Does not remove the library's recorded ownership or version.
- Does not revoke GitHub access or connector permissions.
- Does not turn a collection into an access-control boundary.

Library updates do not rewrite unrelated profile settings. A skill with a stable name retains the profile's existing disabled preference. A renamed skill is a new identity, so review its enabled state after a migration.

If you want only some skills from a collection, disabling the unwanted skills is preferable to manually deleting files inside the managed library. Manual deletion is detected as a local modification and blocks future replacement/removal until resolved.

### Invoke the workflow

Start a new conversation and use a slash command, for example:

```text
/cr-incident-triage
```

Then provide the evidence and decision context requested in its prerequisites. You can also ask Crimson Ray to use the skill by its exact name. Skill suggestions depend on the current profile and enabled inventory; if a command is missing, check those before assuming installation failed.

### A safe first exercise

Use synthetic data, not a live incident, for the first test:

```text
Use cr-incident-triage for this synthetic training example.

Scope: example tenant T-TRAINING; 09:00–10:00 UTC.
E1: Alert A-TRAINING reports a successful sign-in from a new location
    for identity U-TRAINING at 09:15 UTC, associated with device D-TRAINING.
E2: An inventory record says D-TRAINING is managed and was seen at 09:10 UTC.
Missing: travel/change confirmation, authentication details, and business criticality.

Prepare a triage disposition, explain uncertainty, and propose the next
bounded evidence request. Do not treat this as a confirmed compromise.
```

A useful response distinguishes observations from the detector's hypothesis, acknowledges the missing inputs, and proposes a discriminating next read. It should not invent a source IP, claim a breach, disable the account, or say containment occurred.

### Save reports outside the library

The skill's `templates/report.md` is a reusable blank template. Completed reports and working evidence belong in an approved work location, not in the installed skill folder or this repository. The skill can use an available file-writing capability when the user requests a saved artifact; otherwise it returns the report in the conversation.

## 7. Add an existing skill to the company library

### Step 1 — Review its origin and rights

Confirm that the company is allowed to use and redistribute the candidate content to the intended audience. Review the complete folder, not just `SKILL.md`. Check for scripts, hidden files, credentials, customer data, unexpected network calls, and references to files outside the skill.

A skill from another agent product may need adaptation. Tool names, assumptions about permissions, required software, and output expectations must match Crimson Ray. Do not simply rename another product's folder and assume it is compatible.

### Step 2 — Give it a stable, distinct identity

Choose a name such as `cr-your-workflow`. The folder and frontmatter `name` must match. Avoid collisions with bundled skills, personal variants, and other libraries.

Names should remain stable once employees install them. Changing a name creates a new skill identity and can affect slash commands and per-skill preferences.

### Step 3 — Make the folder self-contained

Use this layout:

```text
skills/cr-your-workflow/
├── SKILL.md
├── templates/report.md
└── references/checklist.md
```

Include all required supporting files inside the skill folder. Root-level README files, `docs/`, and maintainer scripts are not installed as part of a selected skill. Do not use symlinks or a shared parent-folder reference to supply missing content.

### Step 4 — Adapt the procedure and prerequisites

State the evidence the workflow needs, what it produces, and what it does not do. Gate named tools on their availability. If a connector or platform-specific helper is required, make the dependency explicit and test that path separately; installation itself does not configure it.

### Step 5 — Add collection membership

Add the exact skill name to the relevant collection(s) in `company-skills.json`, and keep `all` complete. Add the skill to the README catalog. Update this handbook when the new workflow changes company or employee procedures.

### Step 6 — Validate and pilot

Run the repository checks, preview the candidate GitHub ref in Crimson Ray, review the scanner result, and pilot with sanitized evidence. Ask the relevant domain owner to review the actual output before publishing a company recommendation.

## 8. Create a new skill

### Start with a concrete contract

Before writing instructions, answer five questions:

1. Who is the user?
2. What evidence must they supply?
3. What decision or artifact should result?
4. What actions are outside the skill's scope?
5. What observable check shows the result is useful and accurate?

For example, “improve security” is too vague. “Compare a supplied SaaS sharing export against the company's sharing policy and produce a source-linked review register” has an input, a decision criterion, and an output.

Check the existing catalog before creating a new skill. Extend an existing workflow when its evidence and deliverable are substantially the same. Do not create an index skill whose only purpose is to send the model to other skills.

### Create the files

Copy the authoring aid at `docs/new-skill-template.md` into a new folder under `skills/`. Replace every `REPLACE_ME` value and add the supporting template and checklist. You can do this through GitHub's web editor or your normal branch-based development workflow.

Use a working branch and a pull request. Do not edit installed copies as the publishing workflow.

### Write frontmatter

```yaml
---
name: cr-your-workflow
description: "Explain the capability in one short sentence."
version: 0.1.0
author: Hermes
metadata:
  hermes:
    category: security
    tags: [Security, Evidence]
---
```

The description is a routing hint. Keep it to one sentence, at most 60 characters, ending in a period. Do not repeat the skill name or add marketing adjectives. Put the detail in the body.

The generated starters use the literal author `Hermes`, following the harness convention. Do not derive an author from a login name or credential. Record explicitly approved human authorship and reviewer credit through the company's normal contribution process.

Portable Markdown workflows omit `platforms`. A future skill using OS-specific scripts must declare and test its supported platforms. Do not claim portability while relying on a platform-only command.

### Use the standard body structure

| Section | What belongs there |
| --- | --- |
| Title and introduction | Capability, limits, and dependency stance |
| When to Use | Concrete user requests that should trigger the skill |
| Prerequisites | Required evidence, scope, policy, and configured capabilities |
| How to Run | The invocation and available-tool path |
| Quick Reference | Supporting files and key terms |
| Procedure | The actual ordered analysis or planning steps |
| Pitfalls | Domain-specific interpretation traps and failure cases |
| Verification | Observable checks on the completed result |

Declare **Policy: extend**. The skill adds a workflow; it inherits the active harness's approval, data-access, and rendering rules rather than cancelling them.

### Make instructions precise

Prefer “record the source identifier and observation time for each conclusion” over “be thorough.” Distinguish a confirmed observation, an inference, a supplier assertion, and an unknown. Do not instruct the model to fabricate missing evidence or silently broaden the target scope.

Name native tools only when their availability is part of the instruction. The starters use conditional paths for `skill_view`, `read_file`, and `write_file`, with a supplied-text fallback. Do not invent connector tool names, vendor endpoints, query fields, or flags.

### Design the supporting template

A template should specify the information the user needs to review: scope, evidence references, conclusions, uncertainties, owners, and the next decision. It should contain blank fields or clearly labelled prompts, not pre-filled real findings.

A reference checklist should contribute domain definitions, interpretation criteria, or a labelled synthetic example. It should not merely duplicate the Procedure.

### Add code only for a real need

These starters contain no executable skill scripts. If a future workflow genuinely needs parsing or computation that is unreliable to recreate conversationally, add a small tested helper inside that skill's `scripts/` folder. Document its inputs, outputs, limits, dependencies, and supported platforms.

Frame execution through the existing authorized tool path. Do not add an installation hook, automatic network send, background job, or permission bypass. Never require the agent to write a large parser from scratch every time the skill runs.

### Complete authoring

Add collection membership, update documentation, run validation, and submit a pull request with sanitized examples and expected results. A domain reviewer should be able to explain why the workflow is distinct and how its verification criteria detect a bad answer.

## 9. Review, validate, and publish a release

### Layer 1 — Repository contract checks

Maintainers need Python and the pinned YAML parser listed in `requirements-dev.txt`. Employees do not need these packages to use the skills.

On macOS or Linux, an isolated validation environment can be created without changing system packages:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
PYTHON=.venv/bin/python bash scripts/run_tests.sh
```

On Windows PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe scripts/validate_library.py
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

The checks verify metadata, names, section order, support files, collection references, defaults, portability constraints, and size limits. The tests include representative invalid inputs. The GitHub workflow runs the same contract checks and tests.

### Layer 2 — Actual importer and security scan

Preview the candidate repository branch or commit through Crimson Ray Company Skills in a clean local profile. Verify that the source resolves, complete skill folders are staged, and the existing scanner accepts the content. Inspect every warning or block.

Fix the reason for a blocked skill. Do not weaken the scanner, hide dangerous behavior in a supporting file, or describe a blocked preview as a successful installation.

### Layer 3 — Behavioral pilot

Use sanitized examples that include:

- A straightforward case with sufficient evidence.
- Missing mandatory inputs.
- Conflicting records or timestamps.
- An irrelevant or misleading source assertion.
- A request that exceeds the skill's intended scope.

Review the actual result. Check source linkage, uncertainty, decision usefulness, and whether proposed actions remain separate from completed actions. Static validation and a clean scan do not prove analytical correctness.

### Layer 4 — Human approval and release

After domain review and green repository checks:

1. Merge the approved content.
2. Create a new release tag for that exact commit.
3. Write release notes listing added, changed, renamed, and removed skills, collection changes, and user migration steps.
4. Generate the handbook PDF from this source when needed and attach it to the release. Keep generated PDFs out of the source history.
5. Announce the approved ref and recommended collections.

Use a prerelease designation during a controlled pilot if that fits company policy. Do not silently move an existing tag. For strictly repeatable rollout, distribute a full commit SHA alongside the human-readable release name.

## 10. Manage updates, conflicts, retirement, and rollback

### Update a library as a user

In **Company Skills**, select **Check updates / collections** on the installed-library card. Review the source commit and file changes, then approve the new preview separately.

If the library was installed from a branch or default-branch ref, the preview can see new commits. If it was pinned to `v0.1.0`, checking updates still requests `v0.1.0`; it does not automatically switch to a later tag.

To adopt a new release, enter the new ref in the form and preview it. Confirm the collection selection again: a newly entered source/ref starts from the repository's recommended defaults until you select otherwise. Review removed files as carefully as added ones.

### Local modifications

Company Skills records a baseline for the files it manages. Editing, adding, or deleting files inside that managed library can block replacement or removal. The tool also rechecks the tree during apply to avoid silently replacing an edit made after preview.

Do not solve a conflict by deleting internal ownership records. Instead:

1. Identify whether the local change should become an upstream contribution or a personal variant.
2. Preserve a personal variant under a different skill identity through the normal authoring process, or submit the change to the repository.
3. Restore the managed copy to its installed state once the desired changes are safely preserved.
4. Create a new preview and review it again.

If the user does not know how to preserve or restore the copy, involve a maintainer. There is no force-overwrite option intended to bypass this protection.

### Change collections

Uncheck an unwanted collection, select any replacement, and preview again. A skill still required by another selected collection remains installed. If the objective is merely to stop offering one installed skill, use its enabled switch rather than deleting its files.

Maintain stable collection IDs. If a maintainer removes or renames an ID that an installed profile remembers, the old selection may no longer be valid. Enter the repository again to preview its current defaults, then deliberately choose the replacement collection.

### Retire or rename skills

A maintainer retires a skill by updating its collection memberships and, when appropriate, removing its folder in a reviewed change. A subsequent update preview shows the removal. Modified local copies still block replacement/removal.

Renaming changes the skill identity. Announce the new name and ask users to review its enabled state and slash command. Old per-skill preferences are not an automatic migration to the new identity.

### Roll back deliberately

A rollback is another reviewed installation from an earlier tag or commit. Enter the earlier ref, choose the intended collections, and inspect the resulting added/changed/removed files. Conflict checks still apply; an older version is not permission to discard personal work.

Repository tags, local installation records, and application releases are separate. Rolling back a skill library does not roll back the Crimson Ray application or any business-system changes.

### Remove the library

Choose **Preview removal**, inspect the managed files, and approve **Remove library**. Removal uses local ownership records and can work without GitHub access. It does not delete unrelated personal skills, configuration, conversations, or memories.

## 11. Security and data-handling expectations

### Skills influence an agent

Treat instructions and supporting scripts as influential content. Review the source before installation. A security scan helps identify known risky patterns, but it cannot guarantee that a workflow is correct or harmless.

The starter skills produce assessments, plans, and reports. They do not provide execution authority. Operational actions still belong to the existing authorization and approval process.

### Keep working evidence out of the library

Do not commit credentials, personal conversations, customer exports, incident evidence, completed reports, or private keys. Templates are reusable blanks. Examples must be clearly synthetic and must not masquerade as findings about a real environment.

Use approved work locations and retention policies for actual evidence. When an AI provider processes supplied material, the company's provider and data-handling policy still applies; skill installation does not change that policy.

### Repository privacy has limits

A private repository restricts source access on GitHub. It does not make installed copies remotely revocable. Removing an employee's GitHub access stops future authorized downloads, but it does not erase files already installed on their device.

Offboarding may therefore require the company's normal endpoint-management and data-retention procedures. Collections and local profiles are not substitutes for access controls or a remote-erasure mechanism.

### Library integrity and boundaries

The installer validates source and paths, rejects unsupported files and collisions, stages a commit-pinned preview, and checks local ownership before replacement. Preview tokens are profile-local approvals for staged content, not credentials to share with other users.

Do not copy generated installation state between users or profiles. Install from the reviewed repository instead, so each profile gets its own correct ownership and preview state.

### Current content limits

The first implementation allows at most 64 skills per library, 32 collections, 512 selected skill files, and 20 MiB of downloaded content per preview. Individual files are limited to 2 MiB, and each `SKILL.md` to 64 KiB. Symlinks, submodules, hidden files, nested skills, and non-portable or case/Unicode-equivalent paths are rejected.

This starter is comfortably below those limits: 16 skills and 48 Markdown files. It has no executable skill scripts and no additional end-user software dependencies.

## 12. Troubleshooting and support

| Symptom | What to check | Safe next step |
| --- | --- | --- |
| Company Skills tab is missing | Application build and local/hosted mode | Confirm a build containing PR #794; do not assume the library tag upgraded the app |
| Panel says local profiles only | Current gateway connection | Switch to a local gateway; shared hosted management is outside this version |
| GitHub access denied or repository not found | Work account, repository read access, SSO, URL, and ref | Verify the canonical repository URL and company-approved authentication; ask IT if needed |
| Rate-limit message | Anonymous access or exhausted GitHub allowance | Use the approved authenticated account and retry after the limit resets |
| Invalid source URL | A copied `/tree/…`, `/blob/…`, query string, or token-bearing URL | Enter the repository root URL; use the separate ref field |
| Collection is no longer available | Maintainer renamed/removed a collection ID | Preview the repository's current defaults and select the replacement deliberately |
| Existing skill-name conflict | Another library or personal/bundled skill uses the same name | Ask a maintainer for a distinct name or resolve the existing installation; do not overwrite blindly |
| Local changes block update/removal | Managed skill files were edited, added, or deleted | Preserve the intended changes, restore the managed copy, and create a fresh preview |
| Preview expired | More than 30 minutes elapsed | Preview and review again; do not reuse the old token |
| Scanner blocks a skill | Instructions, file structure, or supporting content triggered a policy | Maintainer reviews and fixes the cause; do not bypass the scanner |
| Skill or slash command is missing | Wrong profile, disabled skill, filter, platform requirements, or old conversation | Check the installed Skills list with All filter and start a new conversation |
| The skill asks for evidence | Required records or scope are missing | Supply authorized artifacts or clarify the scope; a skill is not a connector |
| File-operation/recovery error | Permissions, filesystem state, or an interrupted operation | Retry a Company Skills operation to recover; preserve recovery data and contact support if it persists |

### What to include in a support request

Provide the application version, repository URL, requested ref, recorded commit, selected profile/collections, skill name, error text, and a sanitized reproduction. Explain expected versus observed behavior.

Do not include tokens, credential files, preview approval tokens, customer records, or entire conversation transcripts by default. Use the company's approved support channel for any sensitive evidence that is genuinely necessary.

## 13. The starter skill catalog

### cr-evidence-brief

**Audience:** security analysts, solution engineers, and service leads.<br>
**Input:** a question, a bounded source set, and audience/scope context.<br>
**Output:** evidence-backed claims, contradictions, missing information, and a decision handoff.<br>
**Boundary:** source assertions and inferences do not become verified facts by being summarized.

### cr-incident-triage

**Audience:** SOC analysts and incident responders.<br>
**Input:** the original alert, underlying events, affected entity IDs, and investigation context.<br>
**Output:** disposition, provisional or policy-based severity, next bounded reads, and proposed response options.<br>
**Boundary:** no containment, account changes, or breach declaration from an alert title alone.

### cr-incident-timeline

**Audience:** incident responders and forensic analysts.<br>
**Input:** event records, original timestamps, timezone/clock information, and scope.<br>
**Output:** a source-linked chronology with uncertain ordering and causal hypotheses kept separate.<br>
**Boundary:** no guessed timezone or invented events to fill telemetry gaps.

### cr-vulnerability-prioritization

**Audience:** vulnerability and exposure-management teams.<br>
**Input:** findings, assets/components, exposure, criticality, controls, and policy.<br>
**Output:** an explainable queue, owners, remediation readiness, and facts that could change priority.<br>
**Boundary:** vendor severity remains distinct from environment-specific priority; exploit availability is not local exploitation.

### cr-cloud-posture-review

**Audience:** cloud-security and platform teams.<br>
**Input:** explicit cloud boundaries, inventory/configuration exports, capture times, and control criteria.<br>
**Output:** an evidence-backed risk register with effective-state questions and coverage limits.<br>
**Boundary:** a single permissive rule is not a proven end-to-end exposure path.

### cr-identity-access-review

**Audience:** IAM and access-review owners.<br>
**Input:** identities, entitlements, activity windows, ownership, and review criteria.<br>
**Output:** retain/investigate/propose-change items with stable identity references and dependencies.<br>
**Boundary:** human and workload identities are assessed differently; the skill does not revoke access.

### cr-saas-exposure-review

**Audience:** SaaS-security, IT, and collaboration-platform owners.<br>
**Input:** workspace scope, sharing/access/grant exports, data policy, and edition limits.<br>
**Output:** a sharing and application-grant review register with owner decisions and verification needs.<br>
**Boundary:** organization-wide sharing is not automatically anonymous internet exposure.

### cr-detection-gap-analysis

**Audience:** detection engineers and SOC content owners.<br>
**Input:** a threat scenario, telemetry schemas, detection logic, and validation evidence.<br>
**Output:** a behavior-to-telemetry coverage matrix and safe validation backlog.<br>
**Boundary:** a rule's name, tag, or enabled state is not proof of end-to-end detection.

### cr-threat-hunting-plan

**Audience:** threat hunters and senior SOC analysts.<br>
**Input:** a testable hypothesis, available telemetry, scope, and query/privacy/cost limits.<br>
**Output:** bounded read-only query plans, baselines, stop conditions, and escalation criteria.<br>
**Boundary:** it plans the hunt; it does not launch scans or execute queries automatically.

### cr-third-party-risk-review

**Audience:** third-party-risk, procurement, and assurance teams.<br>
**Input:** purchased-service scope, data/access context, supplier evidence, and acceptance criteria.<br>
**Output:** evidence classifications, focused follow-up questions, residual risks, and decision options.<br>
**Boundary:** a supplier assertion or an out-of-scope report is not independent proof of the purchased service's controls.

### cr-compliance-evidence-map

**Audience:** GRC and audit-readiness teams.<br>
**Input:** an exact framework/control set and version, scope, period, and artifacts.<br>
**Output:** control/evidence mappings, applicability questions, and missing-proof requests.<br>
**Boundary:** no invented control identifiers, certification, legal opinion, or final audit conclusion.

### cr-secure-change-review

**Audience:** AppSec and platform change reviewers.<br>
**Input:** the proposed diff, intent, trust boundaries, surrounding code/configuration, and validation results.<br>
**Output:** concrete findings, context questions, and required tests with evidence and locations.<br>
**Boundary:** no repository changes or claims that tests executed without supplied results.

### cr-remediation-plan

**Audience:** security engineers, incident owners, and change approvers.<br>
**Input:** a supported finding, exact targets, outcome, constraints, owners, and recovery information.<br>
**Output:** approval-ready steps, dependencies, impact, verification, and rollback questions.<br>
**Boundary:** plan content is not an execution grant and does not prove a change was completed.

### cr-executive-security-brief

**Audience:** CISOs and decision-makers.<br>
**Input:** an assessment, reporting period, audience, and comparable metrics where available.<br>
**Output:** a leadership summary, decision register, supported measures, and explicit uncertainties.<br>
**Boundary:** no invented financial estimates or claims of improvement from incomparable counts.

### cr-asset-coverage-review

**Audience:** security operations and exposure/platform owners.<br>
**Input:** intended populations, inventory sources, enrollment/telemetry records, and freshness criteria.<br>
**Output:** reconciled assets, coverage measures with denominators, and owner follow-up.<br>
**Boundary:** absence in one export is not proof that an asset or control is absent.

### cr-software-supply-chain-review

**Audience:** AppSec, build-platform, and software owners.<br>
**Input:** release/artifact identity, manifests, lockfiles, SBOMs, build records, and verification evidence.<br>
**Output:** component/artifact discrepancies and a provenance/integrity verification backlog.<br>
**Boundary:** no package execution; a signature or attestation is not automatically proof of safety.

## 14. Command-line reference

The Desktop workflow is preferred for users who do not want to manage commands. The CLI exposes the same explicit preview/apply contract.

### Preview the recommended starter collection

```bash
crimsonray skills company preview https://github.com/crimsonray-ai/company-skills --ref v0.1.0
```

No files are installed by preview alone. Read the output and replace `TOKEN_FROM_PREVIEW` below with the returned token; it is not a literal value to reuse.

```bash
crimsonray skills company apply TOKEN_FROM_PREVIEW
```

### Select role collections explicitly

```bash
crimsonray skills company preview crimsonray-ai/company-skills --ref v0.1.0 --collections essentials soc
```

Preview again after changing the ref or collections, then apply the newly reviewed token. A CLI update is another preview followed by apply; specify the intended ref and collections explicitly.

### Target an existing named profile

```bash
crimsonray -p work skills company preview crimsonray-ai/company-skills --ref v0.1.0 --collections essentials cloud-identity
crimsonray -p work skills company apply TOKEN_FROM_PREVIEW
```

Use the same profile for preview and apply. A token created in one profile is not an installation token for another profile or another machine.

### Inspect installed libraries

```bash
crimsonray skills company list
```

For interactive per-skill enable/disable configuration, the existing CLI surface is:

```bash
crimsonray skills config
```

Use Desktop's installed Skills switches when an interactive terminal is inconvenient. Start a new conversation after changing the intended enabled inventory.

### Remove a library

```bash
crimsonray skills company remove crimsonray-ai/company-skills
crimsonray skills company apply TOKEN_FROM_REMOVAL_PREVIEW
```

The first command previews removal; the second applies only the reviewed removal token. Local changes still block it.

### Storage for support purposes

Managed files live under the active profile's `skills/company-<source-id>/` directory. Preview and recovery state lives under that profile's `company-skills/` directory. The installer resolves the profile home; users should not hardcode another person's path, copy its state, or edit the ownership metadata.

## 15. Rollout checklists and ongoing ownership

### Company readiness

- [ ] An approved Crimson Ray build contains Company Skills.
- [ ] A normal employee can authenticate and read the intended repository.
- [ ] Publishing access and content-review ownership are assigned.
- [ ] The recommended ref and role collections are documented.
- [ ] Domain owners reviewed the initial workflows and data boundaries.
- [ ] Contract checks, actual importer/scanner checks, and sanitized behavioral pilots passed.
- [ ] The company has a support route, update policy, and offboarding procedure.
- [ ] Release notes and the PDF handbook match the published library content.

### Employee readiness

- [ ] The correct local profile is selected.
- [ ] Repository URL, ref, and collections match the onboarding packet.
- [ ] The preview's source, content, and file changes were reviewed.
- [ ] Installation was explicitly approved.
- [ ] Individual enabled skills were checked in the installed Skills list.
- [ ] A new conversation successfully used a skill with synthetic or authorized evidence.
- [ ] Completed reports and evidence are stored outside the managed library.

### Maintainer release checklist

- [ ] New or changed skills have concrete inputs, procedures, and verification criteria.
- [ ] Names, short descriptions, support files, and collection memberships are valid.
- [ ] No secrets, customer evidence, hidden files, or unsupported executable artifacts were added.
- [ ] The candidate commit passed automated checks and human domain review.
- [ ] Migration effects of renamed/removed skills or collections are documented.
- [ ] A new tag was created without moving an existing release tag.
- [ ] Users know whether to stay pinned or deliberately adopt the new ref.

### Suggested ongoing cadence

Assign a recurring review appropriate to the company's change rate. Review skills when policy, telemetry, source schemas, or team responsibilities change—not only when a calendar reminder fires. Use actual support feedback and sanitized pilot results to decide whether to improve, split, or retire a workflow.

The success measure is not the number of installed skills. It is whether employees can repeatedly produce useful, traceable security decisions while keeping access, evidence, and operational changes under the company's existing controls.

---

**Source of truth:** the repository's reviewed Markdown and `company-skills.json`.<br>
**PDF distribution:** a generated release attachment; do not treat an old downloaded copy as evidence of the current application or library version.<br>
**Assurance limit:** automated validation establishes structural compatibility and scanner results, not the correctness of a security judgment or real-vendor qualification.
