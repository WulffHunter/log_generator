# Apache Log Translator

This repository contains tools used for generating synthetic Apache logs and the tools needed to parse reference empirical logs, see [paper](TBD) "On Automatic Parsing of Log Records" for details. 

## Apache Fake Log Generator

For the Apache Fake Log Generator tool, please see the `./generator/` folder. A complete description of how to use the tool in the `./generator/README.md` file.

## Real Log Converter

For the tool used to parse real logs V<sub>A</sub>, V<sub>B</sub>, and V<sub>C</sub> , and convert them into a format ingestible by a machine learning model, please see the `./real_log_cleaner` folder. The origins of the logs are as follows: [V<sub>A</sub>](https://github.com/ocatak/apache-http-logs/blob/b7713f88368443501a296a6adda06475d491d6fb/netsparker.txt), [V<sub>B</sub>](https://github.com/ocatak/apache-http-logs/blob/b7713f88368443501a296a6adda06475d491d6fb/acunetix.txt), and [V<sub>C</sub>](https://github.com/elastic/examples/blob/bc53b584c0f9f574d4373193334bf03541a54936/Common%20Data%20Formats/apache_logs/apache_logs). Additional details are given in `./real_log_cleaner/README.md` file.

## Sample Logs Used

To view all of the sample log files used (including the three real log files, as well as the five generated log files mentioned in the paper), please visit the [data repository](https://doi.org/10.5281/zenodo.4536514).

## License

This project is licensed under the MIT License.

## Contact Us

If you have found a bug or came up with a new feature -- please open an [issue](https://github.com/WulffHunter/log_generator/issues) or [pull request](https://github.com/WulffHunter/log_generator/pulls).

## Acknowledgments

This work was supported and funded by Ryerson University and Natural Sciences and Engineering Research Council of Canada.
