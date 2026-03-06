# Luigi's Mansion 3 - The Last Resort Hotel
# Compact version - 4 floors + crown, ~40 blocks tall
# Built 25 blocks away so player can watch

def on_chat():
    player.say("Building Luigi's Mansion!")

    # Block palette
    BRK = Block.NETHER_BRICK
    STN = Block.STONE_BRICKS
    OBS = Block.OBSIDIAN
    PRI = Block.PRISMARINE
    COL = Block.COAL_BLOCK
    SEA = Block.SEA_LANTERN
    GLO = Block.GLOWSTONE
    EMR = Block.EMERALD_BLOCK
    RST = Block.REDSTONE_BLOCK
    MAG = Block.MAGMA_BLOCK
    EMP = Block.AIR
    WTR = Block.WATER
    BCN = Block.BEACON

    # Z offset - building center is 25 blocks away
    Z = 25

    def fill(blk, x1, y1, z1, x2, y2, z2):
        blocks.fill(blk, pos(x1, y1, z1 + Z), pos(x2, y2, z2 + Z))

    def pb(blk, x, y, z):
        blocks.place(blk, pos(x, y, z + Z))

    def bw(blk, x1, y1, z1, x2, y2, z2):
        fill(blk, x1, y1, z1, x2, y2, z1)
        fill(blk, x1, y1, z2, x2, y2, z2)
        fill(blk, x1, y1, z1 + 1, x1, y2, z2 - 1)
        fill(blk, x2, y1, z1 + 1, x2, y2, z2 - 1)

    def win(wb, x1, z1, x2, z2, ylo, yhi, sp):
        x = x1 + 2
        while x + 1 <= x2 - 2:
            fill(wb, x, ylo, z1, x + 1, yhi, z1)
            fill(wb, x, ylo, z2, x + 1, yhi, z2)
            x += sp
        z = z1 + 2
        while z + 1 <= z2 - 2:
            fill(wb, x1, ylo, z, x1, yhi, z + 1)
            fill(wb, x2, ylo, z, x2, yhi, z + 1)
            z += sp

    def ldg(blk, x1, z1, x2, z2, y):
        fill(blk, x1 - 1, y, z1 - 1, x2 + 1, y, z1 - 1)
        fill(blk, x1 - 1, y, z2 + 1, x2 + 1, y, z2 + 1)
        fill(blk, x1 - 1, y, z1, x1 - 1, y, z2)
        fill(blk, x2 + 1, y, z1, x2 + 1, y, z2)

    def pil(blk, x1, z1, x2, z2, y1, y2):
        fill(blk, x1, y1, z1, x1, y2, z1)
        fill(blk, x1, y1, z2, x1, y2, z2)
        fill(blk, x2, y1, z1, x2, y2, z1)
        fill(blk, x2, y1, z2, x2, y2, z2)

    # =========================================
    # FOUNDATION
    # =========================================
    fill(STN, -14, -1, -14, 14, -1, 14)
    fill(OBS, -13, 0, -13, 13, 0, 13)
    bw(BRK, -14, 0, -14, 14, 2, 14)
    fill(EMP, -13, 1, -13, 13, 2, 13)

    fill(EMP, -2, 0, -14, 2, 3, -14)
    fill(BRK, -3, 0, -14, -3, 3, -14)
    pb(GLO, -3, 4, -14)
    fill(BRK, 3, 0, -14, 3, 3, -14)
    pb(GLO, 3, 4, -14)

    fill(PRI, -2, 0, -8, 2, 1, -4)
    pb(SEA, 0, 2, -6)

    # =========================================
    # FLOOR 1 - Grand Hall (hw=10, h=8)
    # =========================================
    hw = 10
    y = 1
    h = 8
    bw(BRK, -hw, y, -hw, hw, y + h - 1, hw)
    fill(BRK, -hw, y + h, -hw, hw, y + h, hw)
    fill(EMP, -hw + 1, y + 1, -hw + 1, hw - 1, y + h - 1, hw - 1)
    fill(OBS, -hw + 1, y, -hw + 1, hw - 1, y, hw - 1)

    fill(OBS, -hw, y, -hw, -hw + 1, y + h, -hw + 1)
    fill(OBS, -hw, y, hw - 1, -hw + 1, y + h, hw)
    fill(OBS, hw - 1, y, -hw, hw, y + h, -hw + 1)
    fill(OBS, hw - 1, y, hw - 1, hw, y + h, hw)

    win(SEA, -hw, -hw, hw, hw, y + 2, y + 4, 4)
    win(SEA, -hw, -hw, hw, hw, y + 6, y + 7, 4)

    fill(EMP, -2, y + 1, -hw, 2, y + 5, -hw)
    fill(OBS, -3, y, -hw, -3, y + 6, -hw)
    fill(OBS, 3, y, -hw, 3, y + 6, -hw)
    fill(OBS, -3, y + 6, -hw, 3, y + 6, -hw)
    pb(SEA, -3, y + 5, -hw - 1)
    pb(SEA, 3, y + 5, -hw - 1)

    pb(GLO, 0, y + h - 1, 0)
    ldg(PRI, -hw, -hw, hw, hw, y + h)
    y += h + 1

    # =========================================
    # FLOOR 2 - Gallery (hw=8, h=7)
    # =========================================
    hw = 8
    h = 7
    bw(PRI, -hw, y, -hw, hw, y + h - 1, hw)
    fill(PRI, -hw, y + h, -hw, hw, y + h, hw)
    fill(EMP, -hw + 1, y + 1, -hw + 1, hw - 1, y + h - 1, hw - 1)
    fill(BRK, -hw + 1, y, -hw + 1, hw - 1, y, hw - 1)
    pil(OBS, -hw, -hw, hw, hw, y, y + h)
    win(SEA, -hw, -hw, hw, hw, y + 2, y + 4, 4)

    fill(OBS, -hw, y + 5, -hw, hw, y + 5, -hw)
    fill(OBS, -hw, y + 5, hw, hw, y + 5, hw)

    pb(GLO, 0, y + h - 1, 0)
    ldg(BRK, -hw, -hw, hw, hw, y + h)
    y += h + 1

    # =========================================
    # FLOOR 3 - Tower (hw=6, h=7)
    # =========================================
    hw = 6
    h = 7
    bw(BRK, -hw, y, -hw, hw, y + h - 1, hw)
    fill(BRK, -hw, y + h, -hw, hw, y + h, hw)
    fill(EMP, -hw + 1, y + 1, -hw + 1, hw - 1, y + h - 1, hw - 1)
    fill(COL, -hw + 1, y, -hw + 1, hw - 1, y, hw - 1)
    pil(PRI, -hw, -hw, hw, hw, y, y + h)
    win(SEA, -hw, -hw, hw, hw, y + 2, y + 4, 4)

    # Neon sign band
    fill(RST, -hw, y + 5, -hw, hw, y + 5, -hw)
    fill(MAG, -hw, y + 5, hw, hw, y + 5, hw)
    fill(GLO, -2, y + 5, -hw, 2, y + 5, -hw)
    fill(GLO, -2, y + 5, hw, 2, y + 5, hw)

    # Balconies
    fill(STN, -4, y + 3, -hw - 1, 4, y + 3, -hw - 2)
    fill(BRK, -4, y + 4, -hw - 2, 4, y + 4, -hw - 2)
    fill(STN, -4, y + 3, hw + 1, 4, y + 3, hw + 2)
    fill(BRK, -4, y + 4, hw + 2, 4, y + 4, hw + 2)

    pb(GLO, 0, y + h - 1, 0)
    ldg(PRI, -hw, -hw, hw, hw, y + h)
    y += h + 1

    # =========================================
    # FLOOR 4 - Green Crown (hw=4, h=6)
    # =========================================
    hw = 4
    h = 6
    bw(EMR, -hw, y, -hw, hw, y + h - 1, hw)
    fill(EMR, -hw, y + h, -hw, hw, y + h, hw)
    fill(EMP, -hw + 1, y + 1, -hw + 1, hw - 1, y + h - 1, hw - 1)
    fill(OBS, -hw + 1, y, -hw + 1, hw - 1, y, hw - 1)
    win(SEA, -hw, -hw, hw, hw, y + 1, y + 3, 3)
    win(SEA, -hw, -hw, hw, hw, y + 4, y + 5, 3)
    fill(SEA, -hw + 1, y + h, -hw + 1, hw - 1, y + h, hw - 1)
    ldg(OBS, -hw, -hw, hw, hw, y + h)
    y += h + 1

    # =========================================
    # CROWN & SPIRE
    # =========================================
    hw2 = 3
    bw(OBS, -hw2, y, -hw2, hw2, y + 1, hw2)

    # Corner spikes
    fill(OBS, -hw2, y + 1, -hw2, -hw2, y + 5, -hw2)
    pb(EMR, -hw2, y + 6, -hw2)
    pb(SEA, -hw2, y + 7, -hw2)
    fill(OBS, -hw2, y + 1, hw2, -hw2, y + 5, hw2)
    pb(EMR, -hw2, y + 6, hw2)
    pb(SEA, -hw2, y + 7, hw2)
    fill(OBS, hw2, y + 1, -hw2, hw2, y + 5, -hw2)
    pb(EMR, hw2, y + 6, -hw2)
    pb(SEA, hw2, y + 7, -hw2)
    fill(OBS, hw2, y + 1, hw2, hw2, y + 5, hw2)
    pb(EMR, hw2, y + 6, hw2)
    pb(SEA, hw2, y + 7, hw2)

    # Mid spikes
    fill(BRK, -hw2, y + 1, 0, -hw2, y + 4, 0)
    pb(EMR, -hw2, y + 5, 0)
    fill(BRK, hw2, y + 1, 0, hw2, y + 4, 0)
    pb(EMR, hw2, y + 5, 0)
    fill(BRK, 0, y + 1, -hw2, 0, y + 4, -hw2)
    pb(EMR, 0, y + 5, -hw2)
    fill(BRK, 0, y + 1, hw2, 0, y + 4, hw2)
    pb(EMR, 0, y + 5, hw2)

    # Central spire
    fill(OBS, 0, y, 0, 0, y + 7, 0)
    fill(EMR, 0, y + 8, 0, 0, y + 10, 0)
    pb(SEA, 0, y + 11, 0)
    pb(BCN, 0, y + 12, 0)

    pb(SEA, 2, y + 4, 0)
    pb(SEA, -2, y + 4, 0)
    pb(SEA, 0, y + 4, 2)
    pb(SEA, 0, y + 4, -2)

    pb(MAG, 1, y + 9, 0)
    pb(SEA, 1, y + 10, 0)
    pb(MAG, -1, y + 9, 0)
    pb(SEA, -1, y + 10, 0)
    pb(MAG, 0, y + 9, 1)
    pb(SEA, 0, y + 10, 1)
    pb(MAG, 0, y + 9, -1)
    pb(SEA, 0, y + 10, -1)

    player.execute("time set midnight")
    player.execute("weather thunder")
    player.say("Luigi's Mansion is complete!")

player.on_chat("1", on_chat)
