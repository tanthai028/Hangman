from os import system

def interface():

  hangmans = (
    '''
    -----------
     |    
     |    
     |
     |
     |
    -------
    ''',
    '''
    -----------
     |     O
     |  
     |
     |
     |
    -------
    ''',
    '''
    -----------
     |     O
     |     |
     |    
     |
     |
    -------
    ''',
    '''
    -----------
     |     O
     |   --|
     |    
     |
     |
    -------
    ''',
    '''
    -----------
     |     O
     |   --|--
     |    
     |   
     |
    -------
    ''',
    '''
    -----------
     |     O
     |   --|--
     |     |
     |   
     |
    -------
    ''',
    '''
    -----------
     |     O
     |   --|--
     |     |
     |    | 
     |
    -------
    ''',
    '''
    -----------
     |     O
     |   --|--
     |     |
     |    | |
     |    
    -------
    '''
  )

  return hangmans

def summary(hangmans, attempts, incorrect, guessedword):
  system('clear')
  print('''
===================================''')
  print('''
    = Hangman =
  ''')
  print(hangmans[attempts])
  print(f"Incorrect guesses: {(', '.join(incorrect))}")
  print(f"Guessed word: {(' '.join(guessedword))}")
  print('''
===================================''')

  