#!/usr/bin/python3
def lenList(list):
  cnt = 0;
  for i in list:
    cnt += 1;
  return cnt;

def safe_print_list(my_list=[], x=0):
  try:
    output = ""
    if(x > lenList(my_list)):
      for i in range(0, lenList(my_list)):
        output += str(my_list[i]);
      return output;
    else:
      for i in range(0, x):
        output += str(my_list[i]);
      return output
  except:
    return "Unknown error has occured!"
