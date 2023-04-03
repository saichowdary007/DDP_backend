## DDP_backend

Django application for the DDP platform's management backend. Exposes API endpoints for the management frontend to communicate with, for the purposes of

-   Onboarding an NGO client
-   Adding users from the client-organization
-   Creating a client's workspace in our Airbyte installation
-   Configuring that workspace i.e. setting up sources, destinations and connections
-   Configuring data ingest jobs in our Prefect setup
-   Connecting to the client's dbt GitHub repository
-   Configuring dbt run jobs in our Prefect setup

## Development conventions

### Api end points naming

-   REST conventions are being followed.
-   CRUD end points for a User resource would look like:
    -   GET <mark>/api/users/</mark>
    -   GET <mark>/api/users/user_id</mark>
    -   POST <mark>/api/users/</mark>
    -   PUT <mark>/api/users/:user_id</mark>
    -   DELETE <mark>/api/users/:user_id</mark>
-   Route parameteres should be named in snake_case as shown above.

### Api handlers / controller functions naming

-   Handlers would be named in <mark>lowerCamelCase</mark> fashion where the lower case word would represent the api end point followed by the resource/feature/functionality that the api is implementing. Plural name should be used depending on the api.
    -   Eg handler for an api to create User would look like
        <mark>postUser</mark>
    -   Eg handler for an api to create OrganizationClient would look like
        <mark>postOrganizationClient</mark>
    -   Eg handler for an api to fetch all Users would look like
        <mark>getUsers</mark>
    -   Eg handler for a login api would look like <mark>postLogin</mark>

### Variables and Classes naming

-   Variable names should follow snake_case convention. Eg org_user_id, user_id etc. Names like targettype, targetschema etc. are unacceptable.

-   Classes Name for models, services, middlewares should follow CamelCase Format. For eg OrgUserSchema, OrgPrefectBlock etc.

-   Make sure the names are meaningful. Avoid using variable names like 'x' , 'a' etc.

### Folder and file naming

-   Files that have models, services, custom modules, utils, controllers should be named using CamelCasing. For eg AdminController.py, AirbyteService.py, DdpLogger.py etc.

-   Other Files than above should be named using small case letters (snake_case should be used if it improves the readability).

-   All folders are named using small case letters (snake_case should be used if it improves the readability).

## Setup instructions

-   `pip install -r requirements.txt`

-   create .env from .env.template
