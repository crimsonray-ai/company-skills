---
name: hello-world
description: Print a friendly hello-world greeting.
---

# Hello world

**Policy: extend.** Follow the active agent's access and approval rules.

## When to use

Use this skill when the user wants to try the example library or run a hello-world example.

## Procedure

1. Locate `scripts/hello.py` inside this skill's directory.
2. If an authorized command-execution capability is available, run the script with Python 3:

   ```sh
   python3 scripts/hello.py
   ```

   Run from this skill's directory, not the repository root. On Windows, use `py -3` instead of `python3` if needed.
3. Report the actual output. If execution is unavailable, show the command and expected output without claiming it ran.

## Expected result

```text
Hello, world!
```

The script uses no network, credentials, packages, or file writes. Installing the skill does not run it.
