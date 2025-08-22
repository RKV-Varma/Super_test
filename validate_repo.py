import os
import sys
import re

# --- CONFIGURABLE RULES ---
REQUIRED_FILES = ["README.md", "LICENSE"]
REQUIRED_DIRS = ["src", "tests"]
REQUIRED_HEADER = "# Project"  # line that must appear in README.md
REPO_NAME_PATTERN = r"^[a-z0-9\-_]+$"  # lowercase, numbers, hyphen/underscore only

def check_required_files():
    missing = [f for f in REQUIRED_FILES if not os.path.isfile(f)]
    return missing

def check_required_dirs():
    missing = [d for d in REQUIRED_DIRS if not os.path.isdir(d)]
    return missing

def check_readme_header():
    if not os.path.isfile("README.md"):
        return False
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    return REQUIRED_HEADER in content

def check_repo_name():
    # GitHub Actions exposes the repo name in GITHUB_REPOSITORY (owner/repo)
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    repo_name = repo.split("/")[-1]
    return re.match(REPO_NAME_PATTERN, repo_name) is not None

def main():
    errors = []

    missing_files = check_required_files()
    if missing_files:
        errors.append(f"Missing required files: {', '.join(missing_files)}")

    missing_dirs = check_required_dirs()
    if missing_dirs:
        errors.append(f"Missing required directories: {', '.join(missing_dirs)}")

    if not check_readme_header():
        errors.append(f"README.md does not contain required header: {REQUIRED_HEADER}")

    if not check_repo_name():
        errors.append(f"Repo name does not match required pattern: {REPO_NAME_PATTERN}")

    if errors:
        print("Repository validation failed:")
        for e in errors:
            print(" -", e)
        sys.exit(1)  # Non-zero exit blocks the PR/check
    else:
        print("Repository validation passed.")
        sys.exit(0)

if __name__ == "__main__":
    main()
