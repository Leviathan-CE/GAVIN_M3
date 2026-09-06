# GAVIN M3

GAVIN (Generative Artificial Virtual Intelligence Network) is a local desktop chat app. It uses **PyQt6** for the window, talks to **OpenAI** (`gpt-3.5-turbo`), and stores chat history in SQLite.

## Prerequisites

- **Python 3.10+** (3.12 is a safe choice; PyQt WebEngine can be picky on very new Python versions)
- An **OpenAI API key**
- Run commands from the **project root** (`GAVIN_M3`). Paths and imports are relative to the current working directory.

## Setup

Create a virtual environment and install the packages the app actually imports:

```bash
python -m venv .venv
```

**Windows (PowerShell or Git Bash):**

```bash
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

Then install:

```bash
pip install PyQt6 PyQt6-WebEngine openai mistune cryptography
```

| Package | Why it is needed |
|---|---|
| `PyQt6` | Window, widgets, layout |
| `PyQt6-WebEngine` | Renders markdown + LaTeX in chat |
| `openai` | Sends prompts to `gpt-3.5-turbo` |
| `mistune` | Converts markdown (including math) to HTML |
| `cryptography` | Encrypts the API key on disk |

## Run

From the project root, with the venv active:

```bash
python gavin_m3.py
```

The entry point is `gavin_m3.py`. It builds the main window, loads `src/gui/styles/dark_mode.css`, and starts the Qt event loop.

**First launch:** if no valid key is stored, an **API key form** appears. Paste your OpenAI key and confirm. The app tests it with a small `gpt-3.5-turbo` request. If the key is accepted, the form closes and you can start the app again to open the chat window.

After that, type in the input bar and send. Replies are saved in `src/data/Leviathan_local.db`.

## Where secrets live

Do not commit these (they are already in `.gitignore`):

- `src/data/config.ini` — Fernet encryption key
- `src/data/Key_manager.db` — encrypted API key

If you delete them, the app will ask for the OpenAI key again.

## If imports fail

The code expects you to start Python from `GAVIN_M3` so `from src....` works. If you still get `ModuleNotFoundError`, add the project root to `PYTHONPATH`:

**Windows:**

```bash
set PYTHONPATH=%PYTHONPATH%;C:\Users\LeviM\OneDrive\Desktop\GAVIN_M3
```

**macOS / Linux:**

```bash
export PYTHONPATH="${PYTHONPATH}:/path/to/GAVIN_M3"
```

Then run `python gavin_m3.py` again.

## Optional: build a one-file executable

`gavin_m3.spec` is a PyInstaller spec. After `pip install pyinstaller`:

```bash
pyinstaller gavin_m3.spec
```

The output lands in `dist/`. This is optional; day-to-day development uses `python gavin_m3.py`.

## Troubleshooting

- **Window never opens / traceback in the terminal** — look at `src/error_log.txt`. The entry point writes failures there.
- **Must run from the repo root** — `src/data/Paths.py` resolves folders from the current working directory. Running the file from another folder will break styles, images, and the database path.
- **API key rejected** — the key is tested against OpenAI on save. Check that it is a live key and that your account can call `gpt-3.5-turbo`.
- **PyQt6-WebEngine install fails** — try Python 3.12 in a fresh venv, then reinstall the packages above.
