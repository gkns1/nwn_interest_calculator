# nwn_interest_calculator
Simple script to calculate how many times and in-game bank interest has been accumulated. It accumulates every 48 minutes a character has been logged in. 

If someone logs out before the 48 minutes is up, the timer restarts and interest is lost. Logging has to be turned on in the game options for the script to work.

The logs are not utf-8 encoded, so regional characters are broken. It does not affect this script

By default set up to returns interest accumulated until the current timestamp. Interest until the last logged event can be called by get_increments(login, left)
