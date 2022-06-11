def print_full_name(first, last):
  if ((len(first_name))+(len(last_name))) <= 10:
    print("Hello "+ first_name.title() + " " + last_name.title() + "!" + " You just delved into python.")
  else:
    print("You entered invalid input")

  return(first, last)

if __name__ == '__main__':
  first_name = input('First Name: ')
  last_name = input('Last Name: ')
  
  print_full_name(first_name, last_name)
