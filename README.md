# BREACH

*NOTE*: This repository is not maintained anymore. The project has evolved in the [Rupture tool](https://github.com/decrypto-org/rupture), so make sure to check this out if you are interested in the research on the BREACH attack.

## Description

Tools to execute [BREACH](http://breachattack.com) attacks.

| Script | Description |
|---|---|
| breach.py | The main script that starts the attack. |
| connect.py | MitM proxy that sniffs TLS Packets, defragments TLS records and dumps header and payload. |
| parse.py | Script that parses the lengths sniffed over the network and decides how the attack should continue. |
| hillclimbing.py | Script that creates the parameters needed by evil.js. |
| iolibrary.py | Library with useful function for I/O communication with the user. |
| sniff.py | Network sniffer that provides Ethernet level (and above) packet information. |
| index.html | Minimal HTML page that contains the evil js. |
| evil.js | Javascript that parses parameters needed from a file created by hillclimbing.py (and is in the same directory as evil.js and index.html) and issues requests on the endpoint. |
| config.yml | YAML configuration file. |

## Disclaimer

The above code was created for the needs of my thesis at the [School of Electrical and Computer Engineering](http://www.ece.ntua.gr/) of the National Technical University of Athens. Please do not use for malicious purposes!

## License

The content of this project is licensed under the [Creative Commons Attribution 4.0 license](http://creativecommons.org/licenses/by/4.0/) and the source code is licensed under the [MIT license](http://opensource.org/licenses/mit-license.php).
