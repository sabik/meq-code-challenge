# MEQ code challenge - Jiri Baum


## Running the program

HOST=192.0.2.1 PORT=1234 FNAME_BASE=fsm python main.py

No python dependencies are required to run the program. It expects the
graphviz `dot` command to be available on the path.

The output is two files, $FNAME_BASE.dot and $FNAME_BASE.png

Python version 3.12 or later.


## Implementation notes


### Core of solution

The core of the solution is in the Explorer class, which keeps track of the
FSM as discovered so far and decides on the next actions to take.


### Error handling

I have generally assumed the happy path; a real system would have a lot
more handling of errors and invalid situations.

In particular, no attempt is made to handle desynchronisation of the
protocol or unexpected responses from the server, other than logging and
discarding any unexpected characters. If the server does not respond as
expected, the program will likely hang.


### Configuration

Other than the server address and the destination filename base, all other
aspects are hard-coded. A real system would likely have the list of valid
actions in the FSM pulled in from a configuration file or from a separate
module.

I have left GraphViz with its default settings.


### Code style

Standard "black" python code style.


### Development dependencies

pytest, pycodestyle, pylint, mypy, black, isort


## Manifest

- README - this file

- main.py - main program

- client.py - communication with the server

- common.py - type definitions

- explorer.py - handles exploration of the FSM

- visualise.py - visualise the FSM using GraphViz

- test_explorer.py, test_visualise.py - tests for the corresponding modules

