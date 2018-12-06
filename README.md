# bgt1


## Intallation

This is tuned for a t2.micro AWS Linux AMI.

`curl https://raw.githubusercontent.com/jellybaab/bgt1/master/install/setup_bitgo_test | sh`


Now create your keyring password via:

```
keyring set bitgo api_key
<API KEY>
<KEYRING PASSWORD>
```

This will safely store your BitGo API key and also set the keyring passphrase at the same time.  You can verify what you stored via:

```
keyring get bitgo api_key
<KEYRING PASSWORD>
```


## Running

Change directory to the `utils` directory. The `btg` command will tell you what it can do by just typing `./btg`

