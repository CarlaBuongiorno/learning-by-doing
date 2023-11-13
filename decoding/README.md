Problem:
    We have url encoded text and want it in human readable format.
How to automate this.
 
1. We need to get the text to translate (input)
2. Read through the text to figure out what needs translating
3. translate only the relevant parts, check for % signs, include the next 2 characters. Compare them to a lookup table to know what character it should be replaced with.
4. write it down to return to who or what gave us the input.
 
Requirements:
1. Solves the problem as described in the procedure above (url-encoded text to human readable)
2. needs to be usable from the commandline
3. doesn't ask for input while running, gets the input as a command line argument
4. only prints out the output (human readable text)
 
 
Separate parts of the problem
 
step 1:
    get data into the program (commandline arguments)
step 2:
    replace the %-encoded text with their human readable counterpart
Step 3:
    outputting the data

useful python modules:
    argparse to parse command line arguments 
        reference document: https://docs.python.org/3/library/argparse.html
        tutorial: https://docs.python.org/3/howto/argparse.html#the-basics
    function to translate from url encoded text to human readable.
https://docs.python.org/3/library/urllib.parse.html#urllib.parse.unquote


program that decodes percentage encoded text now needs to be expanded with more encodings.
 
what other kinds of text do we decode:
    - jwt
    - base64
Define what the actions to solve the problem are:
    - Get the input (from command line only)
    - read the input and decode it.
    - Print the output
What do we need to do:
    getting input already exits
    figure out the action that we need to take.
        * add a parameter to define what action should be taken
        * code to select the right decoding function
    print the output
 
How to decode:
    * for decoding base64 use the https://docs.python.org/3.10/library/base64.html#base64.b64decode function
    * for decoding jwt tokens. Put the token into the variable called token:
        payload = token.split('.')[1]
        padded_payload = payload + ('=' * (-len(payload) % 4))
        print(base64.urlsafe_b64decode(padded_payload))