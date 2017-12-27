pyTPLinkRouter
==============

pyTPLinkRouter provides an easy to use Python API to control your TPLink router.

The only function currently supported is to retrieve the list of devices connected to the router.
The strength of the library is to detect the authentication method supported by the user's TPLink router model.

The code was developed by Home Assistant developers as a TPLink device tracker platform, and was taken out of Home Assistant codebase to ease maintenance.

It is necessary to provide the host, username and password when using the API.

Installation
------------

You can install PyTPLinkRouter from PyPi using `pip3 install pytplinkrouter`.

Usage
-----
To test run from the console:
`$ python -m pytplinkrouter <host> <username> <password>`

To use within your Python scripts:
```python
# All parameters are required
factory = TPLinkRouterFactory(host, username, password)
router = factory.get_router()
for i in router.scan_devices():
    print i
```

Supported routers
-----------------
The code is working with 6 versions of the TPLink router user interface. However I have no idea what router models are supported.
