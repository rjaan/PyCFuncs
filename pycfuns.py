"""
Define the C-variables and functions from the C-files that are needed in Python
"""
import sys 
from ctypes import c_int, c_uint, CDLL, create_string_buffer

__all__ = [ 'CStrToIntException', 'CStrToInt', 'c_int' ]

class CBaseFuncException(Exception):
    pass

DLLibrary='cfuncs/basic_function_%s.so' % (sys.platform) 

class CBaseFunc(CDLL):
      """
      Defines the C-variables and functions from the C-files that 
      are needed in Python
      """
      def __init__(self, cfuncname, restype, dllib=DLLibrary ) :
          if not cfuncname:
               raise CBaseFuncException('Wrapped C-function not defined' ) 
          try: 
              super(CBaseFunc,self).__init__ ( dllib )
              self.cfunc = eval( f'self.{cfuncname}')
              self.cfunc.restype = restype
          except:
              raise CBaseFuncException('OS %s or %s not recognized' % (sys.platform, cfuncname))
        
class CStrToInt(CBaseFunc):
      """
      The wrapper of c-function str_to_integer 
      """
      def __init__(self):
             super(CStrToInt,self).__init__('str_to_integer',c_int)

      def __call__ (cls, s )->int: 
           return cls.cfunc(        
                         create_string_buffer(s.encode('ascii'))
                      )

class CUintPow(CBaseFunc):
      """
      The wrapper of c-function uint_pow
      """
      def __init__(self):
          super(CUintPow,self).__init__( 'uint_pow', c_uint )
  
      def __call__(cls,x,y) -> int:
         return cls.cfunc( x , y )

# the code will replace in python unit test.
if __name__ == '__main__' :
   import random, string, tmdiff 
   try:
      """
      Checking the possibility to use C-functions  from  
      in-built dinamic library of the module 
      """  
      tmdiff = tmdiff.TimeDiff()  
       
      integers  = []
      cintegers = [   
                   ''.join(random.choices(string.digits, k=N)) for N in range(0,8)
                  ]
      cintegers.append( "-123456" )
      cintegers.append( "+123456" )
      strtoint = CStrToInt()
      print( tmdiff() , 'Checking the possibility to use C-function by name \'strtoint\':'  ) 
      for s in cintegers : 
          n = strtoint( s )
          print( tmdiff(), "Input string: {:>8} ?= Output number: {:>8}". format(s,n) )

      # It is time to use Walrus's operator for pow() testing
      uintpow  = CUintPow() 
      print( tmdiff() , 'Checking the possibility to use C-function by name \'uintpow\':'  )
      for x in range(0, 11):
           y = random.randrange(10)      
           print ( tmdiff(),"raise {:>3} to the power of {:^8} : {:^10} ?= {:^10}".format(x,y,uintpow(x,y),x**y) )
           
   except CBaseFuncException as e:
          print ( e ) 
