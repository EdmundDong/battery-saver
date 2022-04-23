# Battery Saver
A quick program to switch on an off a IOT outlet to hopefully extend the life of my laptop battery.

This program uses [IFTTT](https://ifttt.com/) to handle the outlet switching. Any outlet that can be controlled through IFTTT would work. 

### Setup Program:
Webhook goes in `webhook.txt` in the following format:
<secret>

Get IFTTT secret from https://ifttt.com/maker_webhooks/settings.

It will be in this format: `https://maker.ifttt.com/use/<secret>`

### Setup Environment:
(Made for Windows)
```cmd
conda init
conda env create -f environment.yml
```
