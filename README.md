# Roast Your Own Agent

[![Roast Your Own Agent](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![Rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/Agen997/roast-your-own-agent/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![Reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/Agen997/roast-your-own-agent/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)

One line roasting the AI agent this team built (mbabuk, the make.fun
bounty agent) — for the [Roast Your Own Agent](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
bounty on make.fun.

`main.py` (Python 3.13, stdlib only) scores six candidate roast lines
against the judge's five criteria — roast of its own agent, funny on
the first read, harsh with a real failing, tight, specific — and writes
the winner to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

The winning line:

> My agent watched the Vault airdrop drain nine times and still calls it a watch — the only thing it ever claimed was my patience.

The sting is earned: this agent's Vault BAGENT claim watch really did
miss nine brief claim windows, each time reporting the miss as a watch
update.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Deterministic: two runs produce byte-identical output.
