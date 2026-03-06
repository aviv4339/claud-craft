# Big sign: "CLAUDE CODE" / "LOVES MINECRAFT"
# Pixel art sign - stand still and type "1" in chat

def on_chat():
    Z = 25
    S = 2

    # Glyph data: [width, ...pixel rows flattened...]
    # 5 rows top-to-bottom, each row has 'width' values (0 or 1)
    def glyph(ch):
        if ch == "C":
            return [4, 0,1,1,0, 1,0,0,0, 1,0,0,0, 1,0,0,0, 0,1,1,0]
        elif ch == "L":
            return [4, 1,0,0,0, 1,0,0,0, 1,0,0,0, 1,0,0,0, 1,1,1,1]
        elif ch == "A":
            return [5, 0,1,1,1,0, 1,0,0,0,1, 1,1,1,1,1, 1,0,0,0,1, 1,0,0,0,1]
        elif ch == "U":
            return [4, 1,0,0,1, 1,0,0,1, 1,0,0,1, 1,0,0,1, 0,1,1,0]
        elif ch == "D":
            return [4, 1,1,1,0, 1,0,0,1, 1,0,0,1, 1,0,0,1, 1,1,1,0]
        elif ch == "E":
            return [4, 1,1,1,1, 1,0,0,0, 1,1,1,0, 1,0,0,0, 1,1,1,1]
        elif ch == "O":
            return [4, 0,1,1,0, 1,0,0,1, 1,0,0,1, 1,0,0,1, 0,1,1,0]
        elif ch == "S":
            return [4, 0,1,1,0, 1,0,0,0, 0,1,1,0, 0,0,0,1, 1,1,1,0]
        elif ch == "V":
            return [5, 1,0,0,0,1, 1,0,0,0,1, 0,1,0,1,0, 0,1,0,1,0, 0,0,1,0,0]
        elif ch == "M":
            return [5, 1,0,0,0,1, 1,1,0,1,1, 1,0,1,0,1, 1,0,0,0,1, 1,0,0,0,1]
        elif ch == "I":
            return [3, 1,1,1, 0,1,0, 0,1,0, 0,1,0, 1,1,1]
        elif ch == "N":
            return [5, 1,0,0,0,1, 1,1,0,0,1, 1,0,1,0,1, 1,0,0,1,1, 1,0,0,0,1]
        elif ch == "R":
            return [4, 1,1,1,0, 1,0,0,1, 1,1,1,0, 1,0,1,0, 1,0,0,1]
        elif ch == "F":
            return [4, 1,1,1,1, 1,0,0,0, 1,1,1,0, 1,0,0,0, 1,0,0,0]
        elif ch == "T":
            return [5, 1,1,1,1,1, 0,0,1,0,0, 0,0,1,0,0, 0,0,1,0,0, 0,0,1,0,0]
        else:
            return [2, 0,0, 0,0, 0,0, 0,0, 0,0]

    # Draw one character, returns its pixel width
    # Combines horizontal runs of pixels into single fill calls
    def draw_char(ch, bx, by, color):
        g = glyph(ch)
        w = g[0]
        for row in range(5):
            py = by + (4 - row) * S
            col = 0
            while col < w:
                if g[1 + row * w + col] == 1:
                    run_start = col
                    while col < w:
                        if g[1 + row * w + col] == 1:
                            col = col + 1
                        else:
                            break
                    px1 = bx + run_start * S
                    px2 = bx + col * S - 1
                    blocks.fill(color,
                        pos(px1, py, Z),
                        pos(px2, py + S - 1, Z))
                else:
                    col = col + 1
        return w

    # Characters for each line (as lists, no dict needed)
    line1 = ["C","L","A","U","D","E"," ","C","O","D","E"]
    line2 = ["L","O","V","E","S"," ","M","I","N","E","C","R","A","F","T"]

    # Pre-computed pixel widths
    w1 = 53
    w2 = 76
    max_w = 76

    pad = 2
    gap = 3
    panel_pw = max_w + pad * 2
    panel_ph = 5 + gap + 5 + pad * 2
    sw = panel_pw * S
    sh = panel_ph * S
    start_x = 0 - (sw // 2)

    # Black background panel
    blocks.fill(Block.BLACK_CONCRETE,
        pos(start_x, 0, Z),
        pos(start_x + sw - 1, sh - 1, Z))

    # Diamond border
    blocks.fill(Block.DIAMOND_BLOCK,
        pos(start_x - 1, -1, Z), pos(start_x + sw, -1, Z))
    blocks.fill(Block.DIAMOND_BLOCK,
        pos(start_x - 1, sh, Z), pos(start_x + sw, sh, Z))
    blocks.fill(Block.DIAMOND_BLOCK,
        pos(start_x - 1, -1, Z), pos(start_x - 1, sh, Z))
    blocks.fill(Block.DIAMOND_BLOCK,
        pos(start_x + sw, -1, Z), pos(start_x + sw, sh, Z))

    # Draw "CLAUDE CODE" in gold (top line)
    y1 = (pad + 5 + gap) * S
    off1 = pad + (max_w - w1) // 2
    cx = start_x + off1 * S
    for i in range(11):
        w = draw_char(line1[i], cx, y1, Block.GOLD_BLOCK)
        cx = cx + (w + 1) * S

    # Draw "LOVES MINECRAFT" in emerald (bottom line)
    y2 = pad * S
    off2 = pad + (max_w - w2) // 2
    cx = start_x + off2 * S
    for i in range(15):
        w = draw_char(line2[i], cx, y2, Block.EMERALD_BLOCK)
        cx = cx + (w + 1) * S

    # Redstone separator between lines
    sep_y = (pad + 5 + 1) * S
    blocks.fill(Block.REDSTONE_BLOCK,
        pos(start_x + pad * S, sep_y, Z),
        pos(start_x + (pad + max_w) * S - 1, sep_y + S - 1, Z))

    # Glowstone accents top and bottom
    for i in range(0, sw + 2, 4):
        blocks.place(Block.GLOWSTONE, pos(start_x - 1 + i, sh + 1, Z))
        blocks.place(Block.GLOWSTONE, pos(start_x - 1 + i, -2, Z))

    # Iron pillars with beacons
    blocks.fill(Block.IRON_BLOCK,
        pos(start_x - 3, -2, Z), pos(start_x - 2, sh + 2, Z))
    blocks.fill(Block.IRON_BLOCK,
        pos(start_x + sw + 1, -2, Z), pos(start_x + sw + 2, sh + 2, Z))
    blocks.place(Block.BEACON, pos(start_x - 3, sh + 3, Z))
    blocks.place(Block.BEACON, pos(start_x + sw + 2, sh + 3, Z))

    player.say("Sign complete!")

player.on_chat("1", on_chat)
