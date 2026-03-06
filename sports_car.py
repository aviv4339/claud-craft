# Sports Car Builder
# Stand where you want the front-left corner of the car
# Type "1" in chat to build

def build_car():
    # pos(x, y, z) is relative to player position
    # x = forward/back, z = left/right, y = up/down

    # === WHEELS (black concrete, cross shape with iron hubcap) ===
    def build_wheel(wx, wy, wz):
        blocks.place(BLACK_CONCRETE, pos(wx, wy, wz))
        blocks.place(BLACK_CONCRETE, pos(wx, wy + 1, wz))
        blocks.place(BLACK_CONCRETE, pos(wx, wy - 1, wz))
        blocks.place(BLACK_CONCRETE, pos(wx, wy, wz + 1))
        blocks.place(BLACK_CONCRETE, pos(wx, wy, wz - 1))
        blocks.place(IRON_BLOCK, pos(wx, wy, wz))

    # Front wheels
    build_wheel(2, 1, 0)
    build_wheel(2, 1, 7)
    # Rear wheels
    build_wheel(9, 1, 0)
    build_wheel(9, 1, 7)

    # === UNDERCARRIAGE ===
    blocks.fill(STONE, pos(2, 0, 1), pos(2, 0, 6))
    blocks.fill(STONE, pos(9, 0, 1), pos(9, 0, 6))
    blocks.fill(STONE, pos(2, 0, 2), pos(9, 0, 5))

    # === BODY - Lower section (RED) ===
    # Floor
    blocks.fill(RED_CONCRETE, pos(1, 1, 1), pos(10, 1, 6))

    # Side panels (left and right)
    blocks.fill(RED_CONCRETE, pos(0, 2, 1), pos(11, 3, 1))
    blocks.fill(RED_CONCRETE, pos(0, 2, 6), pos(11, 3, 6))

    # Front face
    blocks.fill(RED_CONCRETE, pos(0, 2, 2), pos(0, 3, 5))

    # Rear face
    blocks.fill(RED_CONCRETE, pos(11, 2, 2), pos(11, 3, 5))

    # Hood (front top)
    blocks.fill(RED_CONCRETE, pos(0, 3, 2), pos(3, 3, 5))

    # Trunk (rear top)
    blocks.fill(RED_CONCRETE, pos(8, 3, 2), pos(11, 3, 5))

    # === CABIN / ROOF ===
    blocks.fill(RED_CONCRETE, pos(4, 5, 1), pos(7, 5, 6))

    # Cabin pillars
    blocks.fill(RED_CONCRETE, pos(4, 4, 1), pos(4, 5, 1))
    blocks.fill(RED_CONCRETE, pos(7, 4, 1), pos(7, 5, 1))
    blocks.fill(RED_CONCRETE, pos(4, 4, 6), pos(4, 5, 6))
    blocks.fill(RED_CONCRETE, pos(7, 4, 6), pos(7, 5, 6))

    # === WINDOWS (glass) ===
    blocks.fill(GLASS, pos(4, 4, 2), pos(4, 4, 5))
    blocks.fill(GLASS, pos(7, 4, 2), pos(7, 4, 5))
    blocks.fill(GLASS, pos(5, 4, 1), pos(6, 4, 1))
    blocks.fill(GLASS, pos(5, 4, 6), pos(6, 4, 6))

    # === HEADLIGHTS (glowstone) ===
    blocks.place(GLOWSTONE, pos(0, 2, 2))
    blocks.place(GLOWSTONE, pos(0, 2, 5))

    # === TAILLIGHTS (redstone block) ===
    blocks.place(REDSTONE_BLOCK, pos(11, 2, 2))
    blocks.place(REDSTONE_BLOCK, pos(11, 2, 5))

    # === BUMPERS (iron) ===
    blocks.fill(IRON_BLOCK, pos(0, 2, 3), pos(0, 2, 4))
    blocks.fill(IRON_BLOCK, pos(11, 2, 3), pos(11, 2, 4))

    # === SEATS ===
    blocks.fill(BROWN_WOOL, pos(5, 2, 2), pos(5, 2, 3))
    blocks.fill(BROWN_WOOL, pos(5, 2, 4), pos(5, 2, 5))
    blocks.fill(BROWN_WOOL, pos(6, 3, 2), pos(6, 3, 3))
    blocks.fill(BROWN_WOOL, pos(6, 3, 4), pos(6, 3, 5))

    # === STEERING WHEEL ===
    blocks.place(IRON_BLOCK, pos(4, 3, 3))

    # === ENGINE BLOCK ===
    blocks.fill(IRON_BLOCK, pos(1, 2, 3), pos(2, 2, 4))

    # === EXHAUST PIPES ===
    blocks.place(STONE, pos(11, 1, 2))
    blocks.place(STONE, pos(11, 1, 5))

    player.say("Sports car built! Vroom vroom!")

player.on_chat("1", build_car)
