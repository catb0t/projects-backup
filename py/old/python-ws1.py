#begin default_header
import head #best practice: google for "why from package import * in python is bad"
from head import * #ONLY because globvars don't (i think) get imported natively with "import <...>"! DO! NOT! EVER! call functions from outside this file imported with "from <...> import *" as "function(args)", ALWAYS as "pkg.function(args)"!
head.header()
time.sleep(1)
#end

def q1():
    '''1. Operators & Expressions.  
      a. Add, subtract, multiply, and divide numerical values.
      b. Square a number, and square root a number by raising it to the (½) power.
      c. Use the floor division (//) and modulo (%) operators.  
      d. # How do floor division and modulo work?
      e. Use parentheses to group operations.
      f. # What is PEMDAS?  Why is it important in programming?'''
    p('')
    p('The sum of 2 and two is:', 2 + two) #in head.__all__, two was defined as int(3) thus 2+2 = 5
    p('because: {} plus {} is 5.'.format(2,two))# the magic is revealed.
    p('\nDid I trick you? Hopefully. (Have a look at head.py for an explanation.)')
    p('')
    p('''The sum of the squares of the sides of the right triangle is equal to the square of the hypotenuse.
    {}^2 is equal to {} and the square root of {} is {}...
    {} floor-divided by {} is {}, and {} goes into {} {} times remainder {}.
      '''.format(8,8**2,\
                 2,2**.5,\
                 16,3.2,16//3.2,  3,10,3,3%10\
                 ))
    #floor division rounds down rather than return a decimal; modulo returns the remainder
    #(P)arentheses, (E)xponents, (M)ultiplication+(D)ivision, (A)ddition+(S)ubtraction ::: where + implies priorities are equal
    #They matter because 2*3-1 is undecipherable because without rules, a start point is not defined.

def q2():
    '''2. Data types:
    a. # What is the difference between an int and a float?
    b. # What is a character?  What is a string?
    c. # What is the difference between 5 and "5"'''
    #In Mathematics class, an (int)eger is any whole absolute value. x=5 is an integer; negative(x) is not.
#However in computing, to make things easier, an integer is any whole number. Both x and x-(x*2) [[can also be written as x=0-x]] are integers
#A character is any singular visual symbol intended for human interpretation: in ASCII a character is any value between 0 ({}) and 127 ({}) or 255 ({}) in ASCII Extended. A string is any literal collection of characters: 5 is an integer while '5' is implicitly a string.

    p('no-op')

def q3():
    '''3. String operations:
    a. What happens when you add two strings?
    b. What happens when you multiply a string by an integer?  
    c. # try out some other operations using strings.  comment on the results.'''
    x = 'string 1'
    y = 'and '
    z = 'string 2'
    p(x + ", ", y, z)
    p('a string multiplied by an integer results in that many repeats of the string: that is a base construct to how the beautiful header is composed at runtime. \nexample: {}'.format(y*random.randint(0,1000)))
    #print (w or p) adds spaces between its args, and string.format is cool.    
def q4():
    '''4. Variables, expressions, statements:
    a. Initialize three variables:  one each of type int, float, and string.
    b. Modify the value(s) of one or more of the variables.
    c. Increase the value of the integer variable by 1 without assigning it's new value directly.
    d. # What is the purpose of a variable in programming?
    e. # What is the difference between an expression and a statement?'''
    x = int(5)
    y = float(8.7)
    z = str('not a val')
    x += y
    y /= 2
    p(x + 1)
    p(x,'is still',x)
    #the variable makes so many things possible, in that you now have a representative object: its purposes are many 
    #a statement contains some explicit instructions or function call; an expression is merely math or operations of the like
    
def q5():
    '''5. Print statements. 
    a. Use the print function to print a string to the interpreter.
    b. Use the print function with multiple parameters to print multiple values on one line.
    c. Print the value of one or more variables.'''
    p('i\'m a string')
    p('i bound q to', q, 'and w and p to', w)
    p('{}{}{}'.format(q, w, p))
    

def q6():
    '''6. Input:
    a. Use the input function to get a string from the user, and then print its value.
    b. # why does input need to be on the right-hand side of a variable assignment?
    c. Use the input function with a string parameter to display a prompt to the user.'''
    r(q('type something $ '))
    r(q('type something $ '))
    b64ec(q('type something $ '))
    b64ec(q('type something $ '))
    b64ec(q('type something $ '))
    r(q('type something $ '))
    #because doing so otherwise creates a misuse of the definition operator: it doesn't make any sense for the input to be a var

def q7():
    '''7. Type-checking
    a. Print the value of the expression: type( 5 )
    b. Print the value of the expression: type( 'asdf' )
    c. Print the value of the expression: type( '5' )
    d. # What is the purpose of the type function?'''
    p('the typeof int(5) is {}'.format(type(5)))
    p('the typeof str(asdf) is {}'.format(type('asdf')))
    p('the typeof str(5) is {}'.format(type('5')))
    #typechecking.    
def q8():
    '''8. Type-casting
    a. Assign a variable x to the value of: int( '5' )
    b. Assign a variable y to the value of: float( '5' )
    c. Assign a variable z to the value of: str( 5 )
    d. # What are the purposes of the int, float, and string functions?'''
    x = int('5')
    y = float('5')
    z = str(5)
    #to explicitly define types.
def q9():
    '''Questions
    9. Procedures:
    a. Define a procedure that initializes a variable, and then prints its value.
    b. Call the procedure multiple times.
    c. # What happens if you define a procedure but never call it?
    d. # What is the purpose of a procedure?
    '''
    def m():
        x = random.randint(-123456789,123456789)
        p(x)
    for i in range(0,random.randint(-127,127)):
        m()
    #it never gets run or compiled: it will be scanned for improper formatting but will not be evaluated till it gets called. it does not occupy memory.
    #to concatenate operations, to make them more easily callable, so you needn't retype stuff, etc
    
def q10():
    '''10. Composition:
    a. Prompt the user to input their name, then print "Hello <name>!"   (replacing <name> with the user input.)
    b. Prompt the user to input a time of day (24 hr. format), and an amount of hours, then print the time after that many hours have elapsed.  For example:  
    time: 14 
    hours: 14 
    new time: 4
    get tod in hr
    get hours to add
    print wrap hours + tod
    '''
    def rettod():
        try:
            x=int(q('TOD as nearest of 24 hours: '))
            y=int(q('hours to add: '))
            if x + y > 24:
                w((x+y)%24)
            else: w(x+y)
        except ValueError:pass
    def getname(evil=None):
        p('part a:')
        x=q('en\670er y\700ur nam\777e (\420on\271 \168 \280 "t inc\501ude \300\320y ??funn\277 \756char&e0;cter\333): ')
        if evil:eval(x)
        else:p(x)
    try:
        getname(1)
    except:
        getname()
    finally:
        rettod()
        rettod()
        
def main():
    ret = '\n' + e2r('ragre sbe arkg dhrfgvba')
    x=q(ret)
    if x is "":q1()
    x=q(ret)
    if x is "":q2()
    x=q(ret)
    if x is "":q3()
    x=q(ret)
    if x is "":q4()
    x=q(ret)
    if x is "":q5()
    x=q(ret)
    if x is "":q6()
    x=q(ret)
    if x is "":q7()
    x=q(ret)
    if x is "":q8()
    x=q(ret)
    if x is "":q9()
    x=q(ret)
    if x is "":q10()

    head.header()
    s(1)
    repl()
main()
        
