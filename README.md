```
             _____          _
            |  __ \        | |
 _ __  _   _| |__) |__  ___| | __
| '_ \| | | |  ___/ _ \/ _ \ |/ /
| |_) | |_| | |  |  __/  __/   <
| .__/ \__, |_|   \___|\___|_|\_\   v0.0.1
| |     __/ |
|_|    |___/
```


### What is it?

pyPeek is a simple script that allows you to 'peek' at the destination a URL will forward you to, without having to load that page in your web browser.  The result is printed to your terminal in an easy-to-read format.  Optionally, you can batch-process a list of shortened URLs from a text file, which will then save the results into output file.

### Why would I want to do this?
You never really know where an unshortened URL is going to send you.  Maybe you're at work, and the destination is someplace that isn't work-safe.  Maybe it will forward you to a malicious URL that would run abusive javascripts. Who knows?  pyPeek knows, and will not execute javascript or render any HTML. 

All this script will do, is visit the link and return the final destiantion to you, right in your terminal.

This was made mostly just to handle many http://x.co shortened links for assisting with dealing with abuse at GoDaddy, but it works with many other shorteners too.  It does *not* work with all shortening services, especially those that make you wait a few seconds (or click a confirm button to continue).


### How do I use it?

There are two ways to use this script.

You can supply the script with a single URL, like so:

##### Syntax:

```
python peek.py url
```

##### Example

```
python peek.py https://tinyurl.com/qalokft
----------------------------------------------------------------------------------------------------
https://tinyurl.com/qalokft <-- forwards to --> https://www.google.com/herp/derp/ka-flerp/
----------------------------------------------------------------------------------------------------
```

Or you can supply the script with a text file full of shortened URLs, like so:

##### Syntax:
```
python peek.py /path/to/urls.txt /path/to/output.txt
```

##### Example:
```
python peek.py /Users/x/Desktop/urls.txt /Users/x/Desktop/output.txt
Beginning batch processing of shortened URLs:
----------------------------------------------------------------------------------------------------
http://t.co/36Fz2f2vHw <-- forwards to --> https://twitter.com/bbcinternetblog/status/637213059950452736/photo/1
https://tinyurl.com/7i7r <-- forwards to --> http://www.amazon.com/
https://goo.gl/XsL62S <-- forwards to --> https://www.apple.com/
... etc
----------------------------------------------------------------------------------------------------
Unshortened links can be found here: /Users/x/Desktop/output.txt
```

If an output file is not specified for batch processing, by default the unshortened URLs will be saved into a file called "output.txt" in the same directory as peek.py.

It's as simple as that!
