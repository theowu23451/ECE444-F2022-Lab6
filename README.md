## ECE444 Lab 6: Test Driven Development (TDD)
Repository created by Theodore Wu

This repository follows the examples from the Flaskr TDD tutorial at https://github.com/mjhea0/flaskr-tdd.

### Group Project Test Cases
On my group's Education Highways project, I wrote the suite of unit test functions given at the following URL:

https://github.com/ECE444-2022Fall/project-1-web-application-design-education-pathways-group-15-runtime-terror/blob/epic2-expanded-course-details/Education_Pathways/tests/test_app.py#L10-L72

The tests also contain a reusable pytest fixture for creating a test application client and setting up a test database. Helper methods are given for running GET and POST requests on the backend resource which queries the reviews database.

### Pros and Cons of TDD
Test-Driven Development (TDD) is a software development workflow that emphasizes the creation of tests as part of the development lifecycle. Rather than wait for code to be developed first before writing tests, TDD reverses this process by requiring the creation of tests before any code is written. 

This methodology has various benefits. First, the emphasis on creating tests makes code easier to maintain and refactor. Since the testing process can be automated, having a good suite of unit tests makes sure that unexpected behaviour does not occur when code is modified. Further, TDD also leads to modular code, as bulky code becomes difficult to unit test. This forces good architectural design by consequence. Finally, TDD improves code design quality since the developer is forced to consider all the edge cases that could occur prior to developing their code. This primes the developer for dealing with these cases as they are writing their modules.

However, TDD has a few drawbacks as well. The key drawback is that maintaining up-to-date tests is difficult. When an interface changes significantly or a large part of the code is rearchitected, unit tests can go out of date and must therefore be updated to the new interface, which may not be trivial task. Further, TDD can slow down the initial phases of development, which may be limiting when experimenting with different ideas at the start of a project. Finally, a system may have many dependencies that must be mocked for a unit test. When the system is complex, mocking these dependencies can be quite difficult and time-consuming, posing a barrier for less experienced developers.