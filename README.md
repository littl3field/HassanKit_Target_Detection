# Targeted "XeroxProfessionals" Office365 Attack User Validation 
This script automates the checking of users contained within the "XeroxProfessionals" targeted attack dumps.

*I recommend running in a sandbox/off network environement*

### To use: 
```sh
$ git clone https://github.com/littl3field/O365PhishingCampaignValidation.git
```
```sh
$ cd O365PhishingCampaignValidation
$ pip install -r requirements.txt
```

Use a text editor to add your query in QUERY variable (I'll add a argparse soon)
[QUERY = "company"] <- Change this

### Output: 
result.txt = full list of data collected from the server
matches.txt = all users matched within the dataset

This is a quick bodge script to automate the task right now. I'll improve it if the attack continues.
I will add argparse soon to make querying easier, it's late AToW.
