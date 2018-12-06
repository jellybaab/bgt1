#!/usr/bin/python3
#

import json
from pywallet import wallet


def create_hd():
    """From https://github.com/ranaroussi/pywallet"""
    # generate 12 word mnemonic seed
    seed = wallet.generate_mnemonic()

    # create bitcoin wallet
    w = wallet.create_wallet(network="BTC", seed=seed, children=1)
    print(w)
    print("xprv = " + w['xprivate_key'][4:])
    print("xpub = " + w['xpublic_key'][4:])
    return w


def add_keychain(url, headers, key)
    user_options = { "xpub": key['xpublic_key'][4:])
    


user_key = create_hd()
backup_key = create_hd()



"""
    // Create the user and backup key. Remember to back these up!!
    const userKey = bitgo.keychains().create();
    const backupKey = bitgo.keychains().create();

    // Add keychains to BitGo
    const options = {
      label: 'key1',
      xpub: userKey.xpub,
      encryptedXprv: bitgo.encrypt({ password: password, input: userKey.xprv })
    };
    bitgo.keychains().add(options, function(err, keychain) {
      if (err) {
        console.dir(err);
        throw new Error('Could not create the user keychain');
      }
      console.log('User keychain xPub: ' + userKey.xpub);

      const options = {
        label: 'key2',
        xpub: backupKey.xpub
      };
      bitgo.keychains().add(options, function(err, keychain) {
        if (err) {
          console.dir(err);
          throw new Error('Could not create the backup keychain');
        }
        console.log('Backup keychain xPub: ' + backupKey.xpub);

        // Now tell BitGo to create their server side key
        bitgo.keychains().createBitGo({}, function(err, keychain) {
          if (err) {
            throw new Error('Could not create 3rd keychain on BitGo');
          }
          console.log('BitGo service keychain xPub: ' + keychain.xpub);

          const options = {
            label: label,
            m: 2,
            n: 3,
            keychains: [
              { xpub: userKey.xpub },
              { xpub: backupKey.xpub },
              { xpub: keychain.xpub }]
          };
          bitgo.wallets().add(options, function(err, result) {
            if (err) {
              console.dir(err);
              throw new Error('Could not add wallet on BitGo');
            }
            console.log('Wallet Created!');
            console.dir(result.wallet);
            console.log('\n\nBACK THIS UP: ');
            console.log('User keychain encrypted xPrv - WRITE IT DOWN: ' + bitgo.encrypt({ password: password, input: userKey.xprv }));
            console.log('Backup keychain encrypted xPrv - WRITE IT DOWN: ' + bitgo.encrypt({ password: password, input: userKey.xprv }));
          });
        });
      });
    });
"""
