# standards #

Project and python specific standards that have been chosen and not otherwise
explicitly recommended.

## project layout ##

See: [django-practices](https://github.com/lakesite/django-practices/) for 
reference.  

## best practices ##

See: [django-practices](https://github.com/lakesite/django-practices/) for 
reference.  

## dependencies ##

Where possible, minimize the number of package dependencies used to get the job
done.  If it's a complex task and someone else has an appropriately licensed
solution which is carefully maintained and largely established, then it's
a good idea.  

Dependencies that are used:

  1. [django-emailuser](https://github.com/lakesite/django-emailuser) which
     provides our custom User model.

## SOLID KISS ##

Use [SOLID](https://en.wikipedia.org/wiki/SOLID) design principles and [keep it stupid simple](https://en.wikipedia.org/wiki/KISS_principle).

## 12Factor ##

Generally heroku's [The Twelve-Factor App](https://12factor.net/) guide should
be followed.
