# LogThoseKeys

LogThoseKeys is a keylogger that can store the key presses of any number of
clients. `__main__.py` runs a Python `flask` server which listens for `POST`
requests from clients and writes the pressed key from the payload to a log file
along with the timestamp at which the key was pressed and the client IP
address, which are also both included in the payload. The client script, stored
in the `client/` directory, listens for key presses and sends a `POST` request
with the appropriate payload to the `flask` server every time any key is
pressed.

# Getting Started

## Download

To download LogThoseKeys, launch your Terminal (or Command Prompt on Windows)
and run the following:

```sh
$ git clone https://github.com/Python3-8/logthosekeys LogThoseKeys
...
$ python3 -m pip install -r LogThoseKeys/requirements.txt
...
```

This should download LogThoseKeys and install all its requirements, and you're
all set, that easily!


## Run

To run LogThoseKeys, navigate to the same folder where you cloned the
repository in your terminal and run the following command:

```sh
$ python3 LogThoseKeys
 * Serving Flask app '__main__' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://0.0.0.0:5000 (Press CTRL+C to quit)
```

This starts the `flask` server that listens for `POST` requests.

Now to run the client, open a new Terminal (or Command Prompt) window, and
navigate to the same directory. From here, run the following:

```sh
$ python3 LogThoseKeys/client
```

That's literally it! Now all your keystrokes will be captured and stored in a
file (that's in your current working directory) called `client-keylog.txt`.

# Customization

Now that you know how to run the program, let's talk about customization.
Getting your preferences into the program.

## Server Hosting Address

To change the address to host the `flask` server on, the
recommended way is to set an environment variable called `LTK_HOST_ADDR`. All
you have to do is set this environment variable to the address to host on, and
the program automatically hosts on it. You can also change the hosting port by
setting an environment variable called `LTK_HOST_PORT`.

An alternative way to achieve this is by manually editing the server program,
which will not be demonstrated here.

## Client Connection Address

If you're changing where the server is hosted, then of course you must change
the address the client connects to. Open `client/__main__.py` and find line 5
where you can change this:

```py
# TODO: Change this to match your requirements
SERVER_ADDR = 'http://0.0.0.0:5000/'
```

The client file is now ready to be distributed to a "victim" (whose consent you
must have in all cases).

## Log File

If you already have an important file named `client-keylog.txt` in the
directory where you cloned the repository, you might want to change the
location where key presses are stored. To do this, the recommended way, similar
to changing the server hosting address, is to set another environment variable
called `LTK_LOGFILE`. Set the value of this environment variable to the desired
log file path and you're all set! The program is now fully customized if you've
followed all these steps.

# Distrubution

If you're like me and you want to hack your mom, that's quite easy. All you
have to do is run the server, change the client file, run it on your victim's
computer, and voilà! First, run the server program on your computer. Next, edit
