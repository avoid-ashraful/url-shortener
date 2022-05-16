
# URL SHORTENER

#### Project Run Instructions:
* Open Terminal
* Go to project directory
* Type `docker-compose -f local.yml up --build` for development. Append the args `-d` to have the docker build and run the project in the background
* Frontend app will be available `http://localhost:8080/`
* Backend app will be available `http://localhost:8000/`

#### Accessing Project Shell
* Type `docker-compose -f local.yml exec <docker_compose_service_name> bash`. I.E: `docker-compose -f local.yml exec web bash`
* Pass the argument --user=root to access project shell as root user to install requirement dependencies. I.E: `docker-compose -f local.yml exec --user=root web bash`

#### Running Bakcned Test Suit
* Type `docker-compose -f local.yml exec web bash -c "cd backend && pytest"`

## Gtihub Action

* There are two actions are being performed here:

    * `flake8` : Cheking `coding style` and `linting` of the codebase.
    * `pytest` : Executing test suit with coverage.

* To view the actions, 
    * Go to : `https://github.com/avoid-ashraful/url-shortener/actions`
    * Click to the latest finished workflow.
    * Click to `build` to see all steps of the workflow.
    * To see the code coverage expand `Test with pytest and display coverage` this section.
