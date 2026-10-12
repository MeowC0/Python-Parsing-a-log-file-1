# Apache Log Analyser

A Python program that helps a web server administrator check an Apache logfile. 
You choose what to look at from a simple menu.

## What it does

The program shows a menu in the terminal. From there you can ask about:

- **Successful requests**: how many requests worked (Code 200), how many came
  from Seneca, and how many were for OPS435_Lab
- **Failed requests**: how many pages were "Not Found" (Code 404), how many of
  those contained "hidebots", and which IP addresses caused them

Right now, each choice just prints "Not implemented yet".

## How to run it

You need Python 3. In the terminal, type the script name followed by one or more log files:

```
./check_apache_log_ckhna.py wiki-access_log
```

To use many files at once, use `*`:

```
./check_apache_log_ckhna.py wiki-access_log*
```

Add `-d` (or `--default`) before the file names to skip the menu. The program
loads the files and shows the total number of successful requests (Code 200):

```
./check_apache_log_ckhna.py -d wiki-access_log
```

## What happens if I type it wrong?

| What you type | Result |
|---|---|
| Nothing after the script name | Shows an error and stops |
| `-d` with no file names | Shows an error and stops |
| `-d` and file names | Loads the files, shows the Code 200 report, stops |
| File names only | Loads the files, shows the main menu |

## Example

```
$ ./check_apache_log_ckhna.py wiki-access_log
Loading wiki-access_log
Apache Log Analyser - Main Menu
===============================
1) Successful Requests
2) Failed Requests
q) Quit
What would you like to do?
```

## Using the menus

- Type the number of the option you want and press Enter.
- Type `q` to go back to the previous menu. In the main menu, `q` quits.
- If you type something that is not on the menu, the program asks you to try
  again.