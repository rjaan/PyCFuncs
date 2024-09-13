"""
Define the C-variables and functions from the C-files that are needed in Python
"""
import sys, random,string 
from ctypes import c_int, CDLL, create_string_buffer

class CStrToIntException(Exception):
    pass

class CStrToInt(CDLL):
      """
      Defines the C-variables and functions from the C-files that 
      are needed in Python
      """
      def __init__(self, prefix, cfuncname ) :
          try: 
              basic_function_lib = CDLL(
                                        '%s_%s.so' % (prefix,sys.platform)
                                       )
              self.cfunc = eval( f'basic_function_lib.{cfuncname}')
          except:
              raise CStrToIntException('OS %s or %s not recognized' % (sys.platform, cfuncname))
        
      def __call__ (cls, s , restype)->int:
          cls.cfunc.restype = restype
          return cls.cfunc(
                            create_string_buffer(s.encode('ascii'))
                          )      

if __name__ == '__main__' :
   try:
      integers  = []
      cintegers = [   
                   ''.join(random.choices(string.digits, k=N)) for N in range(0,9)
                  ]
      strtoint = CStrToInt('cfuncs/basic_function', 'str_to_integer' )
      for s in cintegers : 
          integers.append( strtoint(s,c_int) )     
      print( cintegers  , '=>', integers  )
   except CStrToIntException as e:
          print ( e.message ) 
