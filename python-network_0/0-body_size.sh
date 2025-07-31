#!/bin/bash
# Display body size in bytes
curl -s "$1" | wc -c
