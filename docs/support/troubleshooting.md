---
layout: template
title: Troubleshooting
permalink: /support/troubleshooting/
link_group: support
---
# Troubleshooting

If you are having problems, have a look at this page. There are currently not
much content here, please submit a PR or write an issue if you want to add or
change something.

### Scanning does not find any devices

Scanning relies on the Bonjour protocol (e.g. mDNS and Avahi are implementations
of this protocol on Linux). Since ``pyatv`` uses ``aiozeroconf``, which is a
standalone implementation that does not require any other service running, you
do not need any of those installed. It however helps when troubleshooting (and
most distributions come with avahi installed by default). So a simple start when
troubleshooting might be:

For Linux:

    $ avahi-browse --all

For macOS:

    $ dns-sd -B _appletv-v2._tcp.
    OR
    $ dns-sd -G -B _touch-able._tcp.
    OR
    $ dns-sd -G -B _mediaremotetv._tcp.

If you get an error such as "command not found", you do do not have avahi
installed. You will have to consult your distributions support channels
(e.g. forum) for help on this.

Here are some other possible sources of problems:

- Versions earlier than 0.3.0 of pyatv did not discover Apple TVs that did
  not have Home Sharing enabled. Just enable Home Sharing and upgrade to the
  latest and greatest version of pyatv and it should show up.
- Bonjour/Zeroconf requires you to be on the same network as the devices
  you are looking for. This means that you cannot scan for devices from
  inside of a container or virtual machine, unless they are usig a bridged
  network interface.
- If you are running a Mac or using an iPhone, try enabling AirPlay mirroring
  or use the Remote app. Unless you can get that to work, it is highly
  unlikely that pyatv will work either.
- If you can see your Apple TV on your iPhone, you can try to install an app
  suitable for Bonjour discovery. Just search for *bonjour* in the App store
  (there might be alternatives for Android as well) and lool for your device.
  If it's not found then pyatv will likely not fins it either.
- Firewalls might block the necessary traffic for Bonjour. Make sure the
  traffic is allowed or disable it when scanning.
- We have seen that switching the Apple TV from WiFi to cable solves the problem
  in some cases. It is recommended that you try it out.

If you continue having problems scanning for devices, consider writing a
[support issue](https://github.com/postlund/pyatv/issues/new?assignees=&labels=question&template=question-or-idea.md&title=).
Remember to include debug logs (`--debug` if you sre using `atvremote`).