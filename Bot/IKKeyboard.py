class IKKeyboard:
    def create_keyboard(self, t_buttons, t_size):
        keyboard = []
        col_itr = 1
        kb_row = []
        for button in t_buttons:
            kb_row.append(button)
            if col_itr == t_size or button == t_buttons[-1]:
                kb_row_copy = kb_row.copy()
                keyboard.append(kb_row_copy)
                kb_row = []
                col_itr = 1
            else:
                col_itr += 1
        return keyboard

