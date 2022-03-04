# Bowling score generator: https://bowlinggenius.com/

class BowlingGame:
    newFrame = True
    frames = { 0:"", 1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8:"", 9:"" }
    scoreboard = []
    total_score = 0

    def __init__(self):
        pass

    def strike(i): # strike = current score + next 2 rolls
        temp_score = 0
        n = 0
        while n < 3: 
            value = BowlingGame.frames[i + n]
            if len(value) == 1: 
                temp_score += sum(value)
                n += 1
            if n == 2 and len(value) == 2: 
                temp_score += sum(value)
                n += 2
            if n == 1 and len(value) == 2: 
                temp_score += value[0]
                n += 1
        BowlingGame.total_score += temp_score
        return 

    def spare(i): # spare = current score + next 1 roll
        temp_score = 0
        frame = BowlingGame.frames[i]
        temp_score += sum(frame)
        frame = BowlingGame.frames[i + 1]
        temp_score += frame[0]

        BowlingGame.total_score += temp_score
        return 

    def roll(self, pins):
        if pins > 10: raise ValueError("Can't score more than 10 points.")
        BowlingGame.scoreboard.append(pins)


    def score(self):
        counter = 0
        frames = BowlingGame.frames
        scoreboard = BowlingGame.scoreboard
        while len(scoreboard) > 0:
            if counter > 9: 
                temp = list(frames.values())[9]
                frames[9].append(scoreboard[0])

                break
            if scoreboard[0] == 10:
                frames.update({counter:[scoreboard[0]]})
                scoreboard.pop(0)
                counter += 1
            elif len(list(frames.values())[counter]) == 0 and scoreboard[0] < 10:
                frames.update({counter:[scoreboard[0]]})
                scoreboard.pop(0)
            elif len(list(frames.values())[counter]) == 1 and scoreboard[0] < 10:
                temp = list(frames.values())[counter]
                temp.append(scoreboard[0])
                frames.update({counter:temp})
                scoreboard.pop(0)
                counter += 1

        BowlingGame.frames = frames

        for key, value in enumerate(frames.items()):
            is_strike = False
            is_spare = False
            frame_10 = False
            if sum(value[1]) == 10 and len(value[1]) == 2: is_spare = True
            if sum(value[1]) == 10 and len(value[1]) == 1: is_strike = True
            if key == 9:
                frame_10 = True
                is_strike = False
                is_spare = False
            if sum(value[1]) > 10 and not frame_10: raise ValueError("Can't score more than 10 points in a single frame.")
            if is_strike:
                BowlingGame.strike(key)
            elif is_spare:
                BowlingGame.spare(key)
            else:
                BowlingGame.total_score += sum(value[1])

        return BowlingGame.total_score

            

        
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
    # rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3, 7] # 17
    # rolls = [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 10
    rolls = [10, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 26


    game = roll_new_game(rolls)
    print(game.score())
    


if __name__ == '__main__':
    main()


"""
I'm stuck! I'm making this more difficult than it should be, and I don't know how to simplify or what to consider for next steps. 

Would you help me with next steps?

Here's my process: 

 1. Define class variables `BowlingGame.frames` as a dictionary with 10 key-value pairs and `BowlingGame.scoreboard`, an empty list.
 2. `roll()` method transposes the list argument to the class variable `BowlingGame.scoreboard`.
 3. When `score()` method is called, `BowlingGame.frames` is updated with the `BowlingGame.scoreboard` 
 4. `BowlingGame.frames` is used to calculate the score
 
  """