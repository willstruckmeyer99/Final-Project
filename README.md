# Final-Project

# Metadata

```
Course:  DS 5100
Module: Final Project
Title:   Monte CArlo Simulator
Author:  Will Struckmeyer
Datae:   05/02/2023
```
# Synopsis

```
Installing: To install package use the code "pip install -e." while in the source directory.
Importing: To import use the code "import montecarlo" or to import any of the classes use "from montecarlo import -class name-"
Creating Dice Object: To create a Die use the code "-die obj name- = Die(-array of die faces-)" 
                      To change the weight of a face on the die use "-die obj name-.change_weight(-face-, -new weight-)"
                      To see a dataframe of the die object containg the faces and their weights use "-die obj name-.show_die()"
Playing a Game: To play a game first create a game object using "-game obj name- = Game(-list of dice objects-)"
                Next to initaiate the game use "-game obj name-.play(-number of rolls-)"
                To see a dataframe of the resulting game use "-game obj name-.show_game()"
Analyzing a Game: To Analyze the results of a game first creat an Analyzer object of an already created and played game object using "-analyzer obj name- =  Analyzer(-game object-)"
                  To calculate the total number of jackpots (rolls where all dice land on the same face) in the game use "-analyzer obj name-.jackpot()"
                  To see a dataframe containg all the possible combinations of faces rolled and their frequencies use "-analyzer obj name-.combo()"
                  To see a datframe containg a list with the counts of each face for each roll use "-analyzer obj name-.face_count()"
```

# API Description

```
Die class(): 
    Doc String: A die has N sides, or “faces”, and W weights, and can be rolled to select a face
                    - W defaults to 1.0 for each face but can be changed after the object is created.Note that the weights 
                        are just numbers, not a normalized probability distribution.
                    - The die has one behavior, which is to be rolled one or more times.
                    - Note that what we are calling a “die” here can be any discrete random variable associated with a
                        stochastic process, such as using a deck of cards or flipping a coin or speaking a language. 
                        Our probability model for such variable is, however, very simple 
                    – since our weights apply to only to single events, we are 
                        assuming that the events are independent. This makes sense for coin tosses but not for language use.
                        
    Attributes:
        - faces: A list containg all the possible outcome or faces in a die object
        - W: A list of floats containing the corresponding weights of each face on the die
        - die: A dataframe containg columns for bothe faces and W.
        
    Methods:
        - __init__(faces): An Initializer
                            - Takes an array of faces as an argument. The array's data type (dtype) may be strings or numbers.
                            - Internally iInitializes the weights to 1.0 for each face.
                            - Saves both faces and weights into a private dataframe that is to be shared by the other methods.
        - change_weight(face, new_weight): A method to change the weight of a single side
                                            - Takes two arguments: the face value to be changed and the new weight.
                                            - Checks to see if the face passed is valid; is it in the array of weights?
                                            - Checks to see if the weight is valid; is it a float? Can it be converted to one?
                                           Returns an updated version of the 'die' attribute
        - roll(nrolls = 1): A method to roll the die one or more times.
                                - Takes a parameter of how many times the die is to be rolled; defaults to 1. 
                                - This is essentially a random sample from the vector of faces according to the weights.
                                - Returns a list of outcomes.
                                - Does not store internally these results.
        - show_die(): A method to show the user the die’s current set of faces and weights (since the latter can be changed).
                      Returns the'die' object

Game class:
    Doc String: A game consists of rolling of one or more dice of the same kind one or more times.
                    - Each game is initialized with one or more of similarly defined dice (Die objects).
                    - By “same kind” and “similarly defined” we mean that each die in a given game has the same number of sides and associated 
                        faces, but each die object may have its own weights.
                    - The class has a behavior to play a game, i.e. to rolls all of the dice a given number of times.
                    - The class keeps the results of its most recent play.
                    
    Attributes:
        - dice: A list of die objects 
        - playdf: A dataframe containing the resulting face values for each die and each role from playing a game N rolls by M dice
        
    Methods: 
        - __init__(dice): An initializer
                            - Takes a single parameter, a list of already instantiated similar Die objects
        - play(krolls): A play method
                            - Takes a parameter to specify how many times the dice should be rolled.
                            - Saves the result of the play to a private dataframe of shape N rolls by M dice.
                            - The private dataframe should have the roll number is a named index.
                            - This results in a table of data with columns for roll number, the die number (its list index), 
                                and the face rolled in that instance.
        - show_game(form = 'wide'): A method to show the user the results of the most recent play.
                                        - This method just passes the private dataframe to the user.
                                        - Takes a parameter to return the dataframe in narrow or wide form.
                                        - This parameter defaults to wide form.
                                        - This parameter should raise an exception of the user passes an invalid option.
                                        - The narrow form of the dataframe will have a twocolumn index with the roll number and the die number, 
                                            and a column for the face rolled.
                                        - The wide form of the dataframe will a single column index with the roll number, and each die number as a column.
                                     Returns 'playdf' attribute

Analyzer Class;
    Doc String:  An analyzer takes the results of a single game and computes various descriptive statistical properties about it. 
                 These properties results are available as attributes of an Analyzer object.
                 
    Attributes:
        - game: A game object created using Game
        - combos: A dataframe containing every combination of faces rolled in a game along with their counts
        - game_counts: A dataframe containg counts of each face rolled per roll in a game
       
    Methods:
        - __init__(game): An initializer
                            - Takes a game object as its input parameter. 
                            - At initialization time, it also infers the data type of the die faces used.
        - jackpot(): A jackpot method to compute how many times the game resulted in all faces being identical.
                        - Returns an integer for the number times to the user.
                        - Stores the results as a dataframe of jackpot results in a public attribute.
                        - The dataframe should have the roll number as a named index
                     Returns an int count
        - combo(): A combo method to compute the distinct combinations of faces rolled, along with their counts.
                        - Combinations should be sorted and saved as a multi columned index.
                        - Stores the results as a dataframe in a public attribute.
                   Returns 'combos' attribute
        - face_count(): A face counts per roll method to compute how many times a given face is rolled in each event.
                            - Stores the results as a dataframe in a public attribute.
                            - The dataframe has an index of the roll number and face values as columns (i.e. it is in wide format).
                        Returns 'game_counts' attribute

```

# Manifest

```
Src file
    - monte_carlo
        - montecarlo.py
        - __init__.py
        
    - tests
        - monte_carlo_test.py
        - monte_carlo_testresults.txt
        
    - FinalProjectSubmission.ipynb
    - setup.py
    - README.md
    - LICENSE
```
