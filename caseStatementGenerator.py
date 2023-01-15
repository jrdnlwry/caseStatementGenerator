# import needed libraries
import re

# Functioning REGEX CODE FUNCTION
def regexBasedGrouping():
  # request the TLD extension to strip from the URL
  # this will also remove the domain name
  tld = input("Please type your TLD extension: ")
  cases = []
  more_cases = True
  while more_cases:
    # prompt user for all URLs to begin creating corresponding Regex 
    value = input("Input the URLs to build the regex (space separated) (or enter 'done' to finish): ")
    
    # if the user inputs done then terminate the loop
    if value.lower() == "done":
      more_cases = False
    else:
      # split the string inputs by whitespace & convert to list
      urls = list(value.split(" "))
      u_list = []
      for url in urls:
        # remove the domain extension/name from before
        i = re.sub(f".*\{tld}",'',url)
        u_syntax = ".*" + i + ".*"
        u_list.append(u_syntax)
        items = '|'.join(u_list)  

      result = input("Enter the corresponding value to return if the match is successful: ")
      cases.append((items, result))

  return cases
  
  
def syntaxBasedGrouping():
  syntaxCases = []
  more_cases = True
  while more_cases:
    value = input("Input the URL syntax to build the regex (space separated) i.e. /blog/ (or enter 'done' to finish): ")
    if value.lower() == "done":
      more_cases = False
    else:
      # split the string inputs by whitespace & convert to list
      syntaxFragment = list(value.split(" "))
      syntax = []
      # iterate through the supplied syntax
      for i in syntaxFragment:
        u_syntax = ".*" + i + ".*"
        syntax.append(u_syntax)
        items = '|'.join(syntax) 

      result = input("Enter the corresponding value to return if the match is successful: ")
      syntaxCases.append((items, result))

  return syntaxCases
  
  
def generate_case_statement(caseSyntax):
  case_field = input("Enter the field on which to perform the case statement: ")
  # need to pass cases into this function
  cases = caseSyntax

  default_value = input("Enter the default value to return if no matches are found: ")
  
  case_statement = "CASE"
  for case in cases:
    # case_statement += f" WHEN {case_field} = '{case[0]}' THEN '{case[1]}'"
    case_statement += f" WHEN REGEXP_MATCH({case_field}, '{case[0]}') THEN '{case[1]}'"
  case_statement += f" ELSE '{default_value}'"
  case_statement += " END"
  return case_statement
  
# test selecting a REGEX grouping option
userSelection = input("""Please select how you want to group your case statement:\n => Select 1 to supply URLs and create content groupings.\n => Select 2 to supply URL syntax or subfolders to create content groupings.\n""")
if int(userSelection) == 1:
  print("You chose regexBasedGrouping")
  regexGroup = regexBasedGrouping()
  case_statement = generate_case_statement(regexGroup)
  print(case_statement)
elif int(userSelection) == 2:
  print("You choose syntaxBasedGrouping")
  syntaxGroup = syntaxBasedGrouping()
  case_statement = generate_case_statement(syntaxGroup)
  print(case_statement)
else:
  print("You choose an option that isn't available!\n Please start over!")
