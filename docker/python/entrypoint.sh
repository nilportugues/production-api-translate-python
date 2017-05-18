#!/bin/bash

service supervisor restart
systemctl enable supervisor

# Run forever.
tail -f /dev/null