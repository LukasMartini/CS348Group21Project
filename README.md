# CS348-Group21

Figma link (design will be updated for each milestone): 

https://www.figma.com/design/2SqR3fiXOo7O1gCOu5KLK7/poker-replay?node-id=0-1&t=ln2VSweIvejDPM7F-1

## Setup Instructions for the CS348 Database

This document outlines the steps required to create and configure the `cs348` database locally. These steps assume that PostgreSQL is installed on your machine.

### Prerequisites

- PostgreSQL installed on your local machine.
- Should be in the `backend` directory.

### Step 1: Log into PostgreSQL

Open your terminal and connect to the default PostgreSQL user (typically `postgres`). Run the following command:

```bash
psql postgres
```

### Step 2: Create the Database

Run the following command to create the `cs348` database:

```sql
CREATE DATABASE cs348;
```

### Step 3: Switch to the New Database

Once the database is created, connect to it using the following command:

```sql
\c cs348
```

### Step 4: Create a User

Create a new user called admin and set a password. This user will be used to manage the database:

```sql
CREATE USER admin WITH PASSWORD 'admin123';
```

### Step 5: Grant Privileges

Grant all privileges on the database to the admin user to allow full control over the database:

```sql
GRANT ALL PRIVILEGES ON DATABASE cs348 TO admin;
```

### Step 6: Exit psql

Exit the PostgreSQL command line interface:

```sql
\q
```

### Step 7: Verify the Database

You can verify that the database was created successfully by connecting to it using the `admin` user:

```bash
psql -d cs348 -U admin
```

### Step 8: Load the Schema

Run the following command to load the schema into the database:

```bash
psql -d cs348 -U admin -f sql/create_tables.sql
```

## Setup for bash scripts (Not required)

This adds some convenience functions to your shell. If you don't want to use them, you can skip this step.

To run these the cs348 db must be setup.

Edit your shell profile (~/.bashrc for Bash, ~/.zshrc for Zsh):

```bash
export POKER_REPLAY_ROOT=$HOME:/path/to/poker-replay
```

Then add the following to the end of the file:

```bash
source $POKER_REPLAY_ROOT/shell_commands.sh
```

Then source the profile:

```bash
source ~/.zshrc
```

Usage:

- Drop Tables: `drop_tables`
- Create Tables: `create_tables`
- Load Data: `load_data`
