# Validation Log Converter

These scripts may be helpful if you decide to convert your own logs into the format that can be used for translation. Here, we provide the scripts that we used to convert our validation logs. Script `./netsparker.py` was used to produce V<sub>A</sub>; script `./acunetix.py` -- to produce V<sub>B</sub>, and script `./elastic.py` -- to produce V<sub>C</sub>.

Requires Python 3. To install required packages run
```
pip install -r requirements.txt
```
To test this code, enter the directory in your favourite terminal application and enter:
```
python my_script.py -i input_raw_log_name -o output_transformed_log_name
```
Note that `my_script.py` is one of the scripts discussed above.
