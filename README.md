### GEMFINDER AUTO VOTED

Autovote for the gemfinder.cc with a free recaptcha bypass that uses speech to text, and this script doesnt support proxies, for that `u can add ur own code to be able to use proxies` like api or other things, cuz this is only for example learn educational purposes.

### Base

- Selenium GeckoDriver Firefox
adjust the web driver path that ur system uses for selenium, located in the file `vote_management/web_driver_setup.py`

```python
geckodriver_path = "/bin/geckodriver"
```

- Target votes
u can change the target gemfinder coin link in the `target.py` section

```python
def get_target_url():
    return 'https://gemfinder.cc/gem/17296'
```

### Error iframe

If u find an iframe error in the results, like 

```python
Unable to locate element: //iframe[@title="reCAPTCHA"]
```

That u have voted with that IP Address, so the iframe recaptcha is no longer there, the solution is to use a proxy (u can add your own codes for this proxy)

### License

[MIT License](https://github.com/naix0x/upvote-gemfinder/blob/main/LICENSE).

