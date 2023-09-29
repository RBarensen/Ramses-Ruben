import random
from bke import MLAgent, is_winner, opponent, RandomAgent, train_and_plot, validate, plot_validation

class MyAgent(MLAgent):  #Hier kan de agent inzien hoe belangrijk ieder vakje is
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1  
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward

random.seed(1)
 
my_agent = MyAgent()
random_agent = RandomAgent()
my_agent = MyAgent(alpha=0.05, epsilon=0.01) #Hier kun je voor de agent instellen met behulp van alpha en epsilon hoe snel hij nieuwe kennis opneemt en hoeveel nieuwe zetten hij probeert

train_and_plot( #Dit stuk code programmeert de training van de agent 
    agent=my_agent,
    validation_agent=random_agent,
    iterations=100,
    trainings=1000,
    validations=10)

validation_agent = RandomAgent()
 
validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)
 
plot_validation(validation_result) #Hier worden de trainingsresultaten geplot