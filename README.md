
# Get Started with `textlog`

Simple Python Text Log

## Getting Started

- Use our step-by-step guide to get started with `textlog` in minutes.

### 1. Download Python

- Get started with Python to use everything in the `textlog`.

- [`Download Python`](https://www.python.org/downloads/)

### 2. Get the command line tool

```bash
pip install textlog
```

### 3. Use

- Command
  - add

    ```bash
    # Default
    python log.py add "FILE NAME" "CONTEXT"
    # Example
    python log.py add "dongs" "update >> 0.0.1 --> 0.0.2"
    ```

    ![Example01](./assets/Example01.png)

    ```bash
    # Option
    # -p : Write and print at same time.
    # -P : Specifies the path of the file.
    #   Example
    python log.py add -P "c:" log "(2019.10.20 20:23) process >> END" -p
    ```

    ![Example02](./assets/Example02.png)

  - help

    ```bash
    # Default and Example
    python help
    ```

    ![Example03](./assets/Example03.png)

- Python

  - log

    ```python
    file_name
    context
    path=None
    # Path where the file will be stored
    # default(None) : Interpreter execution location
    isPrint=False
    # with print
    ```

    - Example

        ```python
        import textlog
        textlog.log("dongs", "update >> 0.0.1 --> 0.0.2", path="c:/", isPrint=True)
        ```

        ![Example01](./assets/Example01.png)

## Log

- 0.0.1.1
  - add is_no_file option

- 0.0.1
  - create project
  - add command
    - add
      - add `-p`, `-P` Option
    - help

## Copyright

- Copyright (C) 2019 LEE DONG GUN. (gnyontu39@gmail.com) and contributors
