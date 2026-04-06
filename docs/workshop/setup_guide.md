# Setup Guide -- Agentic Coding for Economists

Complete this guide **before Day 1**. Allow 30--60 minutes. If you run into problems,
email the instructor with the exact error message.

---

## Quick Checklist

- [ ] GitHub account created and SSH key configured
- [ ] Python 3.10+ installed
- [ ] Cursor IDE installed
- [ ] Git installed and configured
- [ ] Node.js installed
- [ ] LaTeX distribution installed
- [ ] Pandoc installed
- [ ] VS Code installed (optional backup editor)
- [ ] All Python packages installed
- [ ] `validate_setup.py` passes all checks

---

## 1. GitHub Account

If you don't have one, create a free account at https://github.com.

Configure Git with your identity:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@university.edu"
```

Generate an SSH key (recommended) or use HTTPS with a personal access token:

```bash
ssh-keygen -t ed25519 -C "your.email@university.edu"
cat ~/.ssh/id_ed25519.pub
# Copy the output and add it at https://github.com/settings/ssh/new
```

---

## 2. Python (3.10+)

### Path A: No admin access (recommended for corporate/institutional machines)

**Option 1: uv (fastest, single binary)**

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then install Python via uv:

```bash
uv python install 3.12
```

**Option 2: Miniconda / Anaconda (user-space)**

Download from https://docs.anaconda.com/miniconda/ and install to your home directory
(no admin needed). Then:

```bash
conda create -n econ python=3.12
conda activate econ
```

### Path B: Admin access available

**macOS:**
```bash
brew install python@3.12
```

**Windows:** Download from https://python.org/downloads/ and run the installer.
Check "Add Python to PATH".

**Linux (Ubuntu/Debian):**
```bash
sudo apt update && sudo apt install python3.12 python3.12-venv python3-pip
```

### Verify

```bash
python --version   # Should show 3.10 or higher
```

---

## 3. Cursor IDE

Download from https://www.cursor.com/downloads.

**macOS:** Drag to `/Applications` (admin) or `~/Applications` (no admin).

**Windows:** Run the installer. The default user-mode install requires no admin.

**Linux:** Download the AppImage. Make it executable and run:

```bash
chmod +x cursor-*.AppImage
./cursor-*.AppImage
```

After installation:
1. Open Cursor and sign in (or create an account).
2. Cursor includes a bundled Git -- but a system-level install is recommended.

---

## 4. Git

### Path A: No admin access

Cursor bundles Git, which may be sufficient. Alternatively:

```bash
# via conda
conda install git

# via uv (if available)
# Git is a system tool; prefer conda or IT pre-install
```

### Path B: Admin access

**macOS:**
```bash
# Xcode command line tools (includes git)
xcode-select --install
# Or via Homebrew
brew install git
```

**Windows:** Download from https://git-scm.com/download/win.

**Linux:**
```bash
sudo apt install git
```

### Verify

```bash
git --version   # Should show 2.30 or higher
```

---

## 5. GitHub CLI (optional but recommended)

```bash
# via conda (no admin)
conda install gh --channel conda-forge

# macOS with admin
brew install gh

# Windows with admin
winget install GitHub.cli
```

Then authenticate:

```bash
gh auth login
```

---

## 6. Node.js

Required for MCP servers and some Cursor extensions.

### Path A: No admin access

```bash
# via conda
conda install nodejs

# Or use nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install --lts
```

### Path B: Admin access

Download LTS from https://nodejs.org/ and install.

### Verify

```bash
node --version   # Should show v18 or higher
npm --version
```

---

## 7. LaTeX Distribution

### Path A: No admin access

**TinyTeX (lightweight, user-space):**

```bash
# macOS / Linux
curl -sL "https://yihui.org/tinytex/install-bin-unix.sh" | sh

# Windows (PowerShell)
Invoke-WebRequest -Uri "https://yihui.org/tinytex/install-bin-windows.bat" -OutFile "install-tinytex.bat"
.\install-tinytex.bat
```

Install required packages:

```bash
tlmgr install beamer pgf tikz-cd booktabs natbib amsmath amssymb
```

**Overleaf (online fallback):** If LaTeX install fails, use https://overleaf.com
(free account). Upload `.tex` files directly.

### Path B: Admin access

**macOS:**
```bash
brew install --cask mactex
```

**Windows:** Download and install MiKTeX from https://miktex.org/download.

**Linux:**
```bash
sudo apt install texlive-full
```

### Verify

```bash
pdflatex --version
bibtex --version
```

---

## 8. Pandoc

### Path A: No admin access

```bash
conda install -c conda-forge pandoc
```

### Path B: Admin access

```bash
# macOS
brew install pandoc

# Windows
winget install JohnMacFarlane.Pandoc

# Linux
sudo apt install pandoc
```

### Verify

```bash
pandoc --version
```

---

## 9. VS Code (optional backup editor)

Download from https://code.visualstudio.com/. User-mode install available on all
platforms (no admin needed).

Recommended extensions (install from Extensions sidebar):
- Python (Microsoft)
- LaTeX Workshop
- Marp for VS Code
- GitHub Pull Requests
- Markdown All in One

---

## 10. Python Packages

Navigate to the course repository and install dependencies:

```bash
# If using uv
uv pip install -r requirements.txt

# If using conda
pip install -r requirements.txt

# If using standard pip
pip install -r requirements.txt
```

Or install from `pyproject.toml`:

```bash
uv pip install -e ".[dev]"
```

---

## 11. Optional: Additional Tools

### Claude Code (Anthropic CLI)

```bash
npm install -g @anthropic-ai/claude-code
```

### OpenAI Codex CLI

```bash
npm install -g @openai/codex
```

### MCP Servers for Domain-Specific Tools

If you use Stata, MATLAB, or R, MCP servers can connect these tools to Cursor.
The instructor will provide configuration during Day 3's MCP module.

---

## 12. Verify Everything

Run the validation script from the course repository root:

```bash
python scripts/validate_setup.py
```

This checks all required tools and packages. Fix any failures before Day 1.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `python` not found | Try `python3` instead. On Windows, check PATH. |
| `git` permission denied | Re-run SSH key setup; check `ssh -T git@github.com`. |
| Cursor won't start on Linux | Ensure AppImage has execute permission: `chmod +x cursor-*.AppImage`. |
| `pip install` fails with permission error | Use `--user` flag or activate a virtual environment first. |
| LaTeX package missing | Run `tlmgr install <package-name>` or let MiKTeX auto-install. |
| Node.js version too old | Use `nvm install --lts` to get the latest LTS version. |
| No internet during install | See `OFFLINE_FALLBACK.md` for pre-cached install options. |
