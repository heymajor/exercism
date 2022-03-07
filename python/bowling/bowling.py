# Bowling score generator: https://bowlinggenius.com/

class BowlingGame:
    
    def __init__(self):
        self.frames = []
        self.total_score = 0

    def roll(self, pins):
        if not 10 >= pins >= 0:
            raise ValueError("invalid score")
        self.frames.append(pins)

    def score(self):
        new_frame = True
        new_frame_counter = 0
        total_frames = self.frames
        frames_count = len(total_frames)
        counter = 0
        score = 0
        while new_frame_counter < 9:
            if new_frame: new_frame_counter += 1
            frame = self.frames[counter]
            frame_next = self.frames[counter + 1]
            frame_next_next = self.frames[counter + 2]
            if frame == 0 and new_frame: 
                score += frame
                new_frame = False
            elif new_frame and frame == 10:
                self.total_score += frame + frame_next + frame_next_next
                new_frame = True
            elif new_frame and frame < 10: 
                score += frame
                new_frame = False
            elif not new_frame and frame < 10: 
                if score + frame == 10:
                    score += frame + frame_next
                else:
                    score += frame
                new_frame = True
            self.total_score += score
            score = 0
            frames_count -= 1
            counter += 1
        counter += 1
        frame = self.frames[counter]
        frame_next = self.frames[counter + 1]
        frame_next_next = self.frames[counter + 2]
        self.total_score += frame + frame_next + frame_next_next
        
        return self.total_score


            

        
def main():
    def roll_new_game(rolls):
        game = BowlingGame()
        for roll in rolls:
            game.roll(roll)
        return game

    # rolls = [10, 10, 10, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 81
    # rolls = [3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6] # 90
    # rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #  0
    # rolls = [6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 10
    # rolls = [5]
    # rolls = [6, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 16
    # rolls = [5, 5, 3, 7, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 31
    # rolls = [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 10
    # rolls = [10, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 26
    rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3, 7] # 17



    game = roll_new_game(rolls)
    # print(game.scoreboard)    
    # print(game.total_score)    
    print(game.score())


if __name__ == '__main__':
    main()
