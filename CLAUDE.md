# Minecraft Builder Project

Python scripts for MakeCode Minecraft Education Edition. Use `/minecraft-builder` skill for generating builds.

## How to use scripts
1. Open Minecraft Education Edition
2. For agent-based builds: place the **Agent bot** from your inventory into the world
3. Press `C` to open the Code Builder
4. Switch to Python mode and paste the script
5. Type `1` in the game chat to execute

For `blocks.fill()` builds, no agent needed — just stand still and type `1`.

## Key conventions
- Agent-based API: `agent.move()`, `agent.place()`, `agent.set_item()`, `agent.turn()`
- World API for complex builds: `blocks.place()`, `blocks.fill()` with `pos(x,y,z)` (relative to player)
- For tall builds: offset the structure away from the player (e.g. Z + 25), player must stand still
- Triggers: `player.on_chat("1", handler)` — always use "1" as the default trigger
- Comments in Hebrew or English
- MakeCode Python (subset of Python — no pip packages, `import math` may not work)

## MakeCode Python gotchas
- Blocks need `Block.` prefix with `blocks.fill()` / `blocks.place()`, but NOT with agent API
- No `str()` — no confirmed replacement
- No tuple unpacking in for loops
- No `nonlocal` keyword
- `NETHER_BRICK` (singular), not `NETHER_BRICKS`
- No `DARK_OAK_WOOD` or `JACK_O_LANTERN` blocks
