# Claud-Craft

Ready-to-paste Python scripts for **Minecraft Education Edition** — built with [Claude Code](https://claude.ai/claude-code).

Drop these into MakeCode's Python editor and type `1` in the game chat to watch them build.

![MakeCode Python](https://img.shields.io/badge/MakeCode-Python-blue)
![Minecraft Education](https://img.shields.io/badge/Minecraft-Education%20Edition-green)
![Built with Claude](https://img.shields.io/badge/Built%20with-Claude%20Code-blueviolet)

## The Builds

| Script | What it builds | Method |
|--------|---------------|--------|
| `colorful_pyramid.py` | A rainbow pyramid that spirals upward in gold, diamond, emerald & iron, topped with a beacon | Agent-based |
| `sports_car.py` | A red sports car with glass windows, glowstone headlights, redstone taillights & brown seats | `blocks.fill()` |
| `luigis_mansion.py` | Luigi's Mansion hotel — 4 shrinking floors + crown spire with emerald tips & beacon top | `blocks.fill()` |
| `pixel_sign.py` | Giant pixel-art sign reading "CLAUDE CODE / LOVES MINECRAFT" with diamond border | `blocks.fill()` |

## How to Use

1. Open **Minecraft Education Edition**
2. Create or join a world
3. For **agent-based** scripts: open your inventory and place the **Agent** in the world
4. Press **C** to open Code Builder
5. Switch to **Python** mode
6. Paste a script and click **Run**
7. Type **`1`** in the game chat

For `blocks.fill()` scripts, no agent needed — just stand still and type `1`.

> **Tip:** For tall builds like Luigi's Mansion, the script builds 25 blocks away so you can watch. Don't move while it builds!

## MakeCode Python Cheat Sheet

These scripts use **MakeCode Python**, which is a subset of standard Python. If you want to write your own builds, here's what to know:

### Two Ways to Build

**Agent API** — The agent bot walks around placing blocks:
```python
agent.set_item(Block.GOLD_BLOCK, 64, 1)
agent.move(FORWARD, 1)
agent.place(BACK)
agent.turn(TurnDirection.LEFT)
```

**World API** — Place blocks directly with coordinates relative to the player:
```python
blocks.place(GLOWSTONE, pos(5, 0, 3))
blocks.fill(Block.STONE, pos(0, 0, 0), pos(10, 5, 10))
```

### Gotchas

- `blocks.fill()` and `blocks.place()` need the `Block.` prefix: `Block.GOLD_BLOCK`
- Agent API does **not** need the prefix: just `GOLD_BLOCK`
- No `import math`, no `str()`, no `len()`, no tuple unpacking, no `nonlocal`, no dictionaries
- Use `if/elif` chains instead of dicts
- `NETHER_BRICK` not `NETHER_BRICKS`
- Trigger with `player.on_chat("1", your_function)`

### Coordinate System

`pos(x, y, z)` is relative to the player:
- **X** = East/West (positive = East)
- **Y** = Up/Down (positive = Up)
- **Z** = South/North (positive = South)

## Building Your Own

Want Claude Code to generate builds for you? Use the `/minecraft-builder` command:

```
/minecraft-builder a medieval castle with towers and a drawbridge
```

## License

MIT — hack away!
