def on_on_chat():
    side_size = 12  # הגודל ההתחלתי
    layer_index = 0 # מונה קומות כדי להחליף צבעים
    
    while side_size > 0:
        # בחירת הבלוק לפי מספר הקומה - פותר את בעיית ה-types
        color_choice = layer_index % 4
        
        if color_choice == 0:
            agent.set_item(Block.GOLD_BLOCK, 64, 1)
        elif color_choice == 1:
            agent.set_item(Block.DIAMOND_BLOCK, 64, 1)
        elif color_choice == 2:
            agent.set_item(Block.EMERALD_BLOCK, 64, 1)
        else:
            agent.set_item(Block.IRON_BLOCK, 64, 1)
        
        # בניית ריבוע אחד (הקומה הנוכחית)
        for side in range(4):
            for step in range(side_size):
                # הפתרון המנצח שלך למניעת התנגשות
                if side == 3 and step == side_size - 1:
                    agent.move(UP, 1)
                    agent.place(DOWN)
                else:
                    agent.move(FORWARD, 1)
                    agent.place(BACK)
            
            agent.turn(TurnDirection.LEFT)

        # הכנה לקומה הבאה
        agent.move(FORWARD, 1)
        side_size = side_size - 2
        layer_index = layer_index + 1

    # סגירה סופית של השפיץ (צ'ופר לסיום)
    agent.set_item(Block.BEACON, 1, 1)
    agent.place(DOWN)

player.on_chat("1", on_on_chat)
