# PyCFuncs module makes c-functions integration easy
---
## How to achieve this?

So, you may to run  some c-functions by help of a dynamic library that it must be built and installed  in a certain system location ( usualy, it is any filesystem directory). 
  
While I'am learning of how to do automatic building of the module with 
GNU make, you need to manually compile the C file using either

    $ gcc -o funcs/basic_function_win32.so -shared -fPIC -O2 funcs/basic_function.c # Windows
    
    $ gcc -o funcs/basic_function_darwin.so -shared -fPIC -O2 funcs/basic_function.c # Mac
    
    $ gcc -o funcs/basic_function_linux.so -shared -fPIC -O2 funcs/basic_function.c # Linux
    

If all Ok, this created a new file ```basic_function_{paltform}.so``` to contain C-function in funcs/ folder  and you will able to run the module as describe below.  

## C-function integration is easy achiving trough  

CStrToInt class is inherited from ctypes.CDLL superclass and allows to define str_to_integer's function from the C-file prefix with cfuncs/basic_function name as show below :

    >>> from cstrtoint import CStrToInt,CStrToIntException,c_int
    >>> try:
    ...    strtoint = CStrToInt('cfuncs/basic_function', 'str_to_integer' )
    ...    integer  = strtoint("1234",c_int)
    ...    print( integer, type(integer).__name__ )
    ... except CStrToIntException as e:
    ...    print ( e )
    ... 

Right entered and executed code outs a result on python's console . The result to have be one of two kind representations are either a textual message or an integer number. If something goes wrong, textual message will contain a following  text about possible failures :   

     OS linux or str_to_integer not recognized  

PyCFuncs module was written with use of [Tutorial: Interfacing Python and C code](https://reptate.readthedocs.io/developers/python_c_interface.html)
