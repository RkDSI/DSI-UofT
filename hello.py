def say_hello (name: str, repeat: int=1, goodbye:bool= False) -> None:
  ''' Echos Hello parameter for n times
  Parameters:
  -----------
  name: str
     The name of the person or theing to repeat
  repeat: int =1
     Repeats the message of Hello 'Name'
  goodbye:bool = False
     if true says goodbye.

  Returns
  -------
  greeting : str
    The string that was printed to stdout.

  Examples:
  ---------
  >>> say_hello ('World')
     Hello, World!
  >>> say_hello ('Alice')
     Hello, Alice!
     '''
  if goodbye:
    message = 'Goodbye'
  else:
    message = 'Hello'
  for _ in range (repeat):
    print (f'{message} {name}')

say_hello ('World', 5)
