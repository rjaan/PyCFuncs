# tmdiff module module allows to obtain a time delta 
# since TimeDiff's instance initializing   
 

import datetime

__all__ = [ 'TimeDiff', ]

"""
 return the current local date and time.
"""
_now = lambda : datetime.datetime.now(tz=None)  

class TimeDiff(object):
      """
      allows to obtain a time delta since start of the class instance  
      initializing 
      """
      _now = lambda : datetime.datetime.now(tz=None)
      _prevtm = _now()

      def __call__(cls):
          return cls.tmdiff
               
      @classmethod
      def _get(cls):
          """
          returns a delta time  
          """
          return _now() - cls._prevtm

      @property
      def tmdiff(self):
          """
          returns a delta time
          """
          return self._get() 

