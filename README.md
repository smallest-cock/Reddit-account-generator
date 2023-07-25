# Reddit-account-generator
Automates the process of signing up for a new reddit account. Also joins a random sub with the new account.

# How to use:
  1. Install requirements with `pip install -r requirements.txt`
  2. Edit `config.json` with new signup info between each run
  3. Run `python account_maker.py`
     - Sometimes the captcha fails, so you may need to wait for it to repeat the process a couple times before it suceeds
  4. Reddit account info will be stored in `accounts.json` upon completion

# Notes
Reddit has a registration cooldown of 10 min per account per IP... so use a VPN to make accounts faster, or just wait 10 mins between runs
