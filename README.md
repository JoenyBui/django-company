# README #

This project is a django application to model a company/employee relationship given a list of privilege and application rights.  The model for the company is that the user won't have access to anything that the company doesn't have access too.

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### Branch ###
* master
main branch where the source code of HEAD always reflect a production-ready state

* develop
main branch where the source code of HEAD always reflects a state where the latest development changes for the next release

* feature branches
used to develop new features for the upcoming or a distant future release
** May branch off from: 
develop
** Must merge back into:
develop
** Branch naming convention:
anything except master, develop, release-*, or hotfix-*

* Release branches
support preparation of a new production release
** May branch off from:
develop
** Must merge back into:
develop and master
** Branch naming convention:
release-*

* Hotfix
much like release branches in that they are also meant to prepare for a new production
** May branch off from:
master
** Must merge back into:
develop and master
** Branching naming convention:
hotfix-*


### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact