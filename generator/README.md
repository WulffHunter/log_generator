# Random Apache Log Generator
Requires Python 3 to run.

To install required packages run
```bash
pip install -r requirements.txt
```

To test this code, enter the directory in your favourite terminal application and enter:
```bash
python generator.py
```

To create a file of fake logs, specify the filename and use the `-l` argument to specify the number of lines to generate, like so:
```bash
python file.py logs.txt -l 200
```
Use the `-s` flag to create 2 files: a training set file and testing set file. Use the `-p` flag to control what percentage of the lines are used for training, e.g.:
```bash
python file.py logs.txt -l 100 -s -p 90
```
This will reserve 90% of the 100 lines for training, while the last 10% will be used for testing. It will also not repeat any template strings from the testing file into the training file (templates are unique between training and testing).

The fake log and its ground truth are separated by a tab (`\t`). Each log is on a newline.

## Hyperparameters

The various hyperparameters of the generator (e.g. the frequency of fields, the maximum length of fields, etc.) can be found and modified in the `parameters.py` file.

## Log Fields

### Currently Available Tool Fields

Currently, our Log Generator tool can generate the following fields:

| Field acronym | Field description |
|---------------|-------------------|
| `h`             | IP address of the client host. Can be IPv4 or IPv6. |
| `l`             | The remote logname. We were unable to find a good example of what kinds of values are returned by Apache servers, thus for this paper we only supplied the commonly-given value ‘-’. This field could not be omitted as it is present in both the ELF and CLF formats.  |
| `u`             | The remote username. Can be empty (`-`) |
| `t`             | The datetime of the request, presented in the default `day/month/year:hour:minute:second zone` format.  |
| `r`             | The request line from the client. Made up of the method, path and   querystring, and protocol. |
| `s`             | The status of the request. |
| `b`             | The number of bytes sent.   |
| `m`             | The request method.   |
| `U`             | The requested URI path.  |
| `H`             | The request protocol.  |
| `q`             | The request querystring.   |
| `v`             | The canonical servername of the server servicing the request.  |
| `V`             | The servername according to UseCanonical. In our generator, this field is identical to the `v`   field.   |
| `i`            | The user agent of the request\*. |
| `R`             | The referrer of the request\*. |   
| `_`             | Represents a separator between log fields. |
\* (**Note:** In a real Apache HTTP server deployment, this field is extracted from the `%i`  log parameter, see the section below for details.)

Adding additional fields can be done easily by adding the acronym and its generator into the `fields` struct in the `./generator.py` file.

### All Available Apache Fields

Below are all of the fields that an Apache server could possibly generate. Modified from [the Apache log manual](https://httpd.apache.org/docs/1.3/mod/mod_log_config.html#logformat]).

```
%...a:          Remote IP-address
%...A:          Local IP-address
%...B:          Bytes sent, excluding HTTP headers.
%...b:          Bytes sent, excluding HTTP headers. In CLF format
        i.e. a '-' rather than a 0 when no bytes are sent.
%...c:          Connection status when response was completed.
                'X' = connection aborted before the response completed.
                '+' = connection may be kept alive after the response is sent.
                '-' = connection will be closed after the response is sent.
%...{FOOBAR}e:  The contents of the environment variable FOOBAR
%...f:          Filename
%...h:          Remote host
%...H       The request protocol
%...{Foobar}i:  The contents of Foobar: header line(s) in the request
                sent to the server.
                
                (**Note**: in our generator tool, `i` reflects the
                User Agent field, which is a commonly-used subset of
                the real `%i` field.)

%...l:          Remote logname (from identd, if supplied)
%...m       The request method
%...{Foobar}n:  The contents of note "Foobar" from another module.
%...{Foobar}o:  The contents of Foobar: header line(s) in the reply.
%...p:          The canonical Port of the server serving the request
%...P:          The process ID of the child that serviced the request.
%...q       The query string (prepended with a ? if a query string exists,
        otherwise an empty string)
%...r:          First line of request
%...s:          Status.  For requests that got internally redirected, this is
                the status of the *original* request --- %...>s for the last.
%...t:          Time, in common log format time format (standard english format)
%...{format}t:  The time, in the form given by format, which should
                be in strftime(3) format. (potentially localized)
%...T:          The time taken to serve the request, in seconds.
%...u:          Remote user (from auth; may be bogus if return status (%s) is 401)
%...U:          The URL path requested, not including any query string.
%...v:          The canonical ServerName of the server serving the request.
%...V:          The server name according to the UseCanonicalName setting.
```

## Standard Log Formats

### CLF

CLF stands for Common Log Format. It appears as follows:

```
%h %l %u %t \"%r\" %>s %b
```

**In our tool**, the format appears as follows:

```
h_l_u_t_r_s_b
```

Which stands for:

- `%h`: Remote host (an IP address value).
- `%l`: Remote logname (unknown value type).
- `%u`: Remote user (a username type, e.g. `Frank` or `Jareds-Computer-3`).
- `%t`: Datetime of the request.
- `%r`: The first line of the request (appearing as `METHOD PATH PROTOCOL`, e.g. `GET /users/18411 HTTP/1.1`).
- `%b`: The number of bytes sent.

**Note:** For `%r`: It is also possible to log one or more parts of the request line independently. For example, the format string `%m %U%q %H` will log the method, path, query-string, and protocol, resulting in exactly the same output as `%r`.

### Combined Log Format / ELF

Another common log format is the Combined Log Format, which appears as follows:

```
%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-agent}i\"
```

**In our tool**, the format appears as follows:

```
h_l_u_t_r_s_b_"R"_"i"
```

In our paper, we refer to Combined Log Format as ELF to easily distinguish between the two log format's acronyms. However, in this codebase, ELF is always referred to as Combined Log Format.
