import pandas as pd
import random

class Die():
    '''A die has N sides, or “faces”, and W weights, and can be rolled to select a face
    - W defaults to 1.0 for each face but can be changed after the object is created.Note that the weights 
        are just numbers, not a normalized probability distribution.
    - The die has one behavior, which is to be rolled one or more times.
    - Note that what we are calling a “die” here can be any discrete random variable associated with a
        stochastic process, such as using a deck of cards or flipping a coin or speaking a language. 
        Our probability model for such variable is, however, very simple 
        – since our weights apply to only to single events, we are 
        assuming that the events are independent. This makes sense 
        for coin tosses but not for language use.

    '''
    
    def __init__(self, faces):
        ''' An Initializer
        - Takes an array of faces as an argument. The array's data type (dtype) may be strings or numbers.
        - Internally iInitializes the weights to 1.0 for each face.
        - Saves both faces and weights into a private dataframe that is to be shared by the other methods.
        '''
        self.faces = faces
        self.W = [1.0] * len(self.faces)
        self.die = pd.DataFrame({'face' : self.faces, 'weight' : self.W})
        
    def change_weight(self, face, new_weight):
        ''' A method to change the weight of a single side
        - Takes two arguments: the face value to be changed and the new weight.
        - Checks to see if the face passed is valid; is it in the array of weights?
        - Checks to see if the weight is valid; is it a float? Can it be converted to one?
        '''
        if face in self.faces:
            if type(new_weight) == float:
                self.W[self.faces.index(face)] = new_weight
                self.die.at[self.faces.index(faces, 'weight'] = new_weight
            else: 
                print(f'{new_weight} is not a float')
        else:
            print(f'{face} is not a face on the die')
            
    def roll(self, nrolls = 1):
        '''A method to roll the die one or more times.
        - Takes a parameter of how many times the die is to be rolled; defaults to 1. 
        - This is essentially a random sample from the vector of faces according to the weights.
        - Returns a list of outcomes.
        - Does not store internally these results.
        '''
         return(random.choices(self.faces, weights=self.W, k=nrolls))
            
    def show_die(self):
        '''A method to show the user the die’s current set of faces and weights (since the latter can be changed).
        - Returns the dataframe created in the initializer.
        '''
        return(self.die)
    
class Game():
    '''A game consists of rolling of one or more dice of the same kind one or more times.
    - Each game is initialized with one or more of similarly defined dice (Die objects).
    - By “same kind” and “similarly defined” we mean that each die in a given game has the same number of sides and associated 
        faces, but each die object may have its own weights.
    - The class has a behavior to play a game, i.e. to rolls all of the dice a given number of times.
    - The class keeps the results of its most recent play.
    '''
    
    def __init__(self, dice):
        '''An initializer
        - Takes a single parameter, a list of already instantiated 
            similar Die objects
        '''
        self.dice = dice
        
    def play(self, krolls):
        '''A play method
        - Takes a parameter to specify how many times the dice should be rolled.
        - Saves the result of the play to a private dataframe of shape N rolls by M dice.
        - The private dataframe should have the roll number is a named index.
        - This results in a table of data with columns for roll number, the die number (its list index), 
            and the face rolled in that instance.
        '''
        self.playdf = pd.DataFrame(columns = range(1, 1+krolls))
        for die in self.dice:
            self.playdf.loc[len(self.playdf)] = die.roll(krolls)
        self.playdf.index += 1
            
    def show_game(self, form = 'wide'):
        '''A method to show the user the results of the most recent play.
        - This method just passes the private dataframe to the user.
        - Takes a parameter to return the dataframe in narrow or wide form.
        - This parameter defaults to wide form.
        - This parameter should raise an exception of the user passes an invalid option.
        - The narrow form of the dataframe will have a twocolumn index with the roll number and the die number, 
            and a column for the face rolled.
        - The wide form of the dataframe will a single column index with the roll number, and each die number as a column.
        '''
        if form == 'wide':
            return(self.playdf)
        elif form == 'narrow':
            return(self.playdf.melt(var_name = 'Roll', value_name = 'face', ignore_index=False))
        else:
            print(f'{form} is not a valid form, choose wide or narrow')
            
class Analyzer():
    '''
    An analyzer takes the results of a single game and computes various 
    descriptive statistical properties about it. These properties results are 
    available as attributes of an Analyzer object.
    '''
    
    def __init__(self, game):
        '''An initializer
        - Takes a game object as its input parameter. 
        - At initialization time, it also infers the data type of the die faces used.

        '''
        self.game = game
        
    def jackpot(self):
        '''A jackpot method to compute how many times the game resulted in all faces being identical.
        - Returns an integer for the number times to the user.
        - Stores the results as a dataframe of jackpot results in a public attribute.
        - The dataframe should have the roll number as a named index
        '''
        count = 0
        for i in range(self.game.playdf.shape[1]):
            col = list((self.game.playdf[i+1]))
            for value in col:
                check = True
                first = col[0]
                if value != first:
                    check = False
                    break
            
            if check == True:
                count += 1
            else:
                continue
        return(count)
    
    def combo(self):
        '''A combo method to compute the distinct combinations of faces rolled, along with their counts.
        - Combinations should be sorted and saved as a multicolumned index.
        - Stores the results as a dataframe in a public attribute.
        '''
        self.combos = pd.DataFrame(columns = ['combos'])
        for i in range(self.game.playdf.shape[1]):    
            col = list((self.game.playdf[i+1]))
            self.combos.loc[len(self.combos)] = [col]
        self.combos = self.combos['combos'].value_counts().reset_index(name='counts')
        return(self.combos)

    def face_count(self):
        '''A face counts per roll method to compute how many times a given face is rolled in each event.
        - Stores the results as a dataframe in a public attribute.
        - The dataframe has an index of the roll number and face values as columns (i.e. it is in wide format).
        '''
        self.game_counts = pd.DataFrame(columns = self.game.dice[1].faces)
        for i in range(self.game.playdf.shape[1]):
            col = self.game.playdf[i+1]
            roll_counts = [0]*len(self.game.dice[1].faces)
            for value in col:
                roll_counts[value-1] += 1
            self.game_counts.loc[len(self.game_counts)] = roll_counts
        self.game_counts.index += 1
        return(self.game_counts)      