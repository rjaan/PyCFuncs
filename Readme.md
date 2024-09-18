# PyCFuncs module makes c-functions integration easy
---
## The C-code wrapping and how to achieve it

So,	 you can perform some c-functions by help of a dynamic linked library that it must be built and installed  in a certain system location ( usualy, it is module's directory). 
  
While I'am learning of how to do automatic building of the module with 
GNU make, you need to manually compile the C file using either

    $ gcc -o funcs/basic_function_win32.so -shared -fPIC -O2 funcs/basic_function.c # Windows
    
    $ gcc -o funcs/basic_function_darwin.so -shared -fPIC -O2 funcs/basic_function.c # Mac
    
    $ gcc -o funcs/basic_function_linux.so -shared -fPIC -O2 funcs/basic_function.c # Linux
    

If all Ok, it will be created DLL's file is named  ```basic_function_{paltform}.so```. The file  will be  located in funcs/ folder that itself is located a root of the repository. Then, you will able to run с-functions of the DLL with use pycfunc module as describe below. 

But you should rember that  you must remain into the root of the repository. So I recommend  you to do a clone  of the repository and go to its directory.

    $ git clone https://github.com/rjaan/PyCfuncs.git \
    && cd PyCfuncs 
   

## C-function integration is easy achiving trough  

CBaseFunc class is inherited from ctypes.CDLL superclass and allows to wrap some c-functions from certain dynamic linked library.  CBaseFunc class itself  can play superclass' role and derive new subclasses such as  CStrToInt and CUintPow classes. Those classes are an example and nothing more. Because they have got more efficient analogs to base on using of built-in functions and operators in Python 

**CStrToInt class**  

CStrToInt class is inherited from CBaseFunc superclass and allows to call ```str_to_integer``` function from ```cfuncs/basic_function_{paltform}.so``` shared library as show below :

    >>> from pycfuns import CStrToInt,CBaseFuncException
    >>> try:
    ...    strtoint = CStrToInt()
    ...    positive  = strtoint("1234")
    ...    print( positive, type(positive).__name__ )
    ...    negative  = strtoint("-1234")
    ...    print( negative, type(negative).__name__ )   
    ... except CBaseFuncException as e:
    ...    print ( e )
    ... 
    1234 int
    -1234 int
 

**CUintPow class**

CStrToInt class is inherited from CBaseFunc superclass and allows to call ```uint_pow``` function as show below :

    >>> from pycfuns import CUintPow
    >>> try: 
    ...     uintpow = CUintPow()
    ...     x=2
    ...     y=4 
    ...     print( f'x={x}', f'y={y} =>', uintpow(x,y) )
    ... except CBaseFuncException as e:
    ...     print(e)
    ... 
    x=2 y=4 => 16


**Exception handling** 

Right entered and executed code outs a result on python's console . The result to have be one of two kind representations are either a textual message or an integer number. If something goes wrong, textual message will contain a following  text about possible failures :   

     OS linux or str_to_integer not recognized  

The message raised by help CBaseFuncException will necessarily contain C-function name.

PyCFuncs module was written with use of [Tutorial: Interfacing Python and C code](https://reptate.readthedocs.io/developers/python_c_interface.html)
				