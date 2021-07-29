# MyGHub

GitHub API wrapper

## Table of contents

- [MyGHub](#myghub)
  - [Table of contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Client](#client)
    - [Server](#server)

## Installation

1. Download this package from [release page](https://github.com/HwDhyeon/myghub/releases)
2. Install package with pip

    ```bash
    pip install <.whl file name>
    ```

## Usage

1. Set Environment variable with `.env` or OS setting

    ```ini
    GH_TOKEN=your_github_token
    ```

### Client

1. Call MyGHub CLI

    ```bash
    $ myghub get issues owner/repository closed '2020-01-01 00:00:00' '2020-12-31 23:59:59'

    {
        counts: 365
        issues: [
            {issue},
            {issue},
            {issue},
            {issue},
            {issue}
        ]
    }
    ```

### Server

1. Run MyGHub Server

    ```bash
    $ uvicorn myghub.server.server:app --port 8000 --host 0.0.0.0 --reload

    INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [6] using watchgod
    INFO:     Started server process [8]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    ```

2. Send HTTP Requst for MyGHub Server

    ```bash
    curl -i --location \
    --header "Content-Type: application/json" \
    --request POST \
    --data '{"repository": "mobigen/IRIS", "search_started_at": "2021-01-01 00:00:00","search_finished_at": "2021-01-31 23:59:59", "state": "all"}' \
    http://SERVER/issues/
    ```
