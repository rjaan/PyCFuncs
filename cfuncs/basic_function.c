/* return the value of x to the power of y */
#define POW(x,y)({ \
     unsigned int __p = 1; \
     for ( int __n = 0 ; __n < y; __n++ )\
         __p *= x;\
     __p; })

/* check the text has all of decimal characters */
#define HAVETEXT_ALLDCHS(s,ns)({\
        int __r = 1; \
        for ( int __i = 0 ; __i < ns ; __i++ ) \
            if ( __i == 0 && *s == '-' ) __r = -1;  \
            else if ( ( *(s+__i) < 0x30 || *(s+__i) > 0x39) ) { \
               __r  = 0; break; }\
        __r ; }) 
 
#include <string.h>

/* convert a textual representaion to a decimal */
#define STRTODEC(s)({\
        int __n = 0, \
            __ns = strlen(s), \
            __sign = HAVETEXT_ALLDCHS(s, __ns); \
        if ( __sign ) { \
           if ( __sign == -1 ) { s++; __ns = strlen(s); };\
           for ( int __i = __ns ; __i > 0  ; __i-- ) \
             __n += POW(10,__ns - __i ) * (s[__i-1] - 0x30);\
        } \
        __n * (__sign) ; })

#include <stdlib.h>
/*
 * str_to_integer(s)
 * c-function takes s parameter to contain a textual represention 
 * of decimal number. Then it converts ihe string to decimal   
 * number by use STRTODEC macros and it returnes the obtained value. 
 */
int str_to_integer( char *s )
{
    return STRTODEC(s); 
}
/*
 * uint_pow(x,y) 
 *   it returns the value of x raised to the power of y 
 */
unsigned int uint_pow( unsigned char x, unsigned int y ) 
{
  return POW(x,y);
}
/* 
  For testing purposes 
 */
#ifdef __HAVE_MAIN__
#include <stdio.h> 
int main(void){
    const char *s = "1234";
    printf(" Convert string %s to integer: %d\n", s, STRTODEC(s) );
    return 0; 
}   
#endif /*__HAVE_MAIN__*/

