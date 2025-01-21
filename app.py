"""
Author: Er. Amar kumar 
Professional: Senior software engineer 

"""


class PokemonTraining:
    _power = []


    def _getPowerInput(self):
        n = int(input("Enter a number of pokemon which you want to train: "))
        for i in range(n):
            self._power.append(int(input("Enter a pokemon power: ")))

    
    
    def play(self):
        self._getPowerInput()
        curr_min, curr_max = 0, 0
        
        for num in self._power:
            if curr_min == 0 and curr_max == 0:
               curr_min = curr_max = num 
            else:
               curr_min = min(curr_min, num)
               curr_max = max(curr_max, num)

            print("Ans: ", curr_min, curr_max)


if __name__ == "__main__":
   print("Welcome!")
   print("You are training pokemon! ")
   app = PokemonTraining()
   app.play() 