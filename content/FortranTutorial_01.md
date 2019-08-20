Title: Fortran Tutorial 1
Date: 2019-08-20 14:30
Category: Post

This is a Fortran tutorial.

Fortran example:
```fortran
PROGRAM myprog
  IMPLICIT NONE
  CALL mysub(5.d0, 4.1d0)
END PROGRAM

SUBROUTINE mysub(x,y)
  IMPLICIT NONE
  REAL(8) :: x, y
  WRITE(*,*) 'x + y = ', x + y
END SUBROUTINE
```