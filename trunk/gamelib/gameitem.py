
class GameItem(object):

    next_id = 0
    arena = None
    remove_from_game = False

    def __init__(self):
        self.id = GameItem.next_id
        GameItem.next_id += 1


    def update_sprite_stats(self):
        self.center_x = self.sprite.width/2
        self.center_y = self.sprite.height/2
        self.width = self.sprite.width
        self.height = self.sprite.height


