movies=[]

def add_movie():
  print('Creating new movie details \n')
  movie_name=input('Enter the movie name \n')
  movie_year=input('Enter the release date \n')

  movies.append({'movie_name':movie_name, 'movie_year':movie_year})

def print_movie():
  print('Printing all the movies \n')
  for i in movies:
    print(i)

def find_movie():
  print('Finding the movie... \n')
  name=input('Enter movie name to search \n')
  for i in movies:
    if i['movie_name']==name:
      print(i)
      break
  else:
    print('No such movie found')

user_function={'a': add_movie, 'p' : print_movie, 'f' : find_movie}

def menu():
  user_input=input('Enter the selection: \n a: add movie \n p: print movie \n f: find movie \n q: quit \n')
  while user_input != 'q':
    select_function=user_function[user_input]
    select_function()
    user_input=input('Enter the selection: \n a: add movie \n p: print movie \n f: find movie \n q: quit \n')
